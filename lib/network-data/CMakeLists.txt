cmake_minimum_required(VERSION 3.8)
project(CommunicationLibrary)

# Dodaj pliki nagłówkowe
set(HEADERS
    iframe.h
    network_data_structure.h
    network_data_type.h
)

# Dodaj pliki źródłowe
set(SOURCES
    network_data_structure.cc
)

# Utwórz bibliotekę CommunicationLibrary
add_library(CommunicationLibrary ${SOURCES} ${HEADERS})

# Dodaj katalog bieżący jako katalog include
target_include_directories(CommunicationLibrary PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Zależności
target_link_libraries(CommunicationLibrary PUBLIC core)

