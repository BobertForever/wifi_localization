#!/usr/bin/env python

import roslib; roslib.load_manifest('wifi_lookup')
import rospy, pickle
from wifi_lookup.msg import WifiData, Wifi

#1st goal, Completed, load database from other node
#2nd goal, Create publisher framework for pose messages
#3rd goal, perform 2-D lookup and set comprehension to create location
dbLoc = "database.pk"

#create proper handler function to append new hotspots to data object

#deserialize the object and do ROS things
def make():
	global database
	try:
		dbFile = open(dbLoc)
		database = pickle.load(dbFile)
		dbFile.close()
	except: 
		database = {}

#Add publisher ROS things
if __name__=='__main__':
	rospy.init_node('wifi_publisher')
	try:
		make()
	except rospy.ROSInterruptException: pass
