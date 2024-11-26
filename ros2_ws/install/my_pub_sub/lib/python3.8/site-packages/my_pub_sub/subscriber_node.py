import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class NumberSubscriber(Node):
    def __init__(self):
        super().__init__('number_subscriber')
        self.subscription = self.create_subscription(
            String,
            'raw_array_topic',
            self.listener_callback,
            10)
        self.subscription  # Subscription referansını tut

    def listener_callback(self, msg):
        # Mesajı al ve 5 sayıyı liste olarak ayır
        raw_array_topic = list(map(int, msg.data.split(",")))

        # Çift sayıların sayısını hesapla
        even_count = sum(1 for number in raw_array_topic if number % 2 == 0)

        # Sayıların toplamını ve ortalamasını hesapla
        total = sum(raw_array_topic)
        average = total / len(raw_array_topic)

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
