#include <ros/ros.h>
#include <tf/transform_broadcaster.h> //tf library for broadcasting
#include <turtlesim/Pose.h>

std::string turtle_name;

void poseCallback(const turtlesim::PoseConstPtr& msg){
  static tf::TransformBroadcaster br; //this is tfb object
  tf::Transform transform; 			  //this is tf object
  transform.setOrigin( tf::Vector3(msg->x, msg->y, 0.0)); //sets origin in 3d using input 
  tf::Quaternion q;										  //whatever a quaternion is q is an object 
  q.setRPY(0, 0, msg->theta); 
  transform.setRotation(q);
  br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "world", turtle_name));
}

int main(int argc, char** argv){
  ros::init(argc, argv, "my_tf_broadcaster");
  if (argc != 2){ROS_ERROR("need turtle name as argument"); return -1;};
  turtle_name = argv[1];

  ros::NodeHandle node;
  ros::Subscriber sub = node.subscribe(turtle_name+"/pose", 10, &poseCallback);

  ros::spin();
  return 0;
};
