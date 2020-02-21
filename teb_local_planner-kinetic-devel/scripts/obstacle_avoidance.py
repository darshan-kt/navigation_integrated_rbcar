
#! /usr/bin/env python
 
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
 

def main():
    global pub
    print "hi"
    rospy.init_node('reading_laser')    
    pub = rospy.Publisher('/move_base/cmd_vel', Twist, queue_size=1)    
    sub = rospy.Subscriber('/front_laser/scan', LaserScan, clbk_laser)    
    rospy.spin()

def clbk_laser(msg):
    regions = {
        # 'right':  min(min(msg.ranges[0:143]), 3),
        # 'fright': min(min(msg.ranges[144:287]), 3),
        'front':  min(min(msg.ranges[355:365]), 0.3),
        # 'fleft':  min(min(msg.ranges[432:575]), 3),
        # 'left':   min(min(msg.ranges[576:713]), 3),
        }
    
    msg=Twist()
    msg.angular.z = 0.3
    pub.publish(msg)
    print "published"
    
    
    
if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except rospy.ROSInterruptException: pass
    
    
    # take_action(regions)


# def take_action(regions):
#     msg = Twist()
#     linear_x = 0
#     angular_z = 0
    
#     # state_description = ''
    
#     # if regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] > 1:
#     #     state_description = 'case 1 - nothing'
#     #     linear_x = 0.6
#     #     angular_z = 0
#     # elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] > 1:
#     #     state_description = 'case 2 - front'
#     #     linear_x = 0
#     #     angular_z = 0.3
#     # elif regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
#     #     state_description = 'case 3 - fright'
#     #     linear_x = 0
#     #     angular_z = 0.3
#     # elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
#     #     state_description = 'case 4 - fleft'
#     #     linear_x = 0
#     #     angular_z = -0.3
#     # elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
#     #     state_description = 'case 5 - front and fright'
#     #     linear_x = 0
#     #     angular_z = 0.3
#     # elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
#     #     state_description = 'case 6 - front and fleft'
#     #     linear_x = 0
#     #     angular_z = -0.3
#     if regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
#         state_description = 'case 7 - front and fleft and fright'
#         linear_x = 0
#         angular_z = 0.3
#     # elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
#     #     state_description = 'case 8 - fleft and fright'
#     #     linear_x = 0.3
#     #     angular_z = 0
#     else:
#         state_description = 'unknown case'
#         rospy.loginfo(regions)
        
#     ROS_INFO("Hi")
 
#     rospy.loginfo(state_description)
#     msg.linear.x = -linear_x
#     msg.angular.z = angular_z
#     pub.publish(msg)