#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
#import RPi.GPIO as GPIO
'''
EN1 = 14
IN1 = 15
IN2 = 18
IN3 = 23
IN4 = 24
EN2 = 25

def motor_init():
    global pwm_L, pwm_R
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EN1, GPIO.OUT)
    GPIO.setup(EN2, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    try:
        pwm_L = GPIO.PWM(EN1, 1000)
        pwm_R = GPIO.PWM(EN2, 1000)
    except:
        pass

def motorStop():
    GPIO.output(EN1, GPIO.LOW)
    GPIO.output(EN2, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def left(vel):
    global pwm_L
    if vel < 0:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        pwm_L.start(0)
        pwm_L.ChangeDutyCycle(-vel)
    else:
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        pwm_L.start(100)
        pwm_L.ChangeDutyCycle(vel)

def right(vel):
    global pwm_R
    if vel < 0:
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        pwm_R.start(0)
        pwm_R.ChangeDutyCycle(-vel)
    else:
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        pwm_R.start(0)
        pwm_R.ChangeDutyCycle(vel)
'''

def onstop():
    print("we are stopping!")

def vel_callback(vel_data):
    vel_l = (vel_data.linear.x - vel_data.angular.z)*100/4
    vel_r = (vel_data.linear.x + vel_data.angular.z)*100/4
    if vel_l > 100:
        vel_l = 100
    elif vel_l < -100:
        vel_l = -100
    if vel_r > 100:
        vel_r = 100
    elif vel_r < -100:
        vel_r = -100
    print(str(vel_l) + ", " + str(vel_r) + '\n')
    rospy.loginfo(str(vel_l)+", "+str(vel_r)+'\n')

def start_node():
    rospy.Subscriber("mercedes/cmd_vel", Twist, vel_callback)
    rospy.init_node('mermer_node')
    rospy.on_shutdown(onstop)
    rospy.spin()

if __name__ == '__main__':
    print("la\nla\nla\n")
    rospy.loginfo("hello???\n?\n?\n?")
    start_node()
