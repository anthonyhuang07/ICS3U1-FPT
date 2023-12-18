import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1000, 700))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            button = event.button

    pygame.display.update()

pygame.quit()