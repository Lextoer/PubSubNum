import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(String, 'raw_array_topic', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)  # 2 saniyede bir yayın yap

    def timer_callback(self):
        # 1-1000 arasında rastgele 5 tamsayı seç
        raw_array_topic = [random.randint(1, 1000) for _ in range(5)]
        message = ",".join(map(str, raw_array_topic))  # Sayıları virgülle birleştir
        self.publisher_.publish(String(data=message))
        self.get_logger().info(f'Yayınlanan sayılar: {message}')


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
