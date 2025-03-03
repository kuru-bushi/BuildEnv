

apt-get install -y libgoogle-glog-dev libgflags-dev
apt-get install -y libatlas-base-dev
apt-get install -y libeigen3-dev
apt-get install -y libsuitesparse-dev
apt-get install cmake make git -y

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