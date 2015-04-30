#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import struct

file = open( "/dev/input/mice", "rb" );

def getMouseEvent():
  buf = file.read(3);
  button = ord( buf[0] );
  bLeft = button & 0x1;
  bMiddle = ( button & 0x4 ) > 0;
  bRight = ( button & 0x2 ) > 0;
  x,y = struct.unpack( "bb", buf[1:] );
  return ("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft,bMiddle,bRight, x, y) );

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = getMouseEvent()
        #rospy.loginfo(str)
        print str
        pub.publish(str)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass