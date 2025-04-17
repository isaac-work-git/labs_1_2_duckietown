#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class TurtleSub:
    def __init__(self):
        self.last_data = ""
        self.started = False
        self.pub_msg = rospy.Publisher('/turtle_dir', String, queue_size=1000)
        rospy.Subscriber("/turtles/turtle1/cmd_vel", Twist, self.callback)
        
        self.dpr = 0.5
        self.rate = rospy.Rate(1 / self.dpr)        
        self.rate_callback()

    def callback(self, data):
        print("New direction received \n")
        self.started, self.last_data
        if (data.linear.x > 0):
            self.last_data = "Right \n"
        elif (data.linear.x < 0):
            self.last_data = "Left \n"
        elif (data.linear.y > 0):
            self.last_data = "Up \n"
        elif (data.linear.y < 0):
            self.last_data = "Down \n"
        if (not self.started):
            self.started = True
        
    def rate_callback(self):
        self.started, self.pub_msg, self.last_data
        while not rospy.is_shutdown():
            if (rospy.has_param("/direction_pub_rate")):
                self.rate = rospy.Rate(1 / rospy.get_param("/direction_pub_rate"))
            if (self.started):
                self.pub_msg.publish(self.last_data)
            rospy.loginfo(self.rate)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.loginfo("Running \n")
    rospy.init_node('turtlesub_node', anonymous=True)
    sub = TurtleSub() 
    rospy.spin()

