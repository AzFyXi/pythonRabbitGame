# animals.py

import random

# Enumeration for genders
class Gender:
    MALE = "male"
    FEMALE = "female"

# Rabbit Class
class Rabbit:
    MAX_UNDER_FEED_AGE = 4
    MAX_HEALTHY_AGE = 6
    WEEKS_PER_YEAR = 52

    def __init__(self, gender):
        self.gender = gender
        self.age = 0
        self.has_eaten = True
        self.weeks_without_food = 0
        self.last_reproduction_week = None

    def age_one_week(self):
        """ Ages the rabbit by one week. """
        self.age += 1 / self.WEEKS_PER_YEAR

    def eat(self, garden):
        """ Rabbit attempts to eat a carrot from the garden. """
        if garden.has_carrots():
            garden.consume_carrot()
            self.has_eaten = True
            self.weeks_without_food = 0
        else:
            self.has_eaten = False
            self.weeks_without_food += 1

    def can_reproduce(self, current_week):
        """ Checks if the rabbit can reproduce. """
        return self.age >= 1 and self.last_reproduction_week != current_week // self.WEEKS_PER_YEAR

    def is_sick(self, epidemic_risk, rabbit_population):
        """ Determines if the rabbit gets sick based on various factors. """
        base_disease_probability = 0.06
        age_factor = (self.age / self.MAX_HEALTHY_AGE) ** 2
        population_factor = rabbit_population / 15
        return random.random() < (base_disease_probability + epidemic_risk * population_factor) * age_factor

    def is_dead(self, epidemic_risk=0, current_week=None, rabbit_population=0):
        """ Determines if the rabbit is dead based on age, hunger, and disease. """
        if self.age > self.MAX_UNDER_FEED_AGE or self.weeks_without_food > 2:
            return True
        if current_week is not None and current_week <= 12 and self.last_reproduction_week is None:
            return False
        return self.is_sick(epidemic_risk, rabbit_population)

# Fox Class
class Fox:
    def __init__(self, image):
        self.image = image
        self.hunger = 0  # Fox hunger level, increases over time

    def hunt(self, rabbits):
        # Implement fox hunting behavior here
        # Can eat a maximum of 1 rabbit per month
        pass

# Hunter Class
class Hunter:
    def __init__(self, image):
        self.image = image
        self.ammunition = 5  # Starting ammunition for hunter

    def hunt(self, foxes):
        # Implement hunter's action here
        # Can kill a fox every 3 months
        pass