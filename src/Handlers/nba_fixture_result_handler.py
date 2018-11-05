from elo_calculator import EloCalculator
from logger import Logger
from Configuration.Constants import MessagingConstants
from Configuration.Constants import ResultConstants
from Configuration.Constants import DataConstants
from data_provider import DataProvider
from publisher import Publisher
import json

class NbaFixtureResultHandler:

    def __init__(self):
        self.logger = Logger()
        self.elo_calculator = EloCalculator()
        self.data_provider = DataProvider()
        self.publisher = Publisher()

    def handle(self, message):
        self.logger.log("NBA handler fixture result recieved")

        message = message.decode(MessagingConstants.ENCODING)

        message_dict = json.loads(message)

        feed_source_id = message_dict[ResultConstants.FEED_SOURCE]

        home_team_feed_id = message_dict[ResultConstants.HOME_TEAM_ID]
        away_team_feed_id = message_dict[ResultConstants.AWAY_TEAM_ID]

        home_team_details = self.data_provider.get_team_details_by_feed_id(feed_source_id, home_team_feed_id)
        away_team_details = self.data_provider.get_team_details_by_feed_id(feed_source_id, away_team_feed_id)

        home_team_id = home_team_details[DataConstants.TEAM_ID]
        home_team_rating = away_team_details[DataConstants.RATING]

        away_team_id = home_team_details[DataConstants.TEAM_ID]
        away_team_rating = away_team_details[DataConstants.RATING]

        home_team_score = message_dict[ResultConstants.HOME_TEAM_SCORE]
        away_team_score = message_dict[ResultConstants.AWAY_TEAM_SCORE]

        home_new_rating, away_new_rating = self.elo_calculator.calculate_new_ratings(MessagingConstants.NBA,
                                                 home_team_rating, away_team_rating, home_team_score, away_team_score)

        rating_change_message = "test_message"

        self.publisher.publish(rating_change_message, MessagingConstants.TEAM_RATING_CHANGE)