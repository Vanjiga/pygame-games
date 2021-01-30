import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

surface = pygame.surface

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color,(("yellow"))
    screenblit(surface,(200,250 ))
    pygame.display.update()
    clock.tick(60)