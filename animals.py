import logging
from datetime import datetime

class Rabbit:
    __MAX_UNDER_FEED_AGE = 4
    __MAX_HEALTH_AGE = 6
    __WEEKS_PER_YEAR = 52

    def __init__(self, gender, age=0):
        self.gender = gender
        self.age = age
        self.has_eaten = True  # Rabbits start well-fed
        self.last_mate = None  # Track the last mate to avoid immediate re-mating

    def age_one_week(self):
        self.age += 1 / self.__WEEKS_PER_YEAR  # Age in years

    def eat(self, garden):
        self.has_eaten = garden.harvest_carrot()

    def can_reproduce(self, current_date):
        return self.age >= 1 and self.gender == 'female' and current_date.month in [4, 7]

    def is_dead(self):
        max_age = self.__MAX_UNDER_FEED_AGE if not self.has_eaten else self.__MAX_HEALTH_AGE
        is_dead = self.age > max_age or (not self.has_eaten and self.age > 2 / self.__WEEKS_PER_YEAR)
        if is_dead:
            logging.info(f"A rabbit died on {datetime.now().strftime('%Y-%m-%d')}.")
        return is_dead


class Carrot:
    def __init__(self):
        pass  # Carrots have no specific attributes for now
