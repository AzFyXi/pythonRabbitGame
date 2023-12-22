# settings_menu.py
import pygame

def show_settings_menu(screen, logo_image, menu_background_image, prev_button_image):
    pygame.init()
    font = pygame.font.SysFont('comicsansms', 30)

    # Chargement des images on/off
    on_image = pygame.image.load('img/on.png')
    off_image = pygame.image.load('img/off.png')

    # États initiaux pour Hunter et Fox
    hunter_enabled = False
    fox_enabled = False

    settings_menu = True

    while settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Initialiser 'clicked' au début de chaque itération
            clicked = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

            mouse_pos = pygame.mouse.get_pos()

            if clicked:
                # Gérer les clics sur les images on/off
                # Assurez-vous que hunter_button_rect et fox_button_rect sont définis
                if hunter_button_rect.collidepoint(mouse_pos):
                    hunter_enabled = not hunter_enabled
                if fox_button_rect.collidepoint(mouse_pos):
                    fox_enabled = not fox_enabled

        screen.blit(menu_background_image, (0, 0))
        logo_rect = logo_image.get_rect(center=(screen.get_width() // 2, 100))
        screen.blit(logo_image, logo_rect)

        prev_button_rect = prev_button_image.get_rect(topleft=(10, 10))
        screen.blit(prev_button_image, prev_button_rect)

        # Affichage des textes et des boutons on/off
        texts_left = ["Carrot count:", "Rabbit count:"]
        texts_right = ["Hunter:", "Fox:"]
        y_offset_left = 200
        y_offset_right = 200

        # Afficher les textes à gauche
        for text in texts_left:
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(left=50, top=y_offset_left)
            screen.blit(text_surface, text_rect)
            y_offset_left += 40

        # Afficher les textes et boutons on/off à droite
        for text in texts_right:
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(left=screen.get_width() // 2, top=y_offset_right)
            screen.blit(text_surface, text_rect)

            image = on_image if (text == "Hunter:" and hunter_enabled) or (text == "Fox:" and fox_enabled) else off_image
            image_rect = image.get_rect(left=screen.get_width() // 2 + 150, top=y_offset_right)
            screen.blit(image, image_rect)

            if clicked and image_rect.collidepoint(mouse_pos):
                if text == "Hunter:":
                    hunter_enabled = not hunter_enabled
                else:  # "Fox:"
                    fox_enabled = not fox_enabled

            y_offset_right += 40

        pygame.display.update()
    
    # Retourner les paramètres ajustés
    return hunter_enabled, fox_enabled
