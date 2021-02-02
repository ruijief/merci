#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def joy_callback(joy_data):
    twist = Twist()
    # vertical left stick axis = linear rate
    twist.linear.x = 4*joy_data.axes[1]
    # horizontal left stick axis = turn rate
    twist.angular.z = 4*joy_data.axes[0]
    pub.publish(twist)

# Intializes everything
def start():
    global pub
    pub = rospy.Publisher('mercedes/cmd_vel', Twist)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, joy_callback)
    # starts the node
    rospy.init_node('Joy2vel_node')
    rospy.spin()

if __name__ == '__main__':
    start()
