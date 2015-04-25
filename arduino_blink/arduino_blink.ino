#include <ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/String.h>

ros::NodeHandle node;
std_msgs::String chat;
ros::Publisher pub("arduino", &chat);

void ledCallback(const std_msgs::Bool &is_led_on){
  if (is_led_on.data) {
    digitalWrite(13, HIGH);
    chat.data = "led on!";
  } else {
    digitalWrite(13, LOW);
    chat.data = "led off!";
  }
  pub.publish(&chat);
}

ros::Subscriber<std_msgs::Bool> sub("led", &ledCallback);

void setup()
{
  pinMode(13, OUTPUT);
  node.initNode();
  node.subscribe(sub);
  node.advertise(pub);
}

void loop()
{
  node.spinOnce();
  delay(1);
}
