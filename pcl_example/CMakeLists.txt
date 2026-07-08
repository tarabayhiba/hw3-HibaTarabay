cmake_minimum_required(VERSION 3.10)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(voxel_demo)

# This also brings PCL related flags, just like how we have CMAKE_EXPORT_COMPILE_COMMANDS or CMAKE_SOURCE DIR
find_package(PCL 1.12 REQUIRED) 

add_executable(voxel_demo main.cpp)

target_include_directories(voxel_demo PRIVATE
    ${PCL_INCLUDE_DIRS}
)

target_link_directories(voxel_demo PRIVATE
    ${PCL_LIBRARY_DIRS}
)
# Add the flags we got from PCL in the compile command
target_compile_definitions(voxel_demo PRIVATE
    ${PCL_DEFINITIONS}
)

target_link_libraries(voxel_demo PRIVATE
    ${PCL_LIBRARIES}
)
