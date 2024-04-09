# Example file showing a circle moving on screen
import pygame
<<<<<<< HEAD
=======
import random
import sys
>>>>>>> 84d188d97c6b1bf83a42deb581350d8bd3a4ea4f

# pygame setup
pygame.init()
<<<<<<< HEAD
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
=======

pygame.display.set_caption("Chicken invaders")
screen = pygame.display.set_mode((800, 500))

clock = pygame.time.Clock()
run = True

while run:
>>>>>>> 84d188d97c6b1bf83a42deb581350d8bd3a4ea4f
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()
<<<<<<< HEAD

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
=======
    clock.tick(60)
>>>>>>> 84d188d97c6b1bf83a42deb581350d8bd3a4ea4f
