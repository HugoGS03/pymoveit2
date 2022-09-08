import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci
from control_msgs.action import FollowJointTrajectory

class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        #self._action_client = ActionClient(self, Fibonacci, 'fibonacci/series')
        self._action_client = ActionClient(self, action_type=FollowJointTrajectory, action_name='arm_controller/follow_joint_trajectory')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order
        print("WAITING1")
        self._action_client.wait_for_server()
        print("Service running")
        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    future = action_client.send_goal(10)

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()
