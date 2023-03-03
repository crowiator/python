import pygame

#Inicializacia
pygame.init()

#Obrazovka
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

#Hlavny cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue= False

#Ukoncenie
pygame.quit()