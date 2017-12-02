#include <ros/ros.h>
#include <geometry_msgs/Twist.h>	//twist msg to publish to turtle
#include <sensor_msgs/Joy.h>		//joy msg to listen to


class TeleopTurtle
{
public:
  TeleopTurtle();

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy); //creates callback function that will take a joy msg

  ros::NodeHandle nh;	//nh object always needed in roscpp

  int linear, angular;
  double l_scale, a_scale;
  ros::Publisher vel_pub;	//publishes commands
  ros::Subscriber joy_sub;	//subscribes to joy

};

TeleopTurtle::TeleopTurtle():linear(1),angular(2){

	nh.param("axis_linear", linear, linear);
	nh.param("axis_angular", angular, angular);
	nh.param("scale_angular", a_scale, a_scale);
	nh.param("scale_linear", l_scale, a_scale);

	vel_pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel",1); //publishes twist commands to topic cmd_vel
	joy_sub = nh.subscribe<sensor_msgs::Joy>("joy", 10, &TeleopTurtle::joyCallback, this); //subscribes to topic joy and calls callback with stack of 10 commands
}

void TeleopTurtle::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)	//def of callback
{
  geometry_msgs::Twist twist;											//initialze twist variable
  twist.angular.z = a_scale*joy->axes[angular];						
  twist.linear.x = l_scale*joy->axes[linear];	
  vel_pub.publish(twist);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "turtle_joy_node");
  TeleopTurtle turtle_joy;

  ros::spin();
}


