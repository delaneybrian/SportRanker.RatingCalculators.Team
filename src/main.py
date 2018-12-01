from consumer import Consumer
from logger import Logger

consumer = Consumer()
logger = Logger()

while(True):
    try:
        logger.info_log("Starting Message Consumer..")
        consumer.start_consumer()
    except:
        logger.warning_log("Error Running Consumer. Restarting...")
