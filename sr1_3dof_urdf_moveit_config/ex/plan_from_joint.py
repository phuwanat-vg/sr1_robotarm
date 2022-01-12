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
	moveit_msgs.msg.DisplayTrajectory,queue_size = 1)

def d2r(deg):
	rad = deg/180*3.14159
	return rad

group_variable_values = group.get_current_joint_values()

group_variable_values[0] = d2r(-46)
group_variable_values[1] = d2r(-36)
group_variable_values[2] = d2r(77)


group.set_joint_value_target(group_variable_values)

plan1 = group.go()

rospy.sleep(5)
