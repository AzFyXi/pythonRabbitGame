# main.py
import pygame.mixer
import pygame
import matplotlib.pyplot as plt
from garden import Garden
from animals import Gender
import random
import time

# Pygame initialization and other configurations
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rabbit Garden")

def fade_in_out(image, screen, duration, stay_time):
    """ Fades an image in and out on the screen. """
    fade_in_duration = fade_out_duration = duration / 2
    start_time = time.time()
    image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Fade in
        if elapsed_time < fade_in_duration:
            alpha = (elapsed_time / fade_in_duration) * 255
        # Stay visible
        elif elapsed_time < fade_in_duration + stay_time:
            alpha = 255
        # Fade out
        elif elapsed_time < fade_in_duration + stay_time + fade_out_duration:
            alpha = 255 - ((elapsed_time - fade_in_duration - stay_time) / fade_out_duration) * 255
        else:
            break

        image.set_alpha(alpha)
        screen.fill((0, 0, 0))
        screen.blit(image, image_rect)
        pygame.display.update()

loading_image = pygame.image.load('img/loading.png')
desired_width = 900
desired_height = 700
loading_image = pygame.transform.scale(loading_image, (desired_width, desired_height))
# Display the loading screen with fade in and out
fade_duration = 1.0  # Duration for fade in and fade out
stay_duration = 2.0  # Duration for the image to stay visible
fade_in_out(loading_image, screen, fade_duration, stay_duration)

background_image = pygame.image.load('img/garden.png')
background_image = pygame.transform.scale(background_image, window_size)

rabbit_image = pygame.image.load('img/rabbit.png')
rabbit_image = pygame.transform.scale(rabbit_image, (int(rabbit_image.get_width() * 0.1), int(rabbit_image.get_height() * 0.1)))

carrot_image = pygame.image.load('img/carrot.png')
carrot_image = pygame.transform.scale(carrot_image, (20, 20))

margin = 0.07
margin_x = int(window_size[0] * margin)
margin_y = int(window_size[1] * margin)

# Assuming Garden, Gender, and other classes are defined in other modules
from garden import Garden
from animals import Gender

garden = Garden(window_size, margin_x, margin_y)

weeks = []
rabbit_counts = []
carrot_counts = []
total_months = 0

pygame.mixer.music.load('music/musique.mp3')
pygame.mixer.music.play(-1)

# Main loop for the simulation over 6 years
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    # Display carrots and rabbits
    for pos in garden.carrots.positions:
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

    rabbit_count = len(garden.rabbits)
    carrot_count = garden.carrots.count 
    font = pygame.font.Font(None, 36)
    rabbit_text = font.render(f'Lapins: {rabbit_count}', True, (255, 255, 255))
    carrot_text = font.render(f'Carottes: {carrot_count}', True, (255, 255, 255))

    rabbit_text_position = (window_size[0] - rabbit_text.get_width() - 10, 10)
    carrot_text_position = (window_size[0] - carrot_text.get_width() - 10, 10 + rabbit_text.get_height())

    months = total_months + (garden.current_week // 4)  # Assuming 4 weeks per month
    month_text = font.render(f'Mois: {months}', True, (255, 255, 255))
    month_text_position = (window_size[0] - month_text.get_width() - 10, 10 + rabbit_text.get_height() + carrot_text.get_height())

    screen.blit(rabbit_text, rabbit_text_position)
    screen.blit(carrot_text, carrot_text_position)
    screen.blit(month_text, month_text_position)

    pygame.display.flip()

    garden.weekly_update()

    pygame.time.delay(100)

    weeks.append(garden.current_week)
    rabbit_counts.append(len(garden.rabbits))
    carrot_counts.append(garden.carrots.count)

# Data visualization with Matplotlib
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(weeks, rabbit_counts, label='Rabbits')
plt.plot(weeks, carrot_counts, label='Carrots')
plt.xlabel('Weeks')
plt.ylabel('Count')
plt.title('Evolution of the Rabbit and Carrot Garden')
plt.legend()
plt.show()

pygame.quit()