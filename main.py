import pygame
import random
import matplotlib.pyplot as plt

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
        self.last_mate = None
        self.last_reproduction_week = None  # Keep track of the last reproduction week

    def age_one_week(self):
        self.age += 1 / self.WEEKS_PER_YEAR

    def eat(self, garden):
        if garden.has_carrots():
            garden.consume_carrot()
            self.has_eaten = True
            self.weeks_without_food = 0
        else:
            self.has_eaten = False
            self.weeks_without_food += 1

    def can_reproduce(self):
        return self.age >= 1 and self.last_reproduction_week != self.current_week // self.WEEKS_PER_YEAR

    def is_dead(self):
        max_age = self.MAX_UNDER_FEED_AGE if not self.has_eaten else self.MAX_HEALTHY_AGE
        if self.age > max_age or self.weeks_without_food > 2:
            return True
        return False

# Carrot Class
class Carrot:
    def __init__(self, count):
        self.count = count

    def harvest(self, additional_count):
        self.count += additional_count

    def consume(self):
        if self.count > 0:
            self.count -= 1
            return True
        return False

# Garden Class
class Garden:
    WEEKS_PER_YEAR = 52
    MARCH_PLANTING_WEEK = 9  # March starts at the 9th week of the year
    JUNE_HARVEST_WEEK = 22  # June starts at the 22nd week of the year

    def __init__(self):
        self.rabbits = [Rabbit(Gender.MALE), Rabbit(Gender.FEMALE)]
        self.carrots = Carrot(200)
        self.current_week = 0
        self.birth_weeks = [12, 24]
        self.litter_size_range = (1, 6)
        self.reproduction_allowed = True

    def has_carrots(self):
        return self.carrots.count > 0

    def consume_carrot(self):
        return self.carrots.consume()

    def weekly_update(self):
        self.current_week += 1

        # Manage carrots in March and June
        current_year = self.current_week // self.WEEKS_PER_YEAR
        week_of_year = self.current_week % self.WEEKS_PER_YEAR

        if week_of_year == self.MARCH_PLANTING_WEEK and not hasattr(self, 'last_planting_year'):
            self.carrots.harvest(200)
            self.last_planting_year = current_year

        if week_of_year == self.MARCH_PLANTING_WEEK and current_year != self.last_planting_year:
            self.carrots.harvest(200)
            self.last_planting_year = current_year

        if week_of_year == 31:  # First week of August
            self.carrots.count = max(0, self.carrots.count - 200)  # Don't go below 0

        # Allow reproduction in April and July
        self.reproduction_allowed = week_of_year in range(14, 18) or week_of_year in range(27, 31)

        for rabbit in self.rabbits:
            rabbit.age_one_week()
            rabbit.eat(self)
            if rabbit.is_dead():
                self.rabbits.remove(rabbit)

        self.handle_reproduction()

    def handle_reproduction(self):
        reproduction_weeks = list(range(14)) + list(range(27))

        if self.current_week % self.WEEKS_PER_YEAR in reproduction_weeks:
            potential_mothers = [rabbit for rabbit in self.rabbits if rabbit.can_reproduce()]
            for mother in potential_mothers:
                fathers = [rabbit for rabbit in self.rabbits if rabbit.gender == Gender.MALE and rabbit.can_reproduce()]
                if fathers:
                    father = random.choice(fathers)
                    litter_size = random.randint(1, 6)
                    for _ in range(litter_size):
                        self.rabbits.append(Rabbit(gender=random.choice([Gender.MALE, Gender.FEMALE])))
                    mother.last_reproduction_week = self.current_week // self.WEEKS_PER_YEAR
                    father.last_reproduction_week = self.current_week // self.WEEKS_PER_YEAR

# Pygame initialization and other configurations...
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rabbit Garden")

background_image = pygame.image.load('img/garden.png')
background_image = pygame.transform.scale(background_image, window_size)

rabbit_image = pygame.image.load('img/rabbit.png')
rabbit_image = pygame.transform.scale(rabbit_image, (int(rabbit_image.get_width() * 0.1), int(rabbit_image.get_height() * 0.1)))

carrot_image = pygame.image.load('img/carrot.png')
carrot_image = pygame.transform.scale(carrot_image, (20, 20))

margin = 0.07
margin_x = int(window_size[0] * margin)
margin_y = int(window_size[1] * margin)

garden = Garden()

weeks = []
rabbit_counts = []
carrot_counts = []

# Main loop for the simulation over 6 years
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    # Display carrots
    for i in range(garden.carrots.count):
        pos_x = random.randint(margin_x, window_size[0] - margin_x - carrot_image.get_width())
        pos_y = random.randint(margin_y, window_size[1] - margin_y - carrot_image.get_height())
        pos = (pos_x, pos_y)
        screen.blit(carrot_image, pos)

    # Display rabbits
    for rabbit in garden.rabbits:
        pos_x = random.randint(margin_x, window_size[0] - margin_x - rabbit_image.get_width())
        pos_y = random.randint(margin_y, window_size[1] - margin_y - rabbit_image.get_height())
        pos = (pos_x, pos_y)
        if rabbit.gender == Gender.MALE:
            rabbit_image_flipped = pygame.transform.flip(rabbit_image, True, False)
            screen.blit(rabbit_image_flipped, pos)
        else:
            screen.blit(rabbit_image, pos)

    pygame.display.flip()

    garden.weekly_update()

    weeks.append(garden.current_week)
    rabbit_counts.append(len(garden.rabbits))
    carrot_counts.append(garden.carrots.count)

    pygame.time.delay(500)

# Display graphs with matplotlib
plt.figure(figsize=(10, 6))
plt.plot(weeks, rabbit_counts, label='Rabbits')
plt.plot(weeks, carrot_counts, label='Carrots')
plt.xlabel('Weeks')
plt.ylabel('Count')
plt.title('Evolution of the rabbit and carrot garden')
plt.legend()
plt.show()

pygame.quit()
