from elo_calculator import EloCalculator
from logger import Logger
from Configuration.Constants import MessagingConstants
from Configuration.Constants import ResultConstants
from Configuration.Constants import DataConstants
from Configuration.Constants import RankingChangeConstants
from Configuration.Constants import SportId
from Configuration.Constants import RankingChangeType
from data_provider import DataProvider
from publisher import Publisher
import json

class NflFixtureResultHandler:

    def __init__(self):
        self.logger = Logger()
        self.elo_calculator = EloCalculator()
        self.data_provider = DataProvider()
        self.publisher = Publisher()

    def handle(self, message):
        self.logger.log("NFL handler fixture result received")

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

        home_new_rating, away_new_rating = self.elo_calculator.calculate_new_ratings(MessagingConstants.NFL,
                                                 home_team_rating, away_team_rating, home_team_score, away_team_score)

        home_rating_change_message = {
            RankingChangeConstants.SPORT_ID: SportId.NBA,
            RankingChangeConstants.TEAM_ID: home_team_id,
            RankingChangeConstants.RANKING: home_new_rating,
            RankingChangeConstants.RANKING_CHANGE_TYPE: RankingChangeType.TEAM
        }

        home_ranking_json = json.dumps(home_rating_change_message)

        self.logger.log(home_ranking_json)

        away_rating_change_message = {
            RankingChangeConstants.SPORT_ID: SportId.NBA,
            RankingChangeConstants.TEAM_ID: away_team_id,
            RankingChangeConstants.RANKING: away_new_rating,
            RankingChangeConstants.RANKING_CHANGE_TYPE: RankingChangeType.TEAM
        }

        away_ranking_json = json.dumps(away_rating_change_message)

        self.logger.log(away_ranking_json)

        self.publisher.publish(home_ranking_json, MessagingConstants.TEAM_RATING_CHANGE)

        self.publisher.publish(away_ranking_json, MessagingConstants.TEAM_RATING_CHANGE)