import re
import time
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
import tf

# Open the text file for reading
file_path = 'odom_data_.txt'
file = open(file_path, 'r')

# Define the letter and associated number pattern to extract from the text
#letter_pattern = """
#pose: 
#  position: 
#    x: r'[-+]?(\d*\.\d+|\d+(\.\d*)?)([eE][-+]?/d+)?'
#    y: r'[-+]?(\d*\.\d+|\d+(\.\d*)?)([eE][-+]?/d+)?'
#    z: r'[-+]?(\d*\.\d+|\d+(\.\d*)?)([eE][-+]?/d+)?'

#"""

# Create a dictionary to store the current value of each letter
letter_values = {}

# Monitor the file for changes and update the letter values
while True:
    # Read the new content of the file
    new_content = file.read()


    matches = re.findall(r"position:\s*\n\s*x:\s*([-+]?\d*\.\d+)\s*\n\s*y:\s*([-+]?\d*\.\d+)", new_content)

    #Extract the letter and associated number from each match
    for letter, number in matches:
            x = letter
            y = number
            th = 0
	    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
	    odom = Odometry()
	    odom.pose.pose = Pose(Point(float(x), float(y), 0.), Quaternion(*odom_quat)) 
	    rospy.init_node('odom_publisher')
	    # Print the current letter values
	    publisher = rospy.Publisher('car2/odom', Odometry, queue_size=10)
	    # Wait for a short period of time before checking for changes again
	    publisher.publish(odom)
            
