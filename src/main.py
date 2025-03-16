import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BLACK
from player import Player

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Game window size
clock = pygame.time.Clock()

# Create Player
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT*0.9)  # Centered at the bottom
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    screen.fill(COLOR_BLACK)  # Clear screen

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(keys)  # Pass the keys to the player's update method

    all_sprites.draw(screen)
    player.draw(screen)  # Draw bullets

    pygame.display.flip()
    clock.tick(FPS)  # 60 FPS

pygame.quit()