#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm_group")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', 
	moveit_msgs.msg.DisplayTrajectory,queue_size=1)

pose_target = geometry_msgs.msg.Pose()

pose_target.orientation.x = 0.041
pose_target.orientation.y = 0.805
pose_target.orientation.z = -0.030
pose_target.orientation.w = 0.592

pose_target.position.x = 0.094
pose_target.position.y = -0.014
pose_target.position.z = 0.092
group.set_pose_target(pose_target)

plan1 = group.go()

rospy.sleep(5)
moveit_commander.roscpp_shutdown()
