
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
