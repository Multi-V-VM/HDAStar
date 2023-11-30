cmake_minimum_required(VERSION 3.10)
project(hw5 C)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wpedantic -Wextra -lpthread -D_WASI_EMULATED_MMAN -lwasi-emulated-mman     -O3 -pthread  -z stack-size=32768      -Wl,--shared-memory             -Wl,--initial-memory=131072,--max-memory=131072")
set(CMAKE_C_FLAGS_DEBUG  "${CMAKE_C_FLAGS_DEBUG} -g")
set(CMAKE_C_FLAGS_RELEASE  "${CMAKE_C_FLAGS_RELEASE} -O1")

add_executable(hw5 main.c heap.h heap.c maze.h maze.c node.h node.c compass.h)
