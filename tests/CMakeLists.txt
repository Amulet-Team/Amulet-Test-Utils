cmake_minimum_required(VERSION 3.13)

project(amulet_test_utils_tests LANGUAGES CXX)

# Set C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set platform variables
if (WIN32)
	# set windows 7 as the minimum version
	add_definitions(-D_WIN32_WINNT=0x0601)
elseif(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15")
else()
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()

# Find dependencies
find_package(pybind11 CONFIG REQUIRED)
find_package(amulet_test_utils CONFIG REQUIRED)

# Find sources
file(GLOB_RECURSE SOURCES LIST_DIRECTORIES false "${CMAKE_CURRENT_LIST_DIR}/*.py.cpp")

pybind11_add_module(_test_test_utils)
target_compile_definitions(_test_test_utils PRIVATE PYBIND11_DETAILED_ERROR_MESSAGES)
target_link_libraries(_test_test_utils PRIVATE amulet_test_utils)
target_sources(_test_test_utils PRIVATE ${SOURCES})
foreach(FILE ${SOURCES})
    file(RELATIVE_PATH REL_PATH ${CMAKE_CURRENT_LIST_DIR} ${FILE})
    get_filename_component(GROUP ${REL_PATH} DIRECTORY)
    string(REPLACE "/" "\\" GROUP "${GROUP}")
    source_group(${GROUP} FILES ${FILE})
endforeach()

# Install
install(TARGETS _test_test_utils DESTINATION ".")
