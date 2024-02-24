cmake_minimum_required(VERSION 3.8)
project(AppLogger)

set(CMAKE_CXX_STANDARD 23)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR})


find_package(spdlog REQUIRED)

# Sources
set(SOURCES
    Logger.cpp
    logger_factory.cc
    console_logger.cc
    dlt_logger.cc
)

# Headers
set(HEADERS
    ILogger.h
    Logger.h
    logger_factory.h
    console_logger.h
    dlt_logger.h
)

# Create library
add_library(logger_library ${SOURCES} ${HEADERS})

# Add dependencies
target_link_libraries(logger_library
    PUBLIC
        Common
        Results
        spdlog
        sockets
)

# Set visibility
target_compile_options(logger_library PRIVATE -fvisibility=default)

# Install library
install(TARGETS logger_library
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Install headers
install(FILES ${HEADERS} DESTINATION include/logger)
