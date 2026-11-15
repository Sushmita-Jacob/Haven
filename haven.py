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

hedgehog_image = pygame.image.load("hedgehog.png").convert_alpha()

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass,
                 retention, y_speed, x_speed, id):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id

        # Use hedgehog image instead of a circle
        self.image = pygame.transform.scale(
            hedgehog_image, (radius * 2, radius * 2)
        )

    def draw(self):
        # Draw the hedgehog image
        screen.blit(
            self.image,
            (self.x_pos - self.radius,
             self.y_pos - self.radius)
        )

    def move(self):
        # Gravity
        self.y_speed += 0.25

        # Move the hedgehog
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

        # Bounce off right wall
        if self.x_pos + self.radius >= width:
            self.x_pos = width - self.radius
            self.x_speed *= -1

        # Bounce off left wall
        if self.x_pos - self.radius <= 0:
            self.x_pos = self.radius
            self.x_speed *= -1

        # Bounce off top wall
        if self.y_pos - self.radius <= 0:
            self.y_pos = self.radius
            self.y_speed *= -1

        # Hedgehog collision rectangle
        ball_rect = pygame.Rect(
            self.x_pos - self.radius,
            self.y_pos - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        # Bounce when hedgehog lands on trampoline
        if ball_rect.colliderect(player_rect) and self.y_speed > 0:
            if ball_rect.bottom - self.y_speed <= player_rect.top:
                self.y_pos = player_rect.top - self.radius
                self.y_speed = -10


# Create hedgehog
ball1 = Ball(100, 100, 30, "blue", 100, 0.9, 5, 4, 1)


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

     # NEW CODE: Move the hedgehog
    ball1.move()

    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(cup, cup_rect)
    
    player_rect.clamp_ip(screen.get_rect())

    #pygame.draw.rect(screen, (255,196,0), player_rect)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
