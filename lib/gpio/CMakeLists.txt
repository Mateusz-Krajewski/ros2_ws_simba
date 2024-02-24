cmake_minimum_required(VERSION 3.8)
project(GPIO_Library)

# Dodaj pliki źródłowe
set(SOURCES
    GPIO_digital_driver.cpp
)

# Dodaj pliki nagłówkowe
set(HEADERS
    IGPIO_digital_driver.h
    GPIO_digital_driver.h
)


# Utwórz bibliotekę gpio_drivers
add_library(gpio_drivers ${SOURCES} ${HEADERS})
target_include_directories(gpio_drivers PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(gpio_drivers PUBLIC gpio_interface)
