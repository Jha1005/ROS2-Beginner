#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Import the message type


class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)  # Create a publisher
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)  # Create a timer with a 0.5 second period

    def timer_callback(self):
        self.counter_ += 1
        msg = String()  # Create a new String message
        msg.data = "Pushpanjali " + str(self.counter_)
        self.publisher_.publish(msg)  # Publish the message
        self.get_logger().info(f"Publishing: {msg.data}")  # Log the message


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
