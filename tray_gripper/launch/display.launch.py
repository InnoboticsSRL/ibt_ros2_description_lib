# @brief     Launch file for visualizing the models of the gripper tray_gripper
#
# @author    Mattia Dei Rossi <mattia.deirossi@innobotics.it>
# @copyright (C) IBT


import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():    
    pkg_dir = get_package_share_directory('tray_gripper')

    # Configuration files
    xacro_file = os.path.join(pkg_dir, 'xacro', 'tray_gripper.urdf.xacro')
    robot_description = ParameterValue(Command(['xacro', ' ', xacro_file, ' prefix:=tray_grippper']),
                                       value_type=str)
    rviz_config_path = os.path.join(pkg_dir, 'config', 'config.rviz')

    # Nodes
    robot_state_publisher_node = Node(
        name='robot_state_publisher',
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description': robot_description}
        ]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=[
            '-d', rviz_config_path
        ]
    )
    nodes = [
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ]

    return LaunchDescription(nodes)
