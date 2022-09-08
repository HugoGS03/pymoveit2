#!/usr/bin/env python3
"""
Example of moving to a pose goal.
`ros2 run pymoveit2 ex_pose_goal.py --ros-args -p position:="[0.25, 0.0, 1.0]" -p quat_xyzw:="[0.0, 0.0, 0.0, 1.0]" -p cartesian:=False`
"""

from threading import Thread

import rclpy
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.node import Node

from pymoveit2 import MoveIt2
from pymoveit2 import MoveIt2Gripper

from pymoveit2.robots import ur5


    

def main(args=None):

    rclpy.init(args=args)

    # Create node for this example
    moveit_node = Node("ex_pose_goal")




    # Declare parameters for position and orientation
    moveit_node.declare_parameter("position", [0.4, 0.6, 0.05])
    moveit_node.declare_parameter("quat_xyzw", [1.0, 0.0, 0.0, 0.0])
    moveit_node.declare_parameter("cartesian", True)



    # Create callback group that allows execution of callbacks in parallel without restrictions
    callback_group = ReentrantCallbackGroup()

    # Create MoveIt 2 interface
    moveit2 = MoveIt2(
        node=moveit_node,
        joint_names=ur5.joint_names(),
        base_link_name=ur5.base_link_name(),
        end_effector_name=ur5.end_effector_name(),
        group_name=ur5.MOVE_GROUP_ARM,
        callback_group=callback_group,
        execute_via_moveit=True,
    )

    # Create node for this example
    gripper_node = Node("ex_gripper")
    # Declare parameter for joint positions
    gripper_node.declare_parameter(
        "action",
        "toggle",
    )
    # Create MoveIt 2 gripper interface
    moveit2_gripper = MoveIt2Gripper(
        node=gripper_node,
        gripper_joint_names=ur5.gripper_joint_names(),
        open_gripper_joint_positions=ur5.OPEN_GRIPPER_JOINT_POSITIONS,
        closed_gripper_joint_positions=ur5.CLOSED_GRIPPER_JOINT_POSITIONS,
        gripper_group_name=ur5.MOVE_GROUP_GRIPPER,
        callback_group=callback_group,
    )

    # Spin the node in background thread(s)
    executor = rclpy.executors.MultiThreadedExecutor(2)
    executor.add_node(moveit_node)
    executor.add_node(gripper_node)
    executor_thread = Thread(target=executor.spin, daemon=True, args=())
    executor_thread.start()

    # Get parameters
    position = moveit_node.get_parameter("position").get_parameter_value().double_array_value
    quat_xyzw = moveit_node.get_parameter("quat_xyzw").get_parameter_value().double_array_value
    cartesian = moveit_node.get_parameter("cartesian").get_parameter_value().bool_value

    period_s = 1.0
    rate = gripper_node.create_rate(1 / period_s)
# Get parameter
    action = gripper_node.get_parameter("action").get_parameter_value().string_value

  
    # Move to pose
    moveit_node.get_logger().info(
        f"Moving to {{position: {list(position)}, quat_xyzw: {list(quat_xyzw)}}}"
    )
    moveit2.move_to_pose(position=position, quat_xyzw=quat_xyzw, cartesian=cartesian)
    moveit2.wait_until_executed()
    '''
    moveit2_gripper.close()
    moveit2_gripper.wait_until_executed()
    
    moveit2_gripper.open()
    moveit2_gripper.wait_until_executed()
    moveit2_gripper.close()
    moveit2_gripper.wait_until_executed()
    moveit2_gripper.open()
    moveit2_gripper.wait_until_executed()
    '''
    rclpy.shutdown()
    exit(0)
  

if __name__ == "__main__":
    main()
