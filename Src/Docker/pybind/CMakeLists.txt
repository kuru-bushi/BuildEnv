cmake_minimum_required(VERSION 3.4...3.18)
project(mycat)

add_subdirectory(pybind11)
pybind11_add_module(mycat mycat.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(mycat
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
