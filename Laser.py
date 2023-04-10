#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
import tf

odom_x = 0


def callback(data):
	global odom_x
	min_distance = .5
	max_distance = 1.5
	in_range = [i for i, dist in enumerate(data.ranges) if dist > min_distance and dist < max_distance and dist!=0]
	rospy.loginfo(in_range) 	

	if len(in_range) > 0:
	   #Use the index of the angle data
	   angles = [data.angle_min + i * data.angle_increment for i in in_range]
	   distances = [data.ranges[i] for i in in_range]
	   rospy.loginfo("robot 2 at angle: %s", str(angles))
	   rospy.loginfo("robot 2 at distance: %s", str(distances))
	   odom_x = .9 - distances[0]
	   odom_publisher()
	   

def laser_scan_subscriber():
	rospy.Subscriber("/scan", LaserScan, callback)

def odom_publisher():
   	    global odom_x
            x = odom_x
            y = 0
            th = 0
	    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
	    odom = Odometry()
	    odom.pose.pose = Pose(Point(float(x), float(y), 0.), Quaternion(*odom_quat)) 
	    # Print the current letter values
	    publisher = rospy.Publisher('/car2/odom', Odometry, queue_size=10)
	    # Wait for a short period of time before checking for changes again
	    publisher.publish(odom)

if __name__ == '__main__':
	rospy.init_node('laser_scan_subscriber')
	laser_scan_subscriber()
	rospy.spin()
	

	 
		
