# garden.py
import random
from animals import Rabbit, Gender

# Carrot Class
class Carrot:
    def __init__(self, count):
        self.count = count

    def consume(self):
        """ Consumes a carrot, if available. """
        if self.count > 0:
            self.count -= 1
            return True
        return False

    def harvest(self, additional_count):
        """ Adds carrots to the garden. """
        self.count += additional_count

# Garden Class
class Garden:
    WEEKS_PER_YEAR = 52

    def __init__(self):
        self.rabbits = [Rabbit(Gender.MALE), Rabbit(Gender.FEMALE)]
        self.carrots = Carrot(200)
        self.current_week = 9
        self.last_planting_year = 0

    def has_carrots(self):
        """ Checks if there are any carrots in the garden. """
        return self.carrots.count > 0

    def consume_carrot(self):
        """ Consumes a carrot from the garden. """
        return self.carrots.consume()

    def weekly_update(self):
        """ Updates the garden status every week. """
        self.current_week += 1
        current_year = self.current_week // self.WEEKS_PER_YEAR
        week_of_year = self.current_week % self.WEEKS_PER_YEAR

        # Planting and harvesting logic
        if week_of_year == 9 and current_year != self.last_planting_year:
            self.carrots.harvest(200)
            self.last_planting_year = current_year

        if week_of_year == 22:
            self.carrots.harvest(200)

        rabbit_population = len(self.rabbits)
        epidemic_risk = 0.05

        # Update each rabbit in the garden
        for rabbit in list(self.rabbits):
            rabbit.age_one_week()
            rabbit.eat(self)
            if rabbit.is_dead(epidemic_risk, self.current_week, rabbit_population):
                self.rabbits.remove(rabbit)

        self.handle_reproduction()

    def handle_reproduction(self):
        """ Handles the reproduction of rabbits in the garden. """
        week_of_year = self.current_week % self.WEEKS_PER_YEAR
        if week_of_year in range(14, 18) or week_of_year in range(27, 31):
            potential_mothers = [rabbit for rabbit in self.rabbits if rabbit.can_reproduce(self.current_week)]
            for mother in potential_mothers:
                fathers = [rabbit for rabbit in self.rabbits if rabbit.gender == Gender.MALE and rabbit.can_reproduce(self.current_week)]
                if fathers:
                    father = random.choice(fathers)
                    litter_size = random.randint(1, 6)
                    for _ in range(litter_size):
                        self.rabbits.append(Rabbit(gender=random.choice([Gender.MALE, Gender.FEMALE])))
                    mother.last_reproduction_week = self.current_week // self.WEEKS_PER_YEAR
                    father.last_reproduction_week = self.current_week // self.WEEKS_PER_YEAR
