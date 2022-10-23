cmake_minimum_required(VERSION 3.13)

option(AFL "Using AFL++" OFF)
if (AFL)
    message("Using AFL++ compiler")
    set(CMAKE_C_COMPILER "/usr/local/bin/afl-cc")
    set(CMAKE_CXX_COMPILER "/usr/local/bin/afl-c++")
endif ()

project(fuzzing_group_02)
set(CMAKE_CXX_STANDARD 20)

# Add main.cpp file of project root directory as source file
set(SOURCE_FILES picojpeg.c picojpeg.h jpg2tga.c)


# Add executable target with source files listed in SOURCE_FILES variable
add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
add_executable(${CMAKE_PROJECT_NAME}_ASan ${SOURCE_FILES})
add_executable(${CMAKE_PROJECT_NAME}_MSan ${SOURCE_FILES})

target_compile_options(${CMAKE_PROJECT_NAME}_ASan PRIVATE -fsanitize=address)
target_link_options(${CMAKE_PROJECT_NAME}_ASan PRIVATE -fsanitize=address)

target_compile_options(${CMAKE_PROJECT_NAME}_MSan PRIVATE -fsanitize=memory -fPIE -pie -fno-omit-frame-pointer)
target_link_options(${CMAKE_PROJECT_NAME}_MSan PRIVATE -fsanitize=memory -fPIE -pie -fno-omit-frame-pointer)

target_link_libraries(${CMAKE_PROJECT_NAME} m)
target_link_libraries(${CMAKE_PROJECT_NAME}_ASan m)
target_link_libraries(${CMAKE_PROJECT_NAME}_MSan m)
