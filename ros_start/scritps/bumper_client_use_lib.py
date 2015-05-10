#!/usr/bin/env python
import rospy
from ros_start.bumper_client import go_until_bumper
rospy.init_node('bumper_client_use_lib')
go_until_bumper()
