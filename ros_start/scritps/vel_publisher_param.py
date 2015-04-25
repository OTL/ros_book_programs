#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('vel_publisher')
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
vel_x = rospy.get_param('~vel_x', 0.5)
vel_rot = rospy.get_param('~vel_rot', 1.0)

while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input('f: forward, b: backward, l: left, r: right > ')
    if 'f' in direction:
        vel.linear.x = vel_x
    if 'b' in direction:
        vel.linear.x = -vel_x
    if 'l' in direction:
        vel.angular.z = vel_rot
    if 'r' in direction:
        vel.angular.z = -vel_rot
    if 'q' in direction:
        break
    print(vel)
    r = rospy.Rate(10.0)
    for i in range(10):
        pub.publish(vel)
        r.sleep()
