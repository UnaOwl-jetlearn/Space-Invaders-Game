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
red_health = 10
yellow_health = 10

RED_HIT = pygame.USEREVENT
YELLOW_HIT = pygame.USEREVENT

bullet_velocity = 5
fps = 60

def handle_bullets(yellow_bullet,yellow,red_bullet,red):
    for i in yellow_bullet:
        i.x -= bullet_velocity
        
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullet.remove(i)
            yellow_health -= 1
            break
    
    for i in red_bullet:
        i.x += bullet_velocity

        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullet.remove(i)
            red_health -= 1
            break

def draw_window(red,yellow,red_bullet,yellow_bullet):
    screen.blit(sky,(0,0))
    screen.blit(red_ship, (red.x,red.y))
    screen.blit(yellow_ship, (yellow.x,yellow.y))
    
    for i in red_bullet:
        pygame.draw.rect(screen,"red",i)
    for i in yellow_bullet:
        pygame.draw.rect(screen, "yellow",i)

    font = pygame.font.SysFont("Arial", 40)
    text = font.render("Health Red Ship:",red_health,"yellow")
    screen.blit(text,(10,10))
    
    pygame.display.update()

def main():
    yellow = pygame.Rect((900,300,60,40))
    red = pygame.Rect((100,300,60,40))

    red_bullet = []
    yellow_bullet= []

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:
                    bullet = pygame.Rect(red.x+red.width,red.y+red.height // 2 - 2,20,10)
                    red_bullet.append(bullet)
                if i.key == pygame.K_RSHIFT:
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height // 2 - 2,20,10)
                    yellow_bullet.append(bullet)
        keypress = pygame.key.get_pressed()
        yellow_move(keypress,yellow)
        red_move(keypress,red)

        handle_bullets(yellow_bullet,yellow,red_bullet,red)
        draw_window(red,yellow,red_bullet,yellow_bullet)
        
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

def red_move(keypress,red):
    if keypress[pygame.K_a]:
        red.x -= 1
    if keypress[pygame.K_d]:
        red.x += 1
    if keypress[pygame.K_w]:
        red.y -= 1
    if keypress[pygame.K_s]:
        red.y += 1

main()