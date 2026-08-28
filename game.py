import pygame
import sys

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION, Y_POSITION = 400, 660
GROUND_Y = Y_POSITION

jumping = False

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/squarestand.png"), (114, 124))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/squreJump.png"), (114, 124))
BACKGROUND = pygame.image.load("assets/stage.png")

kurimanju_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_a]:
        X_POSITION -= 10
    if keys_pressed[pygame.K_d]:
        X_POSITION += 10

    if keys_pressed[pygame.K_SPACE] and not jumping:
        jumping = True
        Y_VELOCITY = JUMP_HEIGHT

    SCREEN.blit(BACKGROUND, (0, 0))
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        
        if Y_POSITION >= GROUND_Y:
            Y_POSITION = GROUND_Y
            jumping = False
            
        kurimanju_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, kurimanju_rect)
    else:
        kurimanju_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, kurimanju_rect)
        

    pygame.display.update()
    CLOCK.tick(60)