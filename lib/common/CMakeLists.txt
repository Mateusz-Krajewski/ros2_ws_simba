cmake_minimum_required(VERSION 3.8)
project(common)

add_library(common INTERFACE)
target_include_directories(common INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
target_sources(common INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/error_code.h 
                                 ${CMAKE_CURRENT_SOURCE_DIR}/wait_queue.h 
                                 ${CMAKE_CURRENT_SOURCE_DIR}/endianess_converter.h)
target_compile_definitions(common INTERFACE VISIBILITY_PUBLIC)
