import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 1. LOADING THE IMAGE
# .convert_alpha() makes the game run much faster by 
# converting the image to the same pixel format as your screen.
try:
    player_surf = pygame.image.load("player.png").convert_alpha()
except:
    # Fallback if the user doesn't have an image yet
    player_surf = pygame.Surface((50, 50))
    player_surf.fill("green")

# 2. THE RECT (Again!)
# We use the surface to create a Rect. 
# This links the image's size to a position we can move (normally, you don't need this).
player_rect = player_surf.get_rect(center = (400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement (Lesson 04 logic)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5

    # 3. DRAWING
    screen.fill((30, 30, 30))
    
    # We blit the Surface at the Rect's position
    screen.blit(player_surf, player_rect)
    
    pygame.display.flip()
    clock.tick(60)
