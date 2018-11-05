import pika
from Configuration.Constants import MessagingConstants
from logger import Logger

class Publisher:

    def __init__(self):
        self.logger = Logger()

    def publish(self, message, routing_key):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=MessagingConstants.HOST))

        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE,
                                 exchange_type='topic')

        channel.basic_publish(exchange='topic_logs',
                              routing_key=routing_key,
                              body=message)
        self.logger.log(" [x] Sent %r:%r" % (routing_key, message))
        connection.close()