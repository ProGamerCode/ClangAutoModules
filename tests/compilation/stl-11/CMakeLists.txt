cmake_minimum_required(VERSION 3.0)
project (stl11-full)

add_compile_options(-std=c++11)

include(clang-modules/ClangModules.cmake)

add_executable(stl-full main.cpp)
