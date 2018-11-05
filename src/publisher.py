import pika
from Configuration.Constants import MessagingConstants

class Publisher:

    def publish(self, message, routing_key):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=MessagingConstants.HOST))

        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE,
                                 exchange_type='topic')

        channel.basic_publish(exchange='topic_logs',
                              routing_key=routing_key,
                              body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        connection.close()