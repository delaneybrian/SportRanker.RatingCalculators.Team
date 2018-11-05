import pika

from Configuration.Constants import MessagingConstants
from dispatcher import Dispatcher

class Consumer:

    def __init__(self):
        self.dispatcher = Dispatcher()

    def message_callback(self, ch, method, properties, body):
        self.dispatcher.recieve_message(method.routing_key, body)

    def start_consumer(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=MessagingConstants.HOST))
        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE,
                                 exchange_type='topic')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue


        channel.queue_bind(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE,
                            queue=queue_name,
                            routing_key=MessagingConstants.ALL_RESULTS)

        print(' [*] Waiting for results. To exit press CTRL+C')

        channel.basic_consume(self.message_callback,
                              queue=queue_name,
                              no_ack=True)

        channel.start_consuming()