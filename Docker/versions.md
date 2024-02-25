
https://www.kkaneko.jp/tools/wsl/wsl_tensorflow2.html


## pytroch GPU のバージョン合わせ
- Windows(WSL2) 環境
- cmd にて
    - nvcc -V
- pytorch イメージのについて
    - [pytorch 公式イメージ](https://hub.docker.com/r/pytorch/pytorch/tags)
    - [イメージ例](https://hub.docker.com/layers/pytorch/pytorch/1.13.1-cuda11.6-cudnn8-runtime/images/sha256-1e26efd426b0fecbfe7cf3d3ae5003fada6ac5a76eddc1e042857f5d049605ee?context=explore)
    `
    FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime
    `

## docker compose と docker-compose の違い
- docker compose は V2 より利用可能
- docker-compose は廃止される可能性がある
- 今後は docker compose を使う
    - 参考: https://www.konosumi.net/entry/2023/02/26/142508

## docker containier が recreate される問題
- 別プロジェクトでも同じディレクトリ名だとコンテナが置き換わってしまう
- 対処方法
    - 1. プロジェクト名を -p で指定
    - 2. ディレクトリごとにドッカーファイルを作成
- 参考
    - https://qiita.com/satons/items/0597d2be64a56eaf4f89