cmake_minimum_required(VERSION 3.8)
project(sockets)

add_subdirectory(../common Common)

set(CMAKE_CXX_STANDARD 23)

set(HEADERS
    "Isocket.h"
    "socket_config.h"
    "ipc_socket.h"
    "udp_socket.h"
    "udp_multicast_socket.h"
)

set(SOURCES
    "ipc_socket.cc"
    "udp_socket.cc"
    "udp_multicast_socket.cc"
)

add_library(sockets ${HEADERS} ${SOURCES})

# Include the directory where error_code.h resides
target_include_directories(sockets PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}"
    "${CMAKE_CURRENT_SOURCE_DIR}/../Common/include"
)

# Link against the Common library
target_link_libraries(sockets PUBLIC Common)
