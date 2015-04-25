#!/usr/bin/env python
import rospy
from ros_start.bumper_client import go_until_bumper
from sensor_msgs.msg import Joy

class JoyBumper(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('joy', Joy, self.joy_callback, queue_size=1)

    def joy_callback(self, joy_msg):
        if joy_msg.buttons[0] == 1:
            go_until_bumper()


if __name__ == '__main__':
    rospy.init_node('joy_bumper')
    joy_bumper = JoyBumper()
    rospy.spin()
