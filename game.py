import pygame
import sys

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping in PyGame")

kurimaju_height, kurimanju_width = 124, 114

X_POSITION, Y_POSITION = 400, 660
GROUND_Y = Y_POSITION

platform_positions = [
    (900, 600),
    (1300, 500),
    (1700, 650),
]

jumping = False

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/squarestand.png"), (114, 124))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/squreJump.png"), (114, 124))
PLATFORM = pygame.transform.scale(pygame.image.load("assets/platform.png"), (143, 35))
BACKGROUND = pygame.image.load("assets/stage.png")

for px, py in platform_positions:
    platform_rect = PLATFORM.get_rect(center=(px, py))
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

    camera_offset_x = X_POSITION - SCREEN_WIDTH // 2

    camera_offset_x = max(0, camera_offset_x)
    camera_offset_x = min(camera_offset_x, BACKGROUND.get_width() - SCREEN_WIDTH)

    SCREEN.blit(BACKGROUND, (-camera_offset_x, 0))
    for px, py in platform_positions:
        SCREEN.blit(PLATFORM, (px - camera_offset_x, py))

    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_POSITION >= GROUND_Y:
            Y_POSITION = GROUND_Y
            jumping = False
        kurimanju_rect = JUMPING_SURFACE.get_rect(
            center=(X_POSITION - camera_offset_x, Y_POSITION)
        )
        SCREEN.blit(JUMPING_SURFACE, kurimanju_rect)
    else:
        kurimanju_rect = STANDING_SURFACE.get_rect(
            center=(X_POSITION - camera_offset_x, Y_POSITION)
        )
        SCREEN.blit(STANDING_SURFACE, kurimanju_rect)

    pygame.display.update()
    CLOCK.tick(60)