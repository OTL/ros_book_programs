#!/usr/bin/env python

import sys
import rospy
from ros_start.srv import *

def call_service(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        response = add_two_ints(x, y)
        return response.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print "Requesting %s+%s" % (x, y)
    sum = call_service(x, y)
    print "%s + %s = %s" % (x, y, sum)
