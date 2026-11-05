"""
フォルダに入れた論文のPDFから、文献リスト（Markdown）を作る

準備:  pip install pymupdf requests
実行:  python pdf_references.py papers      （papers はPDFを入れたフォルダ）
       → papers/references.md ができる

仕組み:
  1. PDFの最初の2ページの文字からDOI（論文の識別番号 10.xxxx/...）を探す
     arXivの論文は arXiv:2401.12345 のような番号からDOIを作る
  2. https://doi.org/ に問い合わせて、著者・題名・雑誌名・年などを取得する
     （Crossref, JaLC(日本の論文), DataCite(arXiv) のどれに登録されたDOIでも使える）
  3. DOIが見つからないPDFは、PDFに記録された題名かファイル名を表示する
"""
import os
import re
import sys

import fitz  # PyMuPDF。pypdfより日本語や文字間隔の崩れたPDFを正しく読める
import requests

DOI_RE = re.compile(r'10\.\d{4,9}/[^\s"<>]+')
ARXIV_RE = re.compile(r'arXiv:\s*(\d{4}\.\d{4,5})', re.IGNORECASE)


def find_dois(path, pages=2):
    """PDFの最初の数ページからDOIの候補を、見つかった順に返す"""
    with fitz.open(path) as doc:
        text = ''.join(doc[i].get_text() for i in range(min(pages, len(doc))))
        text += str(doc.metadata or '')  # PDFの属性にDOIが書かれていることもある
    dois = [d.rstrip('.,;)]}') for d in DOI_RE.findall(text)]
    dois += [f'10.48550/arXiv.{a}' for a in ARXIV_RE.findall(text)]
    return list(dict.fromkeys(dois))  # 重複を除く（順番は保つ）


def pdf_title(path):
    """PDFに記録されている題名。なければ空文字"""
    try:
        with fitz.open(path) as doc:
            return (doc.metadata or {}).get('title', '').strip()
    except Exception:
        return ''


def lookup_doi(doi):
    """doi.org から書誌情報(CSL-JSON)を取得する。見つからなければ None"""
    try:
        r = requests.get(f'https://doi.org/{doi}', timeout=15,
                         headers={'Accept': 'application/vnd.citationstyles.csl+json'})
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None


def format_authors(authors, n=3):
    """著者を最大n人まで。多い場合は et al."""
    names = []
    for a in authors[:n]:
        family, given = a.get('family', ''), a.get('given', '')
        if re.search(r'[ぁ-んァ-ン一-龥]', family):  # 日本語の名前は「姓名」
            names.append(family + given)
        else:  # 英語の名前は「姓 イニシャル」
            initials = ''.join(w[0] for w in re.split(r'[\s.-]+', given) if w)
            names.append(f'{family} {initials}'.strip())
        if not family:
            names[-1] = a.get('literal', '')
    s = ', '.join(names)
    return s + (', et al' if len(authors) > n else '')


def format_reference(m):
    """書誌情報を 著者. 題名. 雑誌名. 年;巻(号):頁. の形にする"""
    year = m.get('issued', {}).get('date-parts', [['']])[0][0]
    journal = m.get('container-title') or m.get('publisher', '')
    if isinstance(journal, list):
        journal = journal[0] if journal else ''
    authors = format_authors(m.get('author', []))
    s = (f'{authors}. ' if authors else '') + f"{m.get('title', '')}. {journal}. {year}"
    issue = m.get('issue') or m.get('number')  # 日本の論文(JaLC)は号が number に入っている
    if m.get('volume'):
        s += f";{m['volume']}"
        if issue:
            s += f'({issue})'
        if m.get('page'):
            s += f":{m['page']}"
    return s + '.'


def make_references(folder):
    pdfs = sorted(f for f in os.listdir(folder) if f.lower().endswith('.pdf'))
    entries = []
    for name in pdfs:
        path = os.path.join(folder, name)
        try:
            dois = find_dois(path)
        except Exception as e:
            print(f'{name}: PDFを読めない ({type(e).__name__})')
            dois = []
        meta = None
        for doi in dois:  # 参考文献のDOIが先に見つかることもあるので、取得できるまで順に試す
            meta = lookup_doi(doi)
            if meta:
                break
        if meta:
            ref = format_reference(meta)
            link = f"[doi:{meta['DOI']}](https://doi.org/{meta['DOI']})"
            year = meta.get('issued', {}).get('date-parts', [[0]])[0][0] or 0
            print(f'{name}: {ref}')
        else:
            ref = f"{pdf_title(path) or os.path.splitext(name)[0]}.（DOI不明）"
            link = ''
            year = 0
            print(f'{name}: DOIが見つからない')
        # ファイル名に空白などがあってもリンクが切れないように <> で囲む
        entries.append((year, f'{ref} {link} [PDF](<{name}>)'))

    entries.sort(key=lambda e: e[0], reverse=True)  # 新しい順
    lines = ['# 文献リスト', '', f'{len(entries)} 件', '']
    lines += [f'{i}. {text}' for i, (_, text) in enumerate(entries, 1)]
    out = os.path.join(folder, 'references.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'→ {out}')


if __name__ == '__main__':
    make_references(sys.argv[1] if len(sys.argv) > 1 else 'papers')
