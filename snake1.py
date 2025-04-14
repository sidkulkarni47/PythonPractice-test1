import pygame, sys
from pygame.locals import *

pygame.init()
WINDOW_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)

snake_color = (255, 255, 255)
snake_pos = (300, 200)
snake_size = (10, 10)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# Code for updating the position of the snake here

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, snake_color, (snake_pos, snake_size))
        pygame.display.update()
        clock.tick(60)