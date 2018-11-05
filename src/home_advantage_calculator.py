from Configuration.Mlb import MlbConstants
from Configuration.Nfl import NflConstsnts
from Configuration.Nhl import NhlConstants
from Configuration.Nba import NbaConstants


class HomeAdvantageCalculator:

    def calculate_home_advantage(self, sport):

        sport = sport.upper()

        if(sport == "MLB"):
            return MlbConstants.HomeAdvantage
        elif(sport == "NHL"):
            return NhlConstants.HomeAdvantage
        elif(sport == "NBA"):
            return NbaConstants.HomeAdvantage
        elif(sport == "NFL"):
            return NflConstsnts.HomeAdvantage