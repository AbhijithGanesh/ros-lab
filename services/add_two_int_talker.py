import rospy
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsResponse, AddTwoIntsRequest


def add_two_numbers(req: AddTwoIntsRequest):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return (req.a + req.b)


if __name__ == "__main__":
    rospy.init_node("ros_nodes_add_two_int_talker")
    rospy.Service('/add_two_ints', AddTwoInts, add_two_numbers)
    rospy.spin()
