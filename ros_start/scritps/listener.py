#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(topic):
    rospy.loginfo("I heard %s", topic.data)

rospy.init_node('listener')
sub = rospy.Subscriber('chatter', String, callback)
rospy.spin()
