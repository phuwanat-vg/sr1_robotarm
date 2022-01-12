#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_control.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from tf.transformations import quaternion_from_euler

 	
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 67, 17))
        self.label_3.setObjectName("label_3")
        self.inX = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inX.setGeometry(QtCore.QRect(90, 20, 104, 31))
        self.inX.setObjectName("inX")
        self.inY = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inY.setGeometry(QtCore.QRect(90, 60, 104, 31))
        self.inY.setObjectName("inY")
        self.inZ = QtWidgets.QTextEdit(self.centralwidget)
        self.inZ.setGeometry(QtCore.QRect(90, 100, 104, 31))
        self.inZ.setObjectName("inZ")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 30, 121, 20))
        self.label_4.setObjectName("label_4")
        self.disp1 = QtWidgets.QLabel(self.centralwidget)
        self.disp1.setGeometry(QtCore.QRect(260, 60, 181, 131))
        self.disp1.setObjectName("disp1")
        self.buttCommand = QtWidgets.QPushButton(self.centralwidget)
        self.buttCommand.setGeometry(QtCore.QRect(60, 150, 141, 51))
        self.buttCommand.setObjectName("buttCommand")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        self.buttCommand.clicked.connect(self.send_command_callback)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "x"))
        self.label_2.setText(_translate("MainWindow", "y"))
        self.label_3.setText(_translate("MainWindow", "z"))
        self.label_4.setText(_translate("MainWindow", "Display monitor"))
        self.disp1.setText(_translate("MainWindow", "Display on this section"))
        self.disp1.setWordWrap(True)
        self.buttCommand.setText(_translate("MainWindow", "Send command"))
        
    
    def send_command_callback(self):
    	x_pos = float(self.inX.toPlainText())
    	y_pos = float(self.inY.toPlainText())
    	z_pos = float(self.inZ.toPlainText())
    	
    	moveit.go_from_pose(x_pos,y_pos,z_pos)
    	#self.disp1.setText(word)

class robotArm(object):
    def __init__(self):
    	moveit_commander.roscpp_initialize(sys.argv)
    	rospy.init_node('move_group_python_gui', anonymous=True)
    	self.robot = moveit_commander.RobotCommander()
    	self.scene = moveit_commander.PlanningSceneInterface()    
    	self.group = moveit_commander.MoveGroupCommander("arm_group")
    	self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', 
    	moveit_msgs.msg.DisplayTrajectory, queue_size = 1)
    	
    def go_from_pose(self,x,y,z):
    	pose_target = geometry_msgs.msg.Pose()
    	roll,pitch,yaw = 0,-45,0
    	q = quaternion_from_euler(roll,pitch,yaw)
    	print(q)
    	pose_target.orientation.x = q[0]
    	pose_target.orientation.y = q[1]
    	pose_target.orientation.z = q[2]
    	pose_target.orientation.w = q[3]
    	pose_target.position.x = x
    	pose_target.position.y = y
    	pose_target.position.z = z
    	self.group.set_goal_orientation_tolerance(3.14)
    	self.group.set_pose_target(pose_target)
    	
    	plan1 = self.group.go()
    	
    	
    	


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    moveit = robotArm()
    
    MainWindow.show()
    sys.exit(app.exec_())

