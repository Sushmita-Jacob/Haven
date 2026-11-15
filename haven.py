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
# player = pygame.Rect(220,160,40,40)
player = pygame.image.load("trampoline.png").convert_alpha()
player = pygame.transform.scale(player, (150,150))
player_rect = player.get_rect(center=(350,500))

cup = pygame.image.load("cup.png").convert_alpha()
cup = pygame.transform.scale(cup, (60,75))
cup_rect = cup.get_rect(center=(350, 250))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x-=4
    if keys[pygame.K_RIGHT]:
        player_rect.x+=4
    #if keys[pygame.K_UP]:
        #player_rect.y-=4
    #if keys[pygame.K_DOWN]:
       #player_rect.y+=4

    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(cup, cup_rect)
    
    player_rect.clamp_ip(screen.get_rect())

    #pygame.draw.rect(screen, (255,196,0), player_rect)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
