# アーキテクト例
- モデルの class method
    - read_data, preprocess, train, test, 
    - train で別ファイルのモデル読み込む
    - handler.py 処理のフローまとめる model まとめる
    - config 作るとわかりやすい
    - opt = args を使うとセルで動かすとエラーが出るため、config から読み込む方が汎用性高い
- pring の代わりに logzero 
    - ../log に出力
