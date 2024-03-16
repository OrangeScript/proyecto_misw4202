import pika


class RabbitMQ:
    def __init__(self, host, queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.queue_name = queue_name
        self.messages = []

    def send_message(self, message, queue_name):
        self.channel.basic_publish(exchange="", routing_key=queue_name, body=message)
        print(" [x] Sent %r" % message)

    def close_connection(self):
        self.connection.close()
