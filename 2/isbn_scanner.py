"""
WEBカメラで本のバーコード（ISBN）を読み取り、Amazonのリンク付きの蔵書リスト（CSV）を作る

準備:  pip install opencv-python requests
実行:  python isbn_scanner.py
       本の裏表紙のバーコードをカメラにかざす。q キーで終了

※ Colab ではPCのカメラを直接使えないので、自分のPCで実行する
※ 書名などは openBD (https://openbd.jp/) から取得する
"""
import csv
import os

import cv2
import requests

CSV_FILE = 'books.csv'


def isbn13_to_isbn10(isbn13):
    """978から始まるISBN-13をISBN-10に変換する（AmazonのURLに使う）"""
    body = isbn13[3:12]
    s = sum((10 - i) * int(d) for i, d in enumerate(body))
    check = (11 - s % 11) % 11
    return body + ('X' if check == 10 else str(check))


def amazon_url(isbn13):
    if isbn13.startswith('978'):
        return f'https://www.amazon.co.jp/dp/{isbn13_to_isbn10(isbn13)}'
    return f'https://www.amazon.co.jp/s?k={isbn13}'  # 979で始まるISBNはISBN-10がないので検索URL


def lookup(isbn13):
    """openBD から 書名, 著者, 出版社 を取得する。見つからなければ空文字"""
    try:
        r = requests.get('https://api.openbd.jp/v1/get', params={'isbn': isbn13}, timeout=10)
        book = r.json()[0]
    except Exception:
        return '', '', ''
    if book is None:
        return '', '', ''
    s = book['summary']
    return s['title'], s['author'], s['publisher']


def load_isbns():
    """すでにCSVに登録したISBNの集合（同じ本を二重に登録しないため）"""
    if not os.path.exists(CSV_FILE):
        return set()
    with open(CSV_FILE, encoding='utf-8-sig') as f:
        return {row['ISBN'] for row in csv.DictReader(f)}


def main():
    registered = load_isbns()
    is_new_file = not os.path.exists(CSV_FILE)
    detector = cv2.barcode.BarcodeDetector()
    cap = cv2.VideoCapture(0)  # 0番のカメラ。映らなければ 1 にする

    # utf-8-sig にするとExcelで開いても文字化けしない
    with open(CSV_FILE, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(['ISBN', '書名', '著者', '出版社', 'Amazon'])

        while True:
            ok, frame = cap.read()
            if not ok:
                print('カメラから画像を取得できない')
                break

            found, codes, types, points = detector.detectAndDecodeWithType(frame)
            if found:
                for code, pts in zip(codes, points):
                    # 日本の本はバーコードが2段。上段の978/979で始まる方がISBN（下段192...は価格コード）
                    if not (len(code) == 13 and code.startswith(('978', '979'))):
                        continue
                    cv2.polylines(frame, [pts.astype(int)], True, (0, 255, 0), 3)
                    cv2.putText(frame, code, pts[1].astype(int), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    if code in registered:
                        continue
                    title, author, publisher = lookup(code)
                    writer.writerow([code, title, author, publisher, amazon_url(code)])
                    f.flush()  # 途中で止めても記録が残るようにすぐ書き込む
                    registered.add(code)
                    print(f'登録: {code} {title} / {author}')

            cv2.imshow('ISBN scanner (q: quit)', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    print(f'{len(registered)} 冊を {CSV_FILE} に登録済み')


if __name__ == '__main__':
    main()
