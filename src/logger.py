import logging

class Logger:

    def __init__(self):
        logging.basicConfig(filename=r"C:\Code\SportRanker\Logs\logs.txt", level=logging.INFO)

    def debug_log(self, message):
        logging.debug(message)
        print(message)

    def info_log(self, message):
        logging.info(message)
        print(message)

    def warning_log(self, message):
        logging.warning(message)
        print(message)

