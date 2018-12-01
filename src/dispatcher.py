from logger import Logger
from Handlers.mlb_fixture_result_handler import MlbFixtureResultHandler
from Handlers.nhl_fixture_result_handler import NhlFixtureResultHandler
from Handlers.nba_fixture_result_handler import NbaFixtureResultHandler
from Handlers.nfl_fixture_result_handler import NflFixtureResultHandler
from Configuration.Constants import MessagingConstants

class Dispatcher:

    def __init__(self):
        self.logger = Logger()
        self.nfl_handler = NflFixtureResultHandler()
        self.nba_handler = NbaFixtureResultHandler()
        self.nhl_handler = NhlFixtureResultHandler()
        self.mlb_handler = MlbFixtureResultHandler()

    def recieve_message(self, routing_key, body):

        split_routing_key = routing_key.split('.')

        if(len(split_routing_key) == 2):
            if(split_routing_key[0] == MessagingConstants.RESULTS
               and split_routing_key[1] == MessagingConstants.NFL):
                self.nfl_handler.handle(body)
            elif(split_routing_key[0] == MessagingConstants.RESULTS
               and split_routing_key[1] == MessagingConstants.NHL):
                self.nhl_handler.handle(body)
            elif (split_routing_key[0] == MessagingConstants.RESULTS
                  and split_routing_key[1] == MessagingConstants.NBA):
                self.nba_handler.handle(body)
            elif (split_routing_key[0] == MessagingConstants.RESULTS
                  and split_routing_key[1] == MessagingConstants.MLB):
                self.mlb_handler.handle(body)
            else:
                self.logger.warning_log("No handler found for message")
        else:
            self.logger.warning_log("Invalid message recived")

