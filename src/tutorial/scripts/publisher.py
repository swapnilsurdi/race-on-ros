#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

import math

RATE = 10  # Publishing rate of new data per second
FREQ = 1   # Frequency of the sinusoidal signal


# Execute this when run as a script
if __name__ == '__main__':

    rospy.init_node('publisher')

    pub  = rospy.Publisher('data', Float32, queue_size=1)
    rate = rospy.Rate(RATE)
    step = 0

    while not rospy.is_shutdown():

        # Generate new data point
        value = math.sin(2*math.pi*step/RATE)

        # Log and publish data
        rospy.loginfo("Publishing {:.3f}".format(value))
        pub.publish(value)

        # Advance the sequence
        step = step + 1

        # Wait to match the rate
        rate.sleep()
