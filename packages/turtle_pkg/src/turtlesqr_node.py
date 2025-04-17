#!/usr/bin/python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def turtle_right(pub, duration):
  cmd = Twist()
  cmd.linear.x = 3 
  pub.publish(cmd)
  rospy.sleep(duration) 
  turtle_stop(pub) 

def turtle_left(pub, duration):
  cmd = Twist()
  cmd.linear.x = -3  
  pub.publish(cmd)
  rospy.sleep(duration) 
  turtle_stop(pub)
  
def turtle_up(pub, duration):
  cmd = Twist()
  cmd.linear.y = 3  
  pub.publish(cmd)
  rospy.sleep(duration) 
  turtle_stop(pub)

def turtle_down(pub, duration):
  cmd = Twist()
  cmd.linear.y = -3  
  pub.publish(cmd)
  rospy.sleep(duration) 
  turtle_stop(pub)

def turtle_stop(pub):
  cmd = Twist()
  pub.publish(cmd)

def turtlesqr_node():
  pub_vel = rospy.Publisher('/turtles/turtle1/cmd_vel', Twist, queue_size=10)
  rospy.init_node('turtlesqr_node', anonymous=True)
  
  move_duration = 1.5
  while True:
    turtle_right(pub_vel, move_duration)
    turtle_up(pub_vel, move_duration)
    turtle_left(pub_vel, move_duration)
    turtle_down(pub_vel, move_duration)

if __name__ == '__main__':
    try:
        turtlesqr_node()
    except rospy.ROSInterruptException:
        pass
