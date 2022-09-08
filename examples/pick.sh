ros2 topic pub /gripper_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "header: 
  stamp: 
    sec: 0
    nanosec: 0
  frame_id: ''
joint_names: ['panda_finger_joint1', 'panda_finger_joint2']
points: 
  - 
    positions: [0.14, 0.14]
    velocities: []
    accelerations: []
    effort: []
    time_from_start: 
      sec: 2
      nanosec: 990099009" --once
      
ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "header: 
  stamp: 
    sec: 0
    nanosec: 0
  frame_id: ''
joint_names: ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']
points: 
  - 
    positions: [1.79433, 0.762, -1.242, -1.597,  -0.606, 2.706, 2.89]
    velocities: []
    accelerations: []
    effort: []
    time_from_start: 
      sec: 2
      nanosec: 990099009" --once
      
ros2 topic pub /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "header: 
  stamp: 
    sec: 0
    nanosec: 0
  frame_id: ''
joint_names: ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6', 'panda_joint7']
points: 
  - 
    positions: [0.0, -0.785, 0.0, -2.356,  0.0, 1.571, 0.785]
    velocities: []
    accelerations: []
    effort: []
    time_from_start: 
      sec: 2
      nanosec: 990099009" --once

sleep 3          
ros2 run pymoveit2 ex_gripper.py --ros-args --param  action:=close
ros2 run pymoveit2 ex_gripper.py --ros-args --param  action:=open
ros2 run pymoveit2 ex_pose_goal.py --ros-args --param  position:='[0.8, 0.0, 0.15]'
ros2 run gazebo_ros spawn_entity.py  -file /home/arshad/.gazebo/models/marker_0/model.sdf  -entity test3 -x 0.8  -y .0 -z 0
ros2 run pymoveit2 ex_gripper.py --ros-args --param  action:=open
ros2 run pymoveit2 ex_pose_goal.py --ros-args --param  position:='[0.8, 0.0, 0.02]'
ros2 run pymoveit2 ex_gripper.py --ros-args --param  action:=close
ros2 run pymoveit2 ex_pose_goal.py --ros-args --param  position:='[0.8, 0.0, 0.15]'


