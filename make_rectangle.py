#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    # Initialize the ROS node
    rospy.init_node('move_turtle_node', anonymous=True)
    
    # Create a publisher to send velocity commands to the turtle
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Define the rate at which the loop will run (10 Hz)
    rate = rospy.Rate(10)
    
    # Create a Twist message to set linear and angular velocity
    vel_msg = Twist()
    
    # Define the side length of the rectangle (change as needed)
    side_length = 2.0  # meters
    
    # Define the duration for moving in a straight line to cover the side of the rectangle
    move_duration = side_length / 1.0  # velocity is set to 1.0 m/s for simplicity
    
    # Define the time for turning 90 degrees
    turn_duration = 1.5  # time to turn 90 degrees, adjust if needed
    
    # Move in a rectangle (4 sides)
    for _ in range(4):
        # Move straight
        vel_msg.linear.x = 1.0  # move forward at 1 m/s
        vel_msg.angular.z = 0.0  # no rotation
        rospy.loginfo("Moving straight")
        
        # Move for the defined duration
        start_time = rospy.Time.now()
        while rospy.Time.now() - start_time < rospy.Duration(move_duration):
            velocity_publisher.publish(vel_msg)
            rate.sleep()
        
        # Stop before turning (optional, for smoother motion)
        vel_msg.linear.x = 0.0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        
        # Turn 90 degrees
        vel_msg.linear.x = 0.0  # stop moving forward
        vel_msg.angular.z = 0.9  # set angular velocity for 90 degree turn (1.57 rad = 90 degrees)
        rospy.loginfo("Turning ")
        
        # Turn for the defined duration
        start_time = rospy.Time.now()
        while rospy.Time.now() - start_time < rospy.Duration(turn_duration):
            velocity_publisher.publish(vel_msg)
            rate.sleep()
        
        # Stop turning before moving to the next side
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)

    rospy.loginfo("Completed rectangle movement")

if __name__ == '__main__':
    try:
        # Call the function to move the turtle
        move_turtle()
    except rospy.ROSInterruptException:
        pass
