import logging
from animals import Rabbit, Carrot
import random
from datetime import datetime, timedelta

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Garden:
    def __init__(self):
        self.rabbits = [Rabbit('male'), Rabbit('female')]
        self.carrots = [Carrot() for _ in range(200)]
        self.current_date = datetime(2023, 1, 1)  # Starting date
        self.rabbit_count = []
        self.carrot_count = []
        self.reproduction_count = []

    def harvest_carrot(self):
        if self.carrots:
            self.carrots.pop()
            return True
        return False

    def weekly_update(self):
        self.current_date += timedelta(weeks=1)
        logging.info(f"Weekly update for {self.current_date.strftime('%Y-%m-%d')}")

        # Aging and eating
        for rabbit in self.rabbits:
            rabbit.age_one_week()
            rabbit.eat(self)

        # Handle reproduction
        reproduction_events = self.handle_reproduction()
        self.reproduction_count.append(reproduction_events)

        # Remove dead rabbits
        self.rabbits = [rabbit for rabbit in self.rabbits if not rabbit.is_dead()]

        # Handle carrot growth
        self.handle_carrot_growth()

        # Collect data
        self.rabbit_count.append(len(self.rabbits))
        self.carrot_count.append(len(self.carrots))

    def handle_reproduction(self):
        potential_mothers = [rabbit for rabbit in self.rabbits if rabbit.can_reproduce(self.current_date)]
        reproduction_count = 0
        for mother in potential_mothers:
            father = random.choice(
                [rabbit for rabbit in self.rabbits if rabbit.gender == 'male' and rabbit != mother.last_mate])
            if father:
                litter_size = random.randint(1, 6)
                for _ in range(litter_size):
                    self.rabbits.append(Rabbit(gender=random.choice(['male', 'female'])))
                mother.last_mate = father
                reproduction_count += 1
        if reproduction_count > 0:
            logging.info(f"{reproduction_count} reproduction events occurred.")
        return reproduction_count

    def handle_carrot_growth(self):
        if self.current_date.month == 3:  # Sowing in March
            self.carrots = [Carrot() for _ in range(200)]
            logging.info("Carrots sown.")
        elif self.current_date.month == 6:  # Harvest in June
            self.carrots = []
            logging.info("Carrots harvested.")

    def __str__(self):
        return f"Garden on {self.current_date.strftime('%Y-%m-%d')} with {len(self.rabbits)} rabbits and {len(self.carrots)} carrots"

    def get_rabbit_positions(self):
        # Cette fonction doit retourner une liste de tuples (x, y) pour chaque lapin
        # Par exemple, retourner une liste de positions aléatoires ou basées sur certaines règles
        return [(random.randint(0, 800), random.randint(0, 600)) for _ in self.rabbits]

    def get_carrot_positions(self):
        # Même principe pour les carottes
        return [(random.randint(0, 800), random.randint(0, 600)) for _ in self.carrots]
