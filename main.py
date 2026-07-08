import pygame

pygame.init()

# -----------------------
# Window
# -----------------------
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peekaboo Spirit")

clock = pygame.time.Clock()

# -----------------------
# Ghost
# -----------------------
ghost_x = 150
ghost_y = 400
speed = 3

# -----------------------
# Sparkles
# -----------------------
sparkles = []
sparkle_timer = 0

running = True

while running:

    # -----------------------
    # Events
    # -----------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -----------------------
    # Keyboard
    # -----------------------
    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_d]:
        ghost_x += speed
        moved = True

    if keys[pygame.K_a]:
        ghost_x -= speed
        moved = True

    if keys[pygame.K_w]:
        ghost_y -= speed
        moved = True

    if keys[pygame.K_s]:
        ghost_y += speed
        moved = True

    # -----------------------
    # Sparkle Creation
    # -----------------------
    if moved:
        sparkle_timer += 1

        if sparkle_timer >= 3:
            sparkles.append([ghost_x, ghost_y, 14])
            sparkle_timer = 0

    # -----------------------
    # Background
    # -----------------------
    screen.fill((255, 228, 236))

    # -----------------------
    # Draw Sparkles
    # -----------------------
    for sparkle in sparkles:

        pygame.draw.circle(
            screen,
            (255, 250, 180),
            (int(sparkle[0]), int(sparkle[1])),
            max(2, sparkle[2] // 3)
        )

        sparkle[1] -= 0.4
        sparkle[2] -= 0.5

    sparkles = [s for s in sparkles if s[2] > 0]

    # -----------------------
    # Shadow
    # -----------------------
    pygame.draw.ellipse(
        screen,
        (220, 190, 200),
        (ghost_x - 18, ghost_y + 30, 36, 10)
    )

    # -----------------------
    # Ghost Body
    # -----------------------
    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (ghost_x, ghost_y),
        22
    )

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (ghost_x - 22, ghost_y, 44, 24)
    )

    pygame.draw.circle(screen, (255,255,255), (ghost_x-14, ghost_y+20), 8)
    pygame.draw.circle(screen, (255,255,255), (ghost_x, ghost_y+24), 8)
    pygame.draw.circle(screen, (255,255,255), (ghost_x+14, ghost_y+20), 8)

    # -----------------------
    # Face
    # -----------------------
    pygame.draw.circle(screen, (0,0,0), (ghost_x-7, ghost_y-5), 3)
    pygame.draw.circle(screen, (0,0,0), (ghost_x+7, ghost_y-5), 3)

    pygame.draw.arc(
        screen,
        (0,0,0),
        (ghost_x-8, ghost_y+2, 16, 10),
        0,
        3.14,
        2
    )

    pygame.draw.circle(screen, (255,180,190), (ghost_x-12, ghost_y+2), 3)
    pygame.draw.circle(screen, (255,180,190), (ghost_x+12, ghost_y+2), 3)

    # -----------------------
    # Update Screen
    # -----------------------
    pygame.display.flip()

    clock.tick(60)

pygame.quit()