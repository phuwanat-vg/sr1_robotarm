search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=sr1_3dof_urdf.srdf
robot_name_in_srdf=sr1_3dof_urdf
moveit_config_pkg=sr1_3dof_urdf_moveit_config
robot_name=sr1_3dof_urdf
planning_group_name=arm_group
ikfast_plugin_pkg=sr1_3dof_urdf_arm_group_ikfast_plugin
base_link_name=base_link
eef_link_name=servo_gripper_1
ikfast_output_path=/home/vm20/rb_ws/src/sr1/sr1_3dof_urdf_description/urdf/sr1_3dof_urdf_arm_group_ikfast_plugin/src/sr1_3dof_urdf_arm_group_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path
