
# ビルドと実行
```
# docker build -t {イメージ名} {Dockerfile のパスがあるディレクトリ}
docker build -t cpp_tutorial .

# 
docker run -t -i -d  -v $(pwd):/home --name cpp_tutorial_cnt cpp_tutorial /bin/bash
```

# ceres-solver
[公式ドキュメント](http://ceres-solver.org/installation.html), [参考1](https://qiita.com/keita-n-ac/items/06f4214c7ae3292c5e44), [参考2](https://ltslam-doc.readthedocs.io/en/latest/tutorial/ceres/ceres_solver_tutorial.html)
```
apt-get install -y libgoogle-glog-dev libgflags-dev
apt-get install -y libatlas-base-dev
apt-get install -y libeigen3-dev
apt-get install -y libsuitesparse-dev

git clone https://ceres-solver.googlesource.com/ceres-solver -b 2.2.0

mkdir ceres-bin
cd ceres-bin
cmake ../ceres-solver
make -j3
make test
# Optionally install Ceres, it can also be exported using CMake which
# allows Ceres to be used without requiring installation, see the documentation
# for the EXPORT_BUILD_DIR option for more information.
make install

```
