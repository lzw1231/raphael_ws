import os
import ros_gz_sim
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    pkg_desc = get_package_share_directory("raphael_robot_description")
    pkg_bringup = get_package_share_directory("raphael_robot_bringup")

    urdf_file = os.path.join(pkg_desc, "urdf", "raphael_robot.urdf.xacro")
    rviz_config = os.path.join(pkg_bringup, "config", "view_raphael_robot.rviz")

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": Command(["xacro ", urdf_file])}],
        output="screen"
    )

    jsp_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", rviz_config],
        output="screen"
    )

    return LaunchDescription([
        robot_state_publisher,
        jsp_gui,
        rviz_node
    ])
