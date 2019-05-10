import logging
import os

class Logger:

    def __init__(self):
        if not os.path.exists('teams.txt'):
            with open('teams.txt', 'w'): pass
        logging.basicConfig(filename=r"teams.txt", level=logging.INFO)

    def debug_log(self, message):
        logging.debug(message)
        print(message)

    def info_log(self, message):
        logging.info(message)
        print(message)

    def warning_log(self, message):
        logging.warning(message)
        print(message)

