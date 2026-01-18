import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 1. DEFINE STARTING POSITION
player_x = 400
player_y = 300
player_speed = 5

while True:
    # A. EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Example of an Event: One-time press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Jump!") # This only triggers ONCE per press

    # B. CONTINUOUS MOVEMENT (Polling)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # C. DRAWING
    screen.fill((30, 30, 30)) # Dark background
    
    # Draw the player at the updated x and y
    pygame.draw.rect(screen, "cyan", (player_x, player_y, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)
