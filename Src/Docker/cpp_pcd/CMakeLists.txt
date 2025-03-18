cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(tutorial_visualization_voxel)

find_package(PCL 1.2 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})


add_executable (tutorial_visualization_voxel tutorial_visualization_voxel.cpp)
target_link_libraries (tutorial_visualization_voxel ${PCL_LIBRARIES})

target_include_directories(tutorial_visualization_voxel PRIVATE ${CMAKE_SOURCE_DIR})