cmake_minimum_required(VERSION 3.13)
project(MRB-Ventilatorbuis)

find_package(OpenCV REQUIRED)
set(CMAKE_CXX_STANDARD 17)

add_executable(MRB-Ventilatorbuis main.cpp)

include_directories(${OpenCV_INCLUDE_DIRS})
target_link_libraries(MRB-Ventilatorbuis ${OpenCV_LIBS})