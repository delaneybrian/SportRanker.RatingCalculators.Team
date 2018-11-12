from elo_calculator import EloCalculator
from consumer import Consumer

consumer = Consumer()

consumer.start_consumer()

"""
elo_calculator = EloCalculator()

home_rating, away_rating = elo_calculator.calculate_new_ratings("nfl", 1500, 1800, 30, 30)

print("Home Rating:")
print(home_rating)
print("Away Rating:")
print(away_rating)
"""