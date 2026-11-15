import pygame
import sys
pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Haven Hedgehog Cup Pong!")

BLACK = (0,0,0)
WHITE = (255,255,255)

carryOn = True
clock = pygame.time.Clock()

background = pygame.image.load("hero-bg.png").convert()
background = pygame.transform.scale(background, (width, height))
player = pygame.Rect(220,160,40,40)
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x-=4
    if keys[pygame.K_RIGHT]:
        player.x+=4
    if keys[pygame.K_UP]:
        player.y-=4
    if keys[pygame.K_DOWN]:
        player.y+=4

    screen.blit(background, (0, 0))
    
    player.clamp_ip(screen.get_rect())

    pygame.draw.rect(screen, (255,196,0), player)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
