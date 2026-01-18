import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 1. SETUP OBJECTS
player_rect = pygame.Rect(100, 100, 50, 50)
wall_rect = pygame.Rect(400, 200, 100, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. MOVEMENT
    keys = pygame.key.get_pressed()
    
    # Store old position in case we hit a wall
    old_pos = player_rect.topleft

    if keys[pygame.K_LEFT]:  player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5
    if keys[pygame.K_UP]:    player_rect.y -= 5
    if keys[pygame.K_DOWN]:  player_rect.y += 5

    # 3. COLLISION LOGIC
    # Check if the player is currently overlapping the wall
    if player_rect.colliderect(wall_rect):
        # HARD COLLISION: Move the player back to where they were
        player_rect.topleft = old_pos

    # 4. DRAWING
    screen.fill((30, 30, 30))
    
    # Draw wall
    pygame.draw.rect(screen, "red", wall_rect)
    
    # Draw player
    # Change color if touching (visual feedback)
    color = "green" if not player_rect.colliderect(wall_rect) else "yellow"
    pygame.draw.rect(screen, color, player_rect)
    
    pygame.display.flip()
    clock.tick(60)
