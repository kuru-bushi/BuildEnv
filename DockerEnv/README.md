## 概要
以前作成した Dockerfile まとめる

## その他
### pyenv
- Mac の場合
```
# 作成
## python3 -m venv {環境名}
## カレントディレクトリに 環境名のディレクトリが作成される
$ python3 -m venv test-venv

# 起動
## . {環境名}/bin/activate 
## もしくは source {環境名}/bin/activate
$. test-venv/bin/activate 

# 終了
$ deactivate

# 削除
{環境名}ディレクトリを削除
```

