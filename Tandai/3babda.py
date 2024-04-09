import pygame
import random
import sys

#Pygame window
pygame.init()

pygame.display.set_caption("Chicken invaders")
screen = pygame.display.set_mode((800, 500))

clock = pygame.time.Clock()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False


    pygame.display.flip()
    clock.tick(60)