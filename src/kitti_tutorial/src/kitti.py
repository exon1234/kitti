import rospy
from sensor_msg


if __name__ == '__main__':
    rospy.init_node("talker",anonymous=True)
    pub = rospy.Publisher("chat",String,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown()