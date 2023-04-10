#!/usr/bin/env python
from pickle import TRUE
import time
import random
from cmath import sqrt
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist

x1 =0.0 
x2 =0.0 
y1=0.0
y2=0.0
z1=0.0
z2 =0.0

theta1 = 1
theta2 = 1
theta3 = 1
theta4 = 1
beta = 0.5
r12 = 1

vel1 = 2
vel2 = 2

robot1_pos = Point(0,0,0)
robot2_pos = Point(0,0,0)
Coillision_Intersection_pos = Point(1.3,0,0)
Safety_Intersection_pos = Point(1.6,0,0)
#Ts_pos= Point(2,0,0)
#Tc_pos= Point(1.7,0,0)
Max_pos = Point(2,0,0)

class Cmd_Publisher():
    def __init__(self, rate):
        self.car1pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
	
    # publishes to the first car's cmd_vel topic
        self.stop_cmd = Twist()
        self.stop_cmd.linear.x = 0.0
        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.3
        self.done = False

        # Set timeout to None if rate is 0 (causes new_message to wait forever
        # for new data to publish)
        if rate != 0.0:
            self.timeout = 1.0 / rate
        else:
            self.timeout = None


# define the callback function for the odom topic
def car1_odom_callback(data):
    global x1 ,y1 , z1 
    x1= data.pose.pose.position.x
    y1= data.pose.pose.position.y
    z1= data.pose.pose.position.z


def car2_odom_callback(data):
    global x2 ,y2 , z2 
    x2= data.pose.pose.position.x
    y2= data.pose.pose.position.y
    z2= data.pose.pose.position.z
    rospy.loginfo("Received odom data2: x=%f, y=%f, z=%f", 
                  x2, y2, z2)
def Robot_movement ():

            publisher = Cmd_Publisher(1)
    
            #travel_dist1 = sqrt((x1*x1)+(y1*y1)) # calculate distance from odom 
            #travel_dist2 = sqrt((x2*x2)+(y2*y2))

            robot_current_pos1 = Point(x1,0,0)
            robot_current_pos2 = Point(x2,0,0)
            # Distance from collision point or the intersection point
           # distance_1 = Intersection_pos - robot_current_pos1 #  refers to the distance from the collision point
           # distance_2 = Intersection_pos - robot_current_pos2
            xColIntersection_Pos =Coillision_Intersection_pos.x
            xSafIntersection_Pos = Safety_Intersection_pos.x
            xrobot_current_pos1 = robot_current_pos1.x
            xrobot_current_pos2 = robot_current_pos2.x
            
            xdistance_Tc1 =  xColIntersection_Pos - xrobot_current_pos1 #  refers to the distance from the collision point
            xdistance_Ts1 =  xSafIntersection_Pos - xrobot_current_pos1
            
            xdistance_Tc2 =  xColIntersection_Pos - xrobot_current_pos2 #  refers to the distance from the collision point
            xdistance_Ts2 =  xSafIntersection_Pos - xrobot_current_pos2
            
            #xdistance_1 = distance_1.x  #only extracting the x coordinate from the point 
            #xdistance_2 = distance_2.x

            print("distance of car 1 collision point is ", xdistance_Tc2)
            print("distance of car 1 safety point is ", xdistance_Ts2)
            
            print("distance of car 2 collision point is ", xdistance_Tc2)
            print("distance of car 2 safety point is ", xdistance_Ts2)
            
            #make a code here that starts the car going forward initially

         
          
            print("velocity", publisher.move_cmd)
                        
            while xrobot_current_pos1 < Max_pos.x:

            # Calculate time to collision and time to safely cross intersection
                Tc2 = (xdistance_Tc2/vel2) # Time to collision 2->1
                Ts2 = (xdistance_Ts2/vel2) # Time to safely cross intersection 

                Tc1 = (xdistance_Tc1/vel1) # Time to collision 2->1
                Ts1 = (xdistance_Ts2/vel1) # Time to safely cross intersection ego1
            # Calculate acceleration values
                a12 = beta*(theta1*Ts1-Tc2+theta2) # Stop
                a22 = beta*(Tc2-theta3*Ts1+theta4)+(1-beta)*r12 # Forward

                # Make decision based on acceleration values
		
                if a12 > a22: # Car 1 needs to stop
                     publisher = Cmd_Publisher(1)
		     publisher.car1pub.publish(publisher.stop_cmd)
                     # subscribe to the second car's odom topic
                     print("Car 1 stopped!")
                   # if distance_2 = Intersection_pos:
                    # publisher.car1pub.publish('[.5.0, 0.0, 0.0]' '[0.0,0.0,0.0]')
                     #if distance_2 >= Intersection_pos:
                     # publisher.car1pub.publish('[2.0, 0.0, 0.0]' '[0.0,0.0,0.0]')
                else:
		    # Car 1 keeps moving forward
                    #publisher.car1pub.publish('[4.0, 0.0, 0.0]', '[0.0,0.0,0.0]')
                    publisher = Cmd_Publisher(1)
		    publisher.car1pub.publish(publisher.move_cmd)
                    print("Car 1 moving forward")

                # Wait for 1 second before checking again
                time.sleep(.2)
                
if __name__ == '__main__':
    # initialize the node
    rospy.init_node('GTRobot')
    
    # specify the ROS master URIs of the two cars
    rospy.set_param('limo_base_nodeCar1_uri', 'http://<10.0.0.3>:11311')
    rospy.set_param('limo_base_node_uri', 'http://<10.0.0.4>:11311')

     # subscribe to the first car's odom topic
    car1_odom_subscriber = rospy.Subscriber('/odom', Odometry, car1_odom_callback)
    
    # subscribe to the second car's odom topic
    car2_odom_subscriber = rospy.Subscriber('/car2/odom', Odometry, car2_odom_callback)

    Robot_movement() # Call the function to start the simulation
    
    # spin the node to keep it running
    rospy.spin()
