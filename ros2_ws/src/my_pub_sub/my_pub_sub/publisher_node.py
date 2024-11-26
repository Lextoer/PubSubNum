import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random


class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        # Int32MultiArray türünde bir publisher oluştur
        self.publisher_ = self.create_publisher(Int32MultiArray, 'raw_array_topic', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)  # 2 saniyede bir yayın yap

    def timer_callback(self):
        # 1-1000 arasında rastgele 5 tamsayı seç
        raw_array = [random.randint(1, 1000) for _ in range(5)]
        # Int32MultiArray mesajını hazırla
        message = Int32MultiArray()
        message.data = raw_array
        # Mesajı yayınla
        self.publisher_.publish(message)
        self.get_logger().info(f'Yayınlanan sayılar: {raw_array}')


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

