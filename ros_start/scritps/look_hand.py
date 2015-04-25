#!/usr/bin/env python
import rospy
import tf2_ros
from ez_utils.ez_joints import JointsServer

if __name__ == '__main__':
    rospy.init_node('pr2_look_left_hand')
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    head = JointsServer('/head_traj_controller')
    left_arm = JointsServer('/l_arm_controller')
    yaw_angle = 0.0
    pitch_angle = 0.0
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tf_buffer.lookup_transform('head_plate_frame',
                                               'l_gripper_led_frame',
                                               rospy.Time())
            yaw_angle = trans.transform.translation.y / 1.0
            pitch_angle = -trans.transform.translation.z / 1.0
            print trans.transform.translation
            head.set_positions([yaw_angle, pitch_angle])
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, 
                tf2_ros.ExtrapolationException):
            rospy.logwarn('tf not found')
        rate.sleep()
