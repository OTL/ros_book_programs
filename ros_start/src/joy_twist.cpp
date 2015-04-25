#include <ros/ros.h>
#include <sensor_msgs/Joy.h>
#include <geometry_msgs/Twist.h>

class JoyTwist
{
public:
  JoyTwist()
  {
    ros::NodeHandle node;
    joy_sub_ = node.subscribe("joy", 1, &JoyTwist::joyCallback, this);
    twist_pub_ = node.advertise<geometry_msgs::Twist>("cmd_vel", 1);
  }
  
  void joyCallback(const sensor_msgs::Joy &joy_msg)
  {
    if (joy_msg.buttons[0] == 1)
    {
      geometry_msgs::Twist twist;
      twist.linear.x = joy_msg.axes[1] * 0.5;
      twist.angular.z = joy_msg.axes[0] * 1.0;
      twist_pub_.publish(twist);
    }
  }
private:
  ros::Subscriber joy_sub_;
  ros::Publisher twist_pub_;
};

int main(int argc, char **argv) {
  ros::init(argc, argv, "joy_twist");
  JoyTwist joy_twist;
  ros::spin();
}
