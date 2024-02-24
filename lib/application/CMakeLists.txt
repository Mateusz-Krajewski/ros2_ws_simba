cmake_minimum_required(VERSION 3.8)
project(IApplication)


set(CMAKE_CXX_STANDARD 23)

find_package(rclcpp REQUIRED)
find_package(diag_interfaces REQUIRED)

# Include directories
include_directories(
    ${rclcpp_INCLUDE_DIRS}
    ${diag_interfaces_INCLUDE_DIRS}
)

# Sources
set(SOURCES
    IApplication.hpp
    IApplication.cpp
)

add_library(IApplication SHARED ${SOURCES})

target_link_libraries(IApplication PUBLIC ${rclcpp_LIBRARIES})


install(TARGETS IApplication
  DESTINATION lib
)

install(FILES IApplication.hpp
    DESTINATION include/${PROJECT_NAME})



