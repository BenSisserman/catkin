#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
  ros::init(argc, argv, "stereo_tf_publisher");
  ros::NodeHandle n;

  ros::Rate r(100);

  tf::TransformBroadcaster bc_left;
  tf::TransformBroadcaster bc_right;
  while(n.ok()){
    bc_left.sendTransform(
		tf::StampedTransform(
			tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.0, 0.15, 0.0)),
			ros::Time::now(),"base_link", "stereo/left"));
	bc_right.sendTransform(
		tf::StampedTransform(
			tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.1, 0.15, 0.0)),
			ros::Time::now(),"base_link", "stereo/left"));
	r.sleep();
  }
}
