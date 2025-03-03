FROM ubuntu:20.04

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y wget unzip curl
# Install compilers.
RUN apt-get install -y gcc && \
    apt-get install -y g++

# SET path to compilers.
# https://stackoverflow.com/questions/17275348/how-to-specify-new-gcc-path-for-cmake
ENV CC=/usr/bin/gcc \
    CXX=/usr/bin/g++

CMD bash
