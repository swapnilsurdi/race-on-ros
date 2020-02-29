#!/usr/bin/env python
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import rospy
from std_msgs.msg import Float32
global counter

# Automatically called by ROS when new message is received
def callback(msg):
    rospy.loginfo("Received {:.3f}".format(msg.data))
    if counter % 10 == 0:
        plt.plot(msg.data, '*')
        plt.axis("equal")
        plt.draw()
        plt.pause(0.00000000001)

	
	
# Execute this when run as a script
if __name__ == '__main__':
    counter = 0
    # Init the node and subscribe for data
    rospy.init_node("subscriber")
    rospy.Subscriber("data", Float32, callback)
    plt.ion()
    plt.show()

    # Prevents python from exiting until this node is stopped
    rospy.spin()
