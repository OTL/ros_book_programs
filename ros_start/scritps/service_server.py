#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
from std_srvs.srv import EmptyResponse

def handle_service(req):
    rospy.loginfo('called!')
    return EmptyResponse()

def service_server():
    rospy.init_node('service_server')
    s = rospy.Service('call_me', Empty, handle_service)
    print "Ready to serve."
    rospy.spin()

if __name__ == "__main__":
    service_server()
