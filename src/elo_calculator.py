from k_value_calculator import KValueCalculator
from home_advantage_calculator import HomeAdvantageCalculator
import math

class EloCalculator:

    win_outcome = 1
    lose_outcome = 0
    draw_outcome = 0.5

    def __init__(self):
        self.k_value_calculator = KValueCalculator()
        self.home_adv_calculator = HomeAdvantageCalculator()

    def calculate_new_ratings(self, sport, home_orignal_rating, away_orignal_rating, home_score, away_score):

        k_value = self.k_value_calculator.calculate_k_value(sport, home_score, away_score)

        home_team_adv = self.home_adv_calculator.calculate_home_advantage(sport)

        #remove ht adv
        diff_in_ratings = math.fabs((home_orignal_rating) - away_orignal_rating)

        expected_result = self.calculate_win_expectency(diff_in_ratings)

        if(home_score > away_score):
            home_new_rating = self.calculate_new_rating(self.win_outcome, expected_result, k_value, home_orignal_rating)
            away_new_rating = self.calculate_new_rating(self.lose_outcome, expected_result, k_value, away_orignal_rating)
            return home_new_rating, away_new_rating
        elif(home_score < away_score):
            home_new_rating = self.calculate_new_rating(self.lose_outcome, expected_result, k_value, home_orignal_rating)
            away_new_rating = self.calculate_new_rating(self.win_outcome, expected_result, k_value, away_orignal_rating)
            return home_new_rating, away_new_rating
        else:
            home_new_rating = self.calculate_new_rating(self.draw_outcome, expected_result, k_value, home_orignal_rating)
            away_new_rating = self.calculate_new_rating(self.draw_outcome, expected_result, k_value, away_orignal_rating)
            return home_new_rating, away_new_rating

    def calculate_new_rating(self, result, expected_result, k_value, orignal_rating):
        return orignal_rating + (k_value * (expected_result - result))

    def calculate_win_expectency(self, difference_in_ratings):

        power = -1 * (difference_in_ratings / 400)

        return 1 / (math.pow(10, power) + 1)

