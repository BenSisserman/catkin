#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <ar_track_alvar_msgs/AlvarMarkers.h>
#include <geometry_msgs/PoseStamped.h>

class ARTurtle
{
public:
  ARTurtle();

private:
  void ARCallback(const ar_track_alvar_msgs::AlvarMarkers::ConstPtr& ar); //creates callback function that will take a joy msg

  ros::NodeHandle nh;	//nh object always needed in roscpp

  int linear, angular;
  double l_scale, a_scale;
  ros::Publisher vel_pub;	//publishes commands
  ros::Subscriber ar_sub;	//subscribes to ar_pose

};

ARTurtle::ARTurtle():linear(1),angular(2){

	nh.param("axis_linear", linear, linear);
	nh.param("axis_angular", angular, angular);
	nh.param("scale_angular", a_scale, a_scale);
	nh.param("scale_linear", l_scale, a_scale);

	vel_pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel",1); //publishes twist commands to topic cmd_vel
	ar_sub = nh.subscribe<ar_track_alvar_msgs::AlvarMarkers>("ar_pose_marker", 10, &ARTurtle::ARCallback, this); 
}


void ARTurtle::ARCallback(const ar_track_alvar_msgs::AlvarMarkers::ConstPtr& ar)	//def of callback
{
	geometry_msgs::Twist twist;											//initialze twist variable
	twist.angular.z = a_scale*ar->markers[0].pose.pose.position.x;				
	twist.linear.x = l_scale*ar->markers[0].pose.pose.position.y;
	vel_pub.publish(twist);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "turtle_ar_node");
  ARTurtle turtle_ar;

  ros::spin();
}
