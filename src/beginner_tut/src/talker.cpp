#include <ros/ros.h>
#include "std_msgs/String.h"
#include <sstream>

//library for string, messages, and ros

int main(int argc, char **argv){

	ros::init(argc, argv, "talker_node");
	//initializes node with name talker_node
	ros::NodeHandle nh;
	//creates a node handler that allows interaction with ros

	ros::Publisher pub = nh.advertise<std_msgs::String>("chatter",1000);
	ros::Rate r(10);
	//sets the rate of ros loop

	while(ros::ok()){
		std_msgs::String msg;
		std::stringstream ss;
		ss << "Hello World From C++";
		msg.data = ss.str();
		ROS_INFO("%s", msg.data.c_str());
		pub.publish(msg);
		ros::spinOnce();
		r.sleep();
	}

return 0;
}

