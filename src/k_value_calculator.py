import math

from Configuration.Mlb import MlbConstants
from Configuration.Nfl import NflConstsnts
from Configuration.Nhl import NhlConstants
from Configuration.Nba import NbaConstants

class KValueCalculator:

    #Base K Value
    base_k_value = 30

    #K Adjustment Factors
    very_small_k_adjustment_factor = 1.1
    small_k_adjustment_factor = 1.3
    mid_k_adjustment_factor = 1.5
    large_k_adjustment_factor = 1.7
    very_large_k_adjustment_factor = 1.9

    def calculate_k_value(self, sport, homeTeamScore, awayTeamScore):

        sport = sport.upper()

        score_diff = math.fabs(homeTeamScore - awayTeamScore)

        if(sport == "NBA"):
            if(score_diff > NbaConstants.VERY_LARGE_DIFF):
                return self.base_k_value * self.very_large_k_adjustment_factor
            elif(score_diff > NbaConstants.LARGE_DIFF):
                return self.base_k_value * self.large_k_adjustment_factor
            elif(score_diff > NbaConstants.MID_DIFF):
                return self.base_k_value * self.mid_k_adjustment_factor
            elif (score_diff > NbaConstants.VERY_SMALL_DIFF):
                return self.base_k_value * self.small_k_adjustment_factor
            elif(score_diff > NbaConstants.SMALL_DIFF):
                return self.base_k_value * self.very_small_k_adjustment_factor
            else:
                return self.base_k_value

        elif(sport == "NHL"):
            if (score_diff > NhlConstants.VERY_LARGE_DIFF):
                return self.base_k_value * self.very_large_k_adjustment_factor
            elif (score_diff > NhlConstants.LARGE_DIFF):
                return self.base_k_value * self.large_k_adjustment_factor
            elif (score_diff > NhlConstants.MID_DIFF):
                return self.base_k_value * self.mid_k_adjustment_factor
            elif (score_diff > NhlConstants.VERY_SMALL_DIFF):
                return self.base_k_value * self.small_k_adjustment_factor
            elif (score_diff > NhlConstants.SMALL_DIFF):
                return self.base_k_value * self.very_small_k_adjustment_factor
            else:
                return self.base_k_value

        elif(sport == "NFL"):
            if (score_diff > NflConstsnts.VERY_LARGE_DIFF):
                return self.base_k_value * self.very_large_k_adjustment_factor
            elif (score_diff > NflConstsnts.LARGE_DIFF):
                return self.base_k_value * self.large_k_adjustment_factor
            elif (score_diff > NflConstsnts.MID_DIFF):
                return self.base_k_value * self.mid_k_adjustment_factor
            elif (score_diff > NflConstsnts.VERY_SMALL_DIFF):
                return self.base_k_value * self.small_k_adjustment_factor
            elif (score_diff > NflConstsnts.SMALL_DIFF):
                return self.base_k_value * self.very_small_k_adjustment_factor
            else:
                return self.base_k_value

        elif(sport == "MLB"):
            if (score_diff > MlbConstants.VERY_LARGE_DIFF):
                return self.base_k_value * self.very_large_k_adjustment_factor
            elif (score_diff > MlbConstants.LARGE_DIFF):
                return self.base_k_value * self.large_k_adjustment_factor
            elif (score_diff > MlbConstants.MID_DIFF):
                return self.base_k_value * self.mid_k_adjustment_factor
            elif (score_diff > MlbConstants.VERY_SMALL_DIFF):
                return self.base_k_value * self.small_k_adjustment_factor
            elif (score_diff > MlbConstants.SMALL_DIFF):
                return self.base_k_value * self.very_small_k_adjustment_factor
            else:
                return self.base_k_value


        return self.base_k_value
