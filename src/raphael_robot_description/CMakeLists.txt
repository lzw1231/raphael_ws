cmake_minimum_required(VERSION 4.3.2)
project(raphael_robot_description)

if (CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif ()

find_package(ament_cmake REQUIRED)

install(
        DIRECTORY meshes urdf
        DESTINATION share/${PROJECT_NAME}/
)

install(FILES LICENSE DESTINATION share/${PROJECT_NAME})

ament_package()
