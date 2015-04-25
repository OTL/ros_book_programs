#!/usr/bin/env python
import rospy
from ros_start.bumper_action import BumperAction

if __name__ == '__main__':
    rospy.init_node('bumper_action_use_lib')
    bumper_action = BumperAction()
    rospy.spin()
