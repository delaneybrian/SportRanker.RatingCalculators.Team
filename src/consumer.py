import pika
from Configuration.Constants import MessagingConstants
from dispatcher import Dispatcher
from logger import Logger

class Consumer:

    def __init__(self):
        self.dispatcher = Dispatcher()
        self.logger = Logger()

    def message_callback(self, ch, method, properties, body):
        try:
            self.dispatcher.recieve_message(method.routing_key, body)
        except:
            self.logger.info_log("Exception thrown dispatching message")

    def start_consumer(self):

        params = pika.URLParameters(MessagingConstants.CLOUD_AMPQ_URL)
        params.socket_timeout = 20

        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE, durable=True,
                                 exchange_type='topic')

        result = channel.queue_declare(queue='ratings-processor-team', durable=True)
        queue_name = result.method.queue


        channel.queue_bind(exchange=MessagingConstants.NEW_FIXTURE_EXCHANGE,
                            queue=queue_name,
                            routing_key=MessagingConstants.ALL_RESULTS)

        print(' [*] Waiting for results. To exit press CTRL+C')

        channel.basic_consume(self.message_callback,
                              queue=queue_name,
                              no_ack=True)

        channel.start_consuming()