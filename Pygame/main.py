import pygame

#Inicializacia pygame
pygame.init()

#Vytvorenie obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

#farby
black =

#hlavny herny cyklus
lets_continue = "True"
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue= False




#ukoncenie hry
pygame.quit()

