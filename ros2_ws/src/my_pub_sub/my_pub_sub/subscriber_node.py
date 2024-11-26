import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray


class NumberSubscriber(Node):
    def __init__(self):
        super().__init__('number_subscriber')
        # Int32MultiArray türünde bir subscription oluştur
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'raw_array_topic',
            self.listener_callback,
            10)
        self.subscription  # Subscription referansını tut

    def listener_callback(self, msg):
        # Gelen diziyi al
        numbers = msg.data
        # Çift sayıların sayısını hesapla
        even_count = sum(1 for number in numbers if number % 2 == 0)
        # Sayıların toplamını ve ortalamasını hesapla
        total = sum(numbers)
        average = total / len(numbers)

        # Çıktıyı yazdır
        self.get_logger().info(
            f'Çift sayı adedi: {even_count} | Toplam: {total} | Ortalama: {average:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = NumberSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

