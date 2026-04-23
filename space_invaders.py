import pygame, os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Space Invaders Game")
run = True

sky = pygame.image.load("space_invaders/images/sky.png")
ship1 = pygame.image.load("space_invaders/images/red_ship.png")
ship2 = pygame.image.load("space_invaders/images/yellow_ship.png")
red_ship = pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),90)
yellow_ship = pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)),270)

def draw_window(red,yellow):
    screen.blit(sky,(0,0))
    screen.blit(red_ship, (red.x,red.y))
    screen.blit(yellow_ship, (yellow.x,yellow.y))

def main():
    yellow = pygame.Rect((900,300,60,40))
    red = pygame.Rect((100,300,60,40))

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
        
        keypress = pygame.key.get_pressed()
        yellow_move(keypress,yellow)

        draw_window(red,yellow)
        pygame.display.update()

def yellow_move(keypress,yellow):
    if keypress[pygame.K_LEFT]:
        yellow.x -= 1
    if keypress[pygame.K_RIGHT]:
        yellow.x += 1
    if keypress[pygame.K_UP]:
        yellow.y -= 1
    if keypress[pygame.K_DOWN]:
        yellow.y += 1


main()