import pygame

def show_settings_menu(screen, logo_image, menu_background_image, prev_button_image):
    pygame.init()
    font = pygame.font.SysFont('comicsansms', 30)
    settings_menu = True
    carrot_count = 200  # Valeur initiale
    rabbit_count = 2    # Valeur initiale

    while settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            clicked = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

            mouse_pos = pygame.mouse.get_pos()

            if clicked:
                if prev_button_rect.collidepoint(mouse_pos):
                    settings_menu = False
                # Ajoutez ici la logique pour régler carrot_count et rabbit_count

        screen.blit(menu_background_image, (0, 0))
        logo_rect = logo_image.get_rect(center=(screen.get_width() // 2, 100))
        screen.blit(logo_image, logo_rect)

        prev_button_rect = prev_button_image.get_rect(topleft=(10, 10))
        screen.blit(prev_button_image, prev_button_rect)

        # Affichez ici les options pour régler carrot_count et rabbit_count

        texts = ["Carrot count:", "Rabbit count:", "Hunter:", "Fox:"]
        y_offset = 200  # Ajustez selon la disposition souhaitée
        for text in texts:
            text_surface = font.render(text, True, (255, 255, 255))  # Blanc
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += 40  # Ajustez l'espacement entre les lignes

        pygame.display.update()

    return carrot_count, rabbit_count