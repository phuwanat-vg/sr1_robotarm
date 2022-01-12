#! /usr/bin/env python3
import sys
import copy
import rospy
import moveit_commander
from moveit_msgs.msg import RobotState
from moveit_msgs.srv import GetPositionFK, GetPositionFKRequest
from std_msgs.msg import Header
from sensor_msgs.msg import JointState

moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('get_fk', anonymous=True)

arm = moveit_commander.MoveGroupCommander('arm_group')
robot = moveit_commander.RobotCommander()

rospy.wait_for_service('compute_fk')

try:
  moveit_fk = rospy.ServiceProxy('compute_fk', GetPositionFK)
except rospy.ServiceException:
  rospy.logerror("Service call failed: %s"%e)

rqst = GetPositionFKRequest()
rqst.header.frame_id = "base_link"
rqst.fk_link_names = ["Pointer_v2_1"]
rqst.robot_state = robot.get_current_state()

res = moveit_fk(rqst)
rospy.loginfo(["FK LOOKUP:", res]) # Print EE Pose
