cat /proc/$(pgrep gzserver)/maps  | grep update
python ex_pose_goal.py --ros-args -p position:='[.3,.3,.1]'

 2015  objdump -t /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/joint_trajectory_controller/libjoint_trajectory_controller.so | c++filt  | grep update
 2016  sudo perf probe -x  /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/joint_trajectory_controller/libjoint_trajectory_controller.so -a update=0x21b082
 2017  sudo perf probe -x  /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/joint_trajectory_controller/libjoint_trajectory_controller.so -a update=0x21b082%return

 2041  perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a 0x2347ac=cm_update
 2042  sudo perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a cm_update=0x2347ac
 2043  sudo perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a cm_update=0x2347ac%return
 2044  sudo perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a cm_read=0x0000000000234776
 2045  sudo perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a cm_read=0x0000000000234776%return
 2046  sudo perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a cm_write=0x000000000023498a
 2047  sudo perf probe -x /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/build/controller_manager/libcontroller_manager.so -a cm_write=0x000000000023498a%return
sudo perf record -e probe_libcontroller_manager:* -aR sleep 1

ros2 run gazebo_ros spawn_entity.py -topic /robot2/robot_description -entity robot2 -robot_namespace /robot2 -x -3.5 -y 7.0 -z 0.0 -unpause

find . -name package.xml | xargs -i{} dirname {} | xargs -i{} touch {}/COLCON_IGNORE


objdump -t /home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/install/rclcpp/lib/librclcpp.so | c++filt  | grep execute_callback

ros2 control load_controller --set-state start arm_controller -c /robot1/controller_manager
ros2 control set_controller_state  arm_controller stop -c /robot1/controller_manager
ros2 control unload_controller  arm_controller  -c /robot1/controller_manager
python controller.py --namespace /robot1


ros2  topic pub -1 --qos-reliability reliable /initialpose geometry_msgs/PoseWithCovarianceStamped "{header: {frame_id: map}, pose: {pose: {position: {x: -0.6, y: 0.0, z: 0.0},              orientation: {x: 0.0, y: 0.0, z: -0.00460209633546322, w: 1.0000000}},        covariance: [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]}}"

ros2 action send_goal  /navigate_to_pose nav2_msgs/action/NavigateToPose "pose: {header: {frame_id: map}, pose: {position: {x: -3.2, y: 6.20, z: 0.0}, orientation:{x: 0.0, y: 0.0, z: 0, w: 1.0000000}}}" 


auto rcl_context = impl_->model_nh_->get_node_base_interface()->get_context()->get_rcl_context();
  rcl_ret_t rcl_ret = rcl_parse_arguments(
    static_cast<int>(argv.size()),
    argv.data(), rcl_get_default_allocator(), &rcl_args);
  rcl_context->global_arguments = rcl_args;
  

/home/arshad/mapped/projects/kinova_arm/kinova_arm_simulation_foxy/install/moveit_ros_move_group/lib/moveit_ros_move_group/move_group --ros-args --log-level info --ros-args -r __ns:=/robot1 --params-file /tmp/launch_params_s9qnom94 --params-file /tmp/launch_params_j0dhvb15 --params-file /tmp/launch_params_kgynuyvu --params-file /tmp/launch_params_nwxr4ll2 --params-file /tmp/launch_params_3y97p0xx --params-file /tmp/launch_params_3tnhgo4l --params-file /tmp/launch_params_4efdls25 --params-file /tmp/launch_params_wqbgcpv_ --params-file /tmp/launch_params_8v2s446w --params-file /tmp/launch_params_r051wyd5 -r /tf:=tf -r /tf_static:=tf_static


ros2 action send_goal /robot1/arm_controller/follow_joint_trajectory  control_msgs/action/FollowJointTrajectory "{ trajectory: { joint_names: [shoulder_pan_joint, shoulder_lift_joint, elbow_joint, wrist_1_joint, wrist_2_joint, wrist_3_joint], points: [ { positions: [2.5, -2.57, 0.0, -1.57, 0.0, 0.0], velocities: [], accelerations: [], time_from_start: { sec: 2, nanosec: 500 } }, ] }, goal_tolerance: [] }"

ros2 action send_goal /robot1/arm_controller/follow_joint_trajectory  control_msgs/action/FollowJointTrajectory "{ trajectory: { joint_names: [shoulder_pan_joint, shoulder_lift_joint, elbow_joint, wrist_1_joint, wrist_2_joint, wrist_3_joint], points: [ { positions: [2.5, -1.57, 0.0, -1.57, 0.0, 0.0], velocities: [], accelerations: [], time_from_start: { sec: 5, nanosec: 500 } }, ] }, goal_tolerance: [ { name: shoulder_pan_joint, position: 0.01 }, { name: shoulder_lift_joint, position: 0.01 }, { name: elbow_joint, position: 0.01 }, { name: wrist_1_joint, position: 0.01 }, { name: wrist_2_joint, position: 0.01 }, { name: wrist_3_joint, position: 0.01 } ] }"

find $PWD -name .git -type d | xargs -i{} dirname {} | xargs -i{} git -C {}  pull origin


ros2 topic pub /robot1/arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "header: 
  stamp: 
    sec: 0
    nanosec: 0
  frame_id: ''
joint_names: ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
points: 
  - 
    positions: [2.5, -2.17, 0.0, -1.57, 0.0, 0.0]
    velocities: []
    accelerations: []
    effort: []
    time_from_start: 
      sec: 0
      nanosec: 0" --once

