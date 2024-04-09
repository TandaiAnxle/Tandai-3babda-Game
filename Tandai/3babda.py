import pygame
import random

#Pygame window
pygame.init()

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()