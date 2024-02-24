cmake_minimum_required(VERSION 3.8)

# Ustaw nazwę twojej biblioteki
project(Result)

# Utwórz listę plików źródłowych
set(SOURCES 
    result.h
)

# Dodaj bibliotekę
add_library(${PROJECT_NAME} ${SOURCES})

# Ustaw widoczność interfejsu
target_include_directories(${PROJECT_NAME} PUBLIC include)
set_target_properties(Result PROPERTIES LINKER_LANGUAGE CXX)
