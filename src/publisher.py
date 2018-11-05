import pika
from Configuration.Constants import MessagingConstants

class Publisher:

    def publish(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=MessagingConstants.HOST))

        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE,
                                 exchange_type='topic')

        routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

        message = ' '.join(sys.argv[2:]) or 'Hello World!'

        channel.basic_publish(exchange='topic_logs',
                              routing_key=routing_key,
                              body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        connection.close()