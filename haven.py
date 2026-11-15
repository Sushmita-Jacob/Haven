import pygame
pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Haven")

BLACK = (0,0,0)
WHITE = (255,255,255)

carryOn = True
clock = pygame.time.Clock()

background = pygame.image.load("hero-bg.png").convert()
background = pygame.transform.scale(background, (width, height))
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    screen.blit(background, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()