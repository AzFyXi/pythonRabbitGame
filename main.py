# main.py

import pygame
import matplotlib.pyplot as plt
from garden import Garden
from animals import Gender
import random

# Pygame initialization and other configurations
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

    # Display carrots and rabbits
    for i in range(garden.carrots.count):
        pos_x = random.randint(margin_x, window_size[0] - margin_x - carrot_image.get_width())
        pos_y = random.randint(margin_y, window_size[1] - margin_y - carrot_image.get_height())
        pos = (pos_x, pos_y)
        screen.blit(carrot_image, pos)

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

    pygame.time.delay(100)

    # Data collection for Matplotlib
    weeks.append(garden.current_week)
    rabbit_counts.append(len(garden.rabbits))
    carrot_counts.append(garden.carrots.count)

# Data visualization with Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(weeks, rabbit_counts, label='Rabbits')
plt.plot(weeks, carrot_counts, label='Carrots')
plt.xlabel('Weeks')
plt.ylabel('Count')
plt.title('Evolution of the Rabbit and Carrot Garden')
plt.legend()
plt.show()

pygame.quit()
