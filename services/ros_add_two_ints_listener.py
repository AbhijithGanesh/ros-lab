import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == "__main__":
    rospy.init_node("ros_nodes_add_two_int_listener")
    rospy.wait_for_service('/add_two_ints')

    try:
        add_two_ints = rospy.ServiceProxy('/add_two_ints', AddTwoInts)
        result = add_two_ints(10, 100)
        rospy.logwarn("Sum is going to be: %s", result)
    except rospy.ServiceException as e:
        rospy.logerr("Something broke")
