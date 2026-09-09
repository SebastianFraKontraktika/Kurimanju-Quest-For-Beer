import pygame
import sys

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kurimanjus quest for beer")

X_POSITION, Y_POSITION = 400, 660
GROUND_Y = Y_POSITION

platform_positions = [
    (900, 600),
    (1300, 500),
    (1700, 250),
]

jumping = False
on_ground = True

PLAYER_WIDTH, PLAYER_HEIGHT = 114, 124

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/squarestand.png"), (114, 124))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/squreJump.png"), (114, 124))
PLATFORM = pygame.transform.scale(pygame.image.load("assets/platform.png"), (143, 35))
BACKGROUND = pygame.image.load("assets/stage.png")

platform_rects = [PLATFORM.get_rect(center=(px, py)) for px, py in platform_positions]

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

    if keys_pressed[pygame.K_SPACE] and on_ground:
        jumping = True
        on_ground = False
        Y_VELOCITY = JUMP_HEIGHT

    prev_y = Y_POSITION
    if not on_ground:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY

    player_rect = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
    player_rect.center = (X_POSITION, Y_POSITION)

    on_ground = False

    check_rect = player_rect.inflate(0, 4)

    if Y_VELOCITY < 0:
        for platform_rect in platform_rects:
            if check_rect.colliderect(platform_rect):
                player_bottom_prev = prev_y + PLAYER_HEIGHT // 2
                if player_bottom_prev <= platform_rect.top + 2:
                    Y_POSITION = platform_rect.top - PLAYER_HEIGHT // 2
                    Y_VELOCITY = 0
                    jumping = False
                    on_ground = True
                    break

    if Y_POSITION >= GROUND_Y:
        Y_POSITION = GROUND_Y
        Y_VELOCITY = 0
        jumping = False
        on_ground = True

    player_rect.center = (X_POSITION, Y_POSITION)

    camera_offset_x = X_POSITION - SCREEN_WIDTH // 2

    bg_width = BACKGROUND.get_width()
    tile_x = camera_offset_x % bg_width

    num_tiles_needed = 10

    for i in range(num_tiles_needed):
        SCREEN.blit(BACKGROUND, (i * bg_width - camera_offset_x, 0))

    camera_offset_x = max(0, camera_offset_x)
    camera_offset_x = min(camera_offset_x, (BACKGROUND.get_width() * (num_tiles_needed - 1)) - SCREEN_WIDTH)

    for px, py in platform_positions:
        SCREEN.blit(PLATFORM, (px - camera_offset_x, py))

    draw_rect_x = X_POSITION - camera_offset_x
    if not on_ground:
        kurimanju_rect = JUMPING_SURFACE.get_rect(center=(draw_rect_x, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, kurimanju_rect)
    else:
        kurimanju_rect = STANDING_SURFACE.get_rect(center=(draw_rect_x, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, kurimanju_rect)

    pygame.display.update()
    CLOCK.tick(60)