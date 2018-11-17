
class RankingChangeType:
    UNSET = 0,
    TEAM = 1,
    STATE = 2,
    CITY = 3

class DataConstants:
    TEAM_ID = 'teamId'
    RATING = 'rating'

class SportId:
    UNSET = 0,
    NBA = 1,
    NFL = 2,
    NHL = 3,
    MLB = 4,
    NASCAR = 5

class SourceId:
    UNSET = 0,
    SPORT_RADAR = 1,
    INTERNAL = 2

class ResultConstants:
    KICK_OFF_TIME_UTC = 'KickOffTimeUtc'
    SOURCE = 'Source'
    SOURCE_ID = 'SourceId'
    SPORT_ID = 'SportId'
    FEED_SOURCE = 'Source'
    HOME_TEAM_ID = 'HomeTeamId'
    HOME_TEAM_NAME = 'HomeTeamName'
    HOME_TEAM_SCORE = 'HomeTeamScore'
    AWAY_TEAM_ID = 'AwayTeamId'
    AWAY_TEAM_NAME = 'AwayTeamName'
    AWAY_TEAM_SCORE = 'AwayTeamScore'

class RankingChangeConstants:
    SPORT_ID = 'SportId'
    TEAM_ID = 'TeamId'
    RANKING = 'Ranking'
    RANKING_CHANGE_TYPE = 'RankingChangeType'

class MessagingConstants:
    ENCODING = 'utf-8'

    CLOUD_AMPQ_URL = r'amqp://lhqadfns:Ox1Z9RVKMsu36ZjbLV0HEzknWsgJi36S@raven.rmq.cloudamqp.com/lhqadfns'
    HOST = 'localhost'
    PORT = ''

    NEW_FIXTURE_EXCHANGE = 'new_fixture_exchange'
    NBA_RESULTS = 'results.nba'
    NFL_RESULTS = 'results.nfl'
    NHL_RESULTS = 'results.nhl'
    MLB_RESULTS = 'results.mlb'
    ALL_RESULTS = 'results.*'

    RESULTS = 'results'
    NBA = 'nba'
    NFL = 'nfl'
    NHL = 'nhl'
    MLB = 'mlb'



    RATING_CHANGE_EXCHANGE = 'rating_change_exchange'
    TEAM_RATING_CHANGE = 'ratings.team'
    LOCATION_RATING_CHANGE = 'ratings.location'
    ALL_RATINGS_CHANGE = 'ratings.*'