#!/usr/bin/env python

import rospy
from ros_start.srv import *

def handle_service(req):
    sum = req.a + req.b
    rospy.loginfo("Returning [%s + %s = %s]" % (req.a, req.b, sum))
    return AddTwoIntsResponse(sum)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_service)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

