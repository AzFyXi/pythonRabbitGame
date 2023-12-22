import pygame
import matplotlib.pyplot as plt
from garden import Garden
from animals import Gender
from settings_menu import show_settings_menu
import random
import time

# Pygame initialization and other configurations
pygame.init()

window_size = (1024, 576)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Rabbit Garden")

logo_image = pygame.image.load('img/logo.png')
logo_image = pygame.transform.scale(logo_image, (300, 300))

def fade_in_out(image, logo, screen, duration, stay_time):
    """ Fades an image and a logo in and out on the screen. """
    fade_in_duration = fade_out_duration = duration / 2
    start_time = time.time()
    image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    logo_rect = logo.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Calcul de l'alpha pour le fondu
        if elapsed_time < fade_in_duration:
            alpha = (elapsed_time / fade_in_duration) * 255
        elif elapsed_time < fade_in_duration + stay_time:
            alpha = 255
        elif elapsed_time < fade_in_duration + stay_time + fade_out_duration:
            alpha = 255 - ((elapsed_time - fade_in_duration - stay_time) / fade_out_duration) * 255
        else:
            break

        image.set_alpha(alpha)
        logo.set_alpha(alpha)  # Applique le même alpha au logo
        screen.fill((0, 0, 0))
        screen.blit(image, image_rect)
        screen.blit(logo, logo_rect)
        pygame.display.update()

# Loading and displaying the loading screen
loading_image = pygame.image.load('img/loading.png')
desired_width = 1024
desired_height = 576
loading_image = pygame.transform.scale(loading_image, (desired_width, desired_height))
fade_duration = 1.0  # Duration for fade in and fade out
stay_duration = 1.0  # Duration for the image to stay visible
fade_in_out(loading_image, logo_image, screen, fade_duration, stay_duration)

# Chargement des images pour le menu
menu_background_image = pygame.image.load('img/menuBackground.png')
menu_background_image = pygame.transform.scale(menu_background_image, window_size)
logo_image = pygame.image.load('img/logo.png')
logo_image = pygame.transform.scale(logo_image, (200, 200))

play_button_image = pygame.image.load('img/play.png')
setting_button_image = pygame.image.load('img/setting.png')
exit_button_image = pygame.image.load('img/exit.png')
prev_button_image = pygame.image.load('img/prev.png')

def show_menu():
    menu = True
    while menu:
        clicked = False  # Définir 'clicked' à chaque itération de la boucle principale

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
                mouse_pos = pygame.mouse.get_pos()

                # Actions des boutons
                if play_button_rect.collidepoint(mouse_pos):
                    menu = False  # Quitter le menu et lancer la partie
                elif setting_button_rect.collidepoint(mouse_pos):
                    show_settings_menu(screen, logo_image, menu_background_image, prev_button_image)
                    # Ouvrir le menu des options
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

        screen.blit(menu_background_image, (0, 0))
        logo_rect = logo_image.get_rect(center=(window_size[0] // 2, 100))
        screen.blit(logo_image, logo_rect)

        # Positionnement des boutons en ligne
        button_y_position = 300
        play_button_rect = play_button_image.get_rect(center=(window_size[0] // 2 - 150, button_y_position))
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
                mouse_pos = pygame.mouse.get_pos()

                # Actions des boutons
                if play_button_rect.collidepoint(mouse_pos):
                    menu = False  # Quitter le menu et lancer la partie
                elif setting_button_rect.collidepoint(mouse_pos):
                    show_settings_menu(screen, logo_image, menu_background_image, prev_button_image)
                    # Ouvrir le menu des options
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

        screen.blit(menu_background_image, (0, 0))
        logo_rect = logo_image.get_rect(center=(window_size[0] // 2, 100))
        screen.blit(logo_image, logo_rect)

        # Positionnement des boutons en ligne
        button_y_position = 300
        play_button_rect = play_button_image.get_rect(center=(window_size[0] // 2 - 150, button_y_position))
        setting_button_rect = setting_button_image.get_rect(center=(window_size[0] // 2, button_y_position))
        exit_button_rect = exit_button_image.get_rect(center=(window_size[0] // 2 + 150, button_y_position))

        screen.blit(play_button_image, play_button_rect)
        screen.blit(setting_button_image, setting_button_rect)
        screen.blit(exit_button_image, exit_button_rect)

        clicked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True

        mouse_pos = pygame.mouse.get_pos()

        # Actions des boutons
        
        if play_button_rect.collidepoint(mouse_pos) and clicked:
            menu = False  # Quitter le menu et lancer la partie
        if setting_button_rect.collidepoint(mouse_pos) and clicked:
            show_settings_menu(screen, logo_image, menu_background_image, prev_button_image)
            # Ouvrir le menu des options
            pass
        elif exit_button_rect.collidepoint(mouse_pos) and clicked:
            pygame.quit()
            quit()

        pygame.display.update()

show_menu()

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

plt.figure(figsize=(10, 6))
plt.plot(weeks, rabbit_counts, label='Rabbits')
plt.plot(weeks, carrot_counts, label='Carrots')
plt.xlabel('Weeks')
plt.ylabel('Count')
plt.title('Evolution of the Rabbit and Carrot Garden')
plt.legend()
plt.show()

pygame.quit()
