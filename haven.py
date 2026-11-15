import pygame
import sys
pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Haven Hedgehog Bounce Back!")
font = pygame.font.SysFont("Arial", 36)


BLACK = (0,0,0)
WHITE = (255,255,255)

carryOn = True
clock = pygame.time.Clock()

#background
background = pygame.image.load("hero-bg.png").convert()
background = pygame.transform.scale(background, (width, height))

#haven logo
logo = pygame.image.load("logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (85,50))
logo_rect = logo.get_rect(center=(50,450))

#trampoline
# player = pygame.Rect(220,160,40,40)
player = pygame.image.load("trampoline.png").convert_alpha()
player = pygame.transform.scale(player, (150,150))
player_rect = player.get_rect(center=(350,500))

#picnic blanket
blanket = pygame.image.load("picnic_blanket.png").convert_alpha()
blanket = pygame.transform.scale(blanket, (250,250))
blanket_rect = blanket.get_rect(center=(350,275))

#cup
cup = pygame.image.load("cup.png").convert_alpha()
cup = pygame.transform.scale(cup, (60,75))
cup_rect = cup.get_rect(center=(width/2, height/2))

#hedgehog
hedgehog_image = pygame.image.load("hedgehog.png").convert_alpha()

bounces = 0
score_text = font.render(f"Bounces: {bounces}", True, (255, 255, 255))


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
        self.y_speed += 0.12
        global bounces
        global score_text

        # Move the hedgehog
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

        # Bounce off right wall
        if self.x_pos + self.radius >= width:
            self.x_pos = width - self.radius
            self.x_speed *= -1
            bounces += 1
            score_text = font.render(f"Bounces: {bounces}", True, (255, 255, 255))


        # Bounce off left wall
        if self.x_pos - self.radius <= 0:
            self.x_pos = self.radius
            self.x_speed *= -1
            bounces += 1
            score_text = font.render(f"Bounces: {bounces}", True, (255, 255, 255))


        # Bounce off top wall
        if self.y_pos - self.radius <= 0:
            self.y_pos = self.radius
            self.y_speed *= -1
            bounces += 1
            score_text = font.render(f"Bounces: {bounces}", True, (255, 255, 255))


        # Hedgehog collision rectangle
        ball_rect = pygame.Rect(
            self.x_pos - self.radius,
            self.y_pos - self.radius,
            self.radius * 2,
            self.radius * 2
        )

        # Bounce when hedgehog lands on trampoline
        if ball_rect.colliderect(player_rect) and self.y_speed > 0:
                self.y_pos = player_rect.top - self.radius
                self.y_speed = -6

        # Add bounce streak
        


# Calling class Ball to create hedgehog
ball1 = Ball(100, 100, 30, "blue", 100, 0.9, 5, 4, 1)

# if user wins:
won = False

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x-=4
    if keys[pygame.K_RIGHT]:
        player_rect.x+=4
    #below commented out to disable trampoline from moving up and down
    #if keys[pygame.K_UP]:
        #player_rect.y-=4
    #if keys[pygame.K_DOWN]:
       #player_rect.y+=4
    
    player_rect.clamp_ip(screen.get_rect())

    # when hedgehog is not in the cup, then ball is still in motion
    if not won:
         ball1.move() 

    if(player_rect.y<=0):
        lose_img = pygame.image.load("lose.png").convert()
        lose_img = pygame.transform.scale(lose_img, (width, height))
        screen.blit(lose_img, (0, 0))
    #pygame.draw.rect(screen, (255,196,0), player_rect)

    # collision for ball --> cup :)
        ball_rect = pygame.Rect(
            ball1.x_pos - ball1.radius, 
            ball1.y_pos - ball1.radius,
            ball1.radius * 2,
            ball1.radius * 2
        )

        if ball_rect.colliderect(cup_rect):
            won = True
            
    screen.blit(background, (0, 0))
    screen.blit(logo, logo_rect)
    screen.blit(player, player_rect)
    screen.blit(cup, cup_rect)
    screen.blit(score_text, (20, 20))

    ball1.draw()

    if not won:
        ball1.move()
    # else:
        # all winning image :)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
