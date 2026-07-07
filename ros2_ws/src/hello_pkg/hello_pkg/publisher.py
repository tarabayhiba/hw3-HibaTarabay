# rclpy is the client library that connects this process to the ROS2 graph (nodes, topics, discovery)
import rclpy
# node is the base class every ROS2 node inherits from; it gives access to pub/sub/timer/logging APIs
from rclpy.node import Node
# std_msgs/String is the message type carried on the topic, publisher & subscriber must agree on it
from std_msgs.msg import String


class HelloPublisher(Node):

    def __init__(self):
        # registers this node with the ROS2 graph under the name 'hello_publisher'
        super().__init__('hello_publisher')

        # declares this node as a publisher on 'hello_topic'; 10 is the QoS queue depth for buffered messages
        # Qos queue depth is the nb of msgs that can be buffered before sending
        # if the queue is full, older messages are dropped
        self.pub_ = self.create_publisher(String, 'hello_topic', 10)
        # a ROS2 timer drives periodic work
        # it fires timer_callback once/sec on the node's executor
        # node's executor is a thread that runs callbacks for timers/subscriptions/services/etc.. in the node
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        # self.count=0 bc we want to keep track of how many msgs have been published to be included in the msg data
        self.count_ = 0 

    def timer_callback(self):
        # messages are data objects matching the topic's type, filled in before sending
        msg = String()
        msg.data = f"Hello World: {self.count_}"

        # publish() hands the message to ROS2's middleware (DDS), which delivers it to any current subscribers
        self.pub_.publish(msg)

        # get_logger() ties log output to this node's name/namespace, distinguishing it in multi-node systems
        self.get_logger().info(f"Publishing: {msg.data}")

        self.count_ += 1


def main(args=None):
    # initializes the ROS2 client library for this process 
    # this must happen before any node is created
    rclpy.init(args=args)
    node = HelloPublisher()

    # spin() blocks main thread & hands control to the executor which triggers timers/callbacks as events occur
    # runs forever until process is interrupted (ctrl+c)
    rclpy.spin(node)

    # cleans up node resources once spinning stops example on shutdown/interrupt
    node.destroy_node()
    # shuts down the ROS2 context for this process releasing middleware resources
    rclpy.shutdown()