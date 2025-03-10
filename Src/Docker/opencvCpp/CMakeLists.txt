cmake_minimum_required(VERSION 3.13)
project(Lucas_kanade CXX)
# hello.cppとgood_morning.cppをコンパイルして静的ライブラリlibgreetings.aを作成

# find_package(OpenCV REQUIRED)
# include_directories(${OpenCV_INCLUDE_DIRS})
set(OpenCV_DIR "../libs/opencv/build")

# OpenCVを探す
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# a.outという実行ファイルをmain.cppから作成
add_executable(Lucas_kanade ../Lucas_kanade.cpp)
target_link_libraries(Lucas_kanade ${OpenCV_LIBS})
