# 参考文献

## 無料テキスト

* [python.jp](https://www.python.jp/index.html)
  * [ゼロからのPython入門講座](https://www.python.jp/train/index.html): Colabの使い方、基本的な文法はここで学べます。
  * [Python環境構築ガイド](https://www.python.jp/install/install.html):自分のPCで動かしたい人向け。

### Colab前提で書かれている

* [Pythonプログラミング入門@東大数理・情報教育研究センター](https://utokyo-ipp.github.io/) 詳しく書かれているので辞書的に使うのがよい。
* [Python早見帳@東工大(現：東京科学大)](https://chokkan.github.io/python/index.html)

### 自分のPCで動かすことを前提に書かれている

* [プログラミング演習 Python 2023@京大](https://repository.kulib.kyoto-u.ac.jp/handle/2433/285599) 自分のPCで動かすことが前提となっている。
* [Pythonゼロからはじめるプログラミング@筑波大](https://mitani.cs.tsukuba.ac.jp/book_support/python/)
書籍もあるが学習用教材だけでも有用

### 機械学習までカバーする内容

* [医療とAI・ビッグデータ@旧東京医科歯科大（現：東京科学大） 2023年度](https://www.tmd.ac.jp/labs/education/ds/)
[2022年ワークショップ](https://github.com/TMDU-AI/workshop2022)
2023年版はColab向け、2022年版はPC用
* [医療とAIはじめの一歩](https://www.yodosha.co.jp/yodobook/book/9784758124188/) 上の内容を書籍化したもの。図書館にあり。
* [機械学習帳@東工大（現：東京科学大）](https://chokkan.github.io/mlnote/index.html) 難しいが数理をきちんと追いたい人には有用

### 図書館にある書籍

* [Pythonによる医用画像処理入門 改訂2版(上杉正人、平原大助編)](https://v3opac2.kyorin-u.ac.jp/webopac/BB10229791)
  
* [神経科学者と学ぶ深層学習超入門 : AIの種を知り、知識の樹を育て、研究で最新モデルを使いこなす
(渡辺英治)](https://v3opac2.kyorin-u.ac.jp/webopac/BB10229769)

* [大規模データで困ったときに、まず図を描くことからはじめる生命科学データ解析 : 解析のゴールドスタンダードを学び、生成AIとの対話でPython・Rを使いこなす(河野暢明編)](https://v3opac2.kyorin-u.ac.jp/webopac/BB10228909)

* [独習Pythonバイオ情報解析 : 生成AI時代に活きるJupyter、NumPy、pandas、Matplotlib、Scanpyの基礎を身につけ、シングルセル、RNA-Seqデータ解析を自分の手で](https://v3opac2.kyorin-u.ac.jp/webopac/BB10226184)

* [Pythonで実践 : 生命科学データの機械学習 : あなたのPCで最先端論文の解析レシピを体得できる!](https://v3opac2.kyorin-u.ac.jp/webopac/BB10211510)

## よく使われるライブラリ

* [numpy](https://numpy.org/ja/) 数学関数、数値計算全般で必須
* [matplotlib](https://matplotlib.org/) グラフを描くためのツール [チートシート](https://github.com/matplotlib/cheatsheets?tab=readme-ov-file)　[scientific visualization](https://github.com/rougier/scientific-visualization-book)
* [pandas](https://pandas.pydata.org/) excel,csvの表形式データの取り込みなどデータ解析に有用 [チートシート](https://github.com/pandas-dev/pandas/blob/main/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
* [seaborn](https://seaborn.pydata.org/) 統計データの可視化
* [scikit-learn](https://scikit-learn.org/stable/index.html) 機械学習全般で使うツール
* [tensorflow](https://www.tensorflow.org/?hl=ja) 多次元データ（テンソル）の処理
* [tensorflow playground](https://playground.tensorflow.org/) コードを書かずに試せる
* [keras](https://keras.io/) 深層学習のライブラリ（Keras 3からはTensorFlow/PyTorch/JAXのいずれでも動作）
* [PyTorch](https://pytorch.org/) tensorflowと同様に多次元データ用のライブラリ
* [ライブラリブック](https://k-techlabo.org/www_python/python_modules.pdf)各種ライブラリの使用法

## 有名な書籍

* [deeplearningbook](https://www.deeplearningbook.org/) Goodfellow
[翻訳された書籍](https://www.amazon.co.jp/dp/B07GQV1X76)
* [pattern recognition and machine learning](https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) Bishop
* [Deep Learning: Foundations and Concepts](https://www.bishopbook.com/) Bishop & Bishop (2024) PRMLの後継書。Web版は無料で閲覧可
* [Deep Kearning with Python](https://deepleaserningwithpython.io/) Chollet  翻訳本は図書館にある

## データセット

* [UC Irvine](https://archive.ics.uci.edu/) Taskから分類、回帰、クラスターなど目的に合うデータを探すことができ、
pythonコードから直接ダウンロードできる仕組みもある。
* [COVID-19 X-ray Dataset](https://github.com/agchung/Actualmed-COVID-chestxray-dataset)
* [kaggle](https://www.kaggle.com/) 様々なデータとそれに対する他の人の解決方法を学べる
* [physionet](https://physionet.org/about/database/) 生理学的シグナルや医療データのコレクション
* [tensorflow datasets](https://www.tensorflow.org/datasets?hl=ja)

## AlphaFold関連

* [AlphaFold Server](https://alphafoldserver.com/welcome) 登録すれば非商用目的で使える。タンパク配列を入れるだけでコーディング不要
* [AlphaFold3](https://github.com/google-deepmind/alphafold3) 2024年11月にコード公開（モデルの重みは申請制、非商用）
* [AlphaFold3の解説](https://zenn.dev/tonets/articles/dd8c3855eadb2b)
* [ColabFold](https://github.com/sokrypton/ColabFold) Google Colabで動く。AlphaFold2ベースで多量体（AlphaFold-Multimer）は予測できるが、低分子・核酸との複合体などAlphaFold3の機能は非対象

## 顕微鏡画像関連

* [scikit-image: image processing](https://scikit-image.org/)
* [napari: a fast, interactive viewer for multi-dimensional images in Python](https://napari.org/stable/)
* [cellpose: a generalist algorithm for cellular segmentation](https://www.cellpose.org/)
* [Trackpy: Fast, Flexible Particle-Tracking Toolkit](https://soft-matter.github.io/trackpy/v0.7/)

## DICOMなど医用画像関連

* [pydicom](https://github.com/pydicom/pydicom)
* [SimpleITK](https://simpleitk.org/)
* [NiBabel](https://nipy.org/nibabel/)
* [MONAI:Medical Open Network for Artificial Intelligence](https://project-monai.github.io/)

## その他

* [teachable machine](https://teachablemachine.withgoogle.com/) 画像をアップロードすると、機械学習モデルを作成できる。コーディング不要
* [pythontutor](https://pythontutor.com/python-compiler.html#mode=edit) ステップバイステップで実行しながら、変数の変化を見ることができる
* [マンガと学ぶデータビジュアライゼーション](https://kakeami.github.io/viz-madb/index.html) 少年マンガのデータを使って、データ可視化の方法が学べる。
* [chatGPTを用いたコーディング習得方法](https://speakerdeck.com/keio_smilab/keio-univ-intro-to-ml-02-coding)
* [滋賀大の動画教材](https://www.youtube.com/@%E6%95%B0%E7%90%86%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%82%B9%E6%95%99%E8%82%B2%E5%BC%B7%E5%8C%96/videos)
* [google機械学習集中講座](https://developers.google.com/machine-learning/crash-course?hl=ja)
