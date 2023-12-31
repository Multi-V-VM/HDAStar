cmake_minimum_required(VERSION 3.10)
project(hw5 C)

set(CMAKE_C_STANDARD 90)

add_executable(hw5 main.c heap.h heap.c maze.h maze.c node.h node.c compass.h)
