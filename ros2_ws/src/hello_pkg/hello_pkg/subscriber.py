import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloSubscriber(Node):

    def __init__(self):
        # registers this node with the ROS2 graph under the name 'hello_subscriber'
        super().__init__('hello_subscriber')

        # subscribes to 'hello_topic'; ROS2 discovery matches this to any publisher on the same topic/type
        # with no direct reference between the two nodes needed
        # this happens automatically via the ROS2 graph & DDS discovery
        # dds recovery is the process of finding other nodes in the ROS2 graph that are publishing/subscribing to the same topic
        self.sub_ = self.create_subscription(
            String,
            'hello_topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        # invoked asynchronously by the executor whenever a new message arrives on the topic
        self.get_logger().info(f"Received: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = HelloSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()