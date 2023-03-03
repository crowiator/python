# importujeme pygame
import pygame
# Inicializace pygame
pygame.init()
# Vytvoření obrazovky
screen = pygame.display.set_mode((600, 400))
# Hlavní herní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

# Ukončení pygame
pygame.quit()
