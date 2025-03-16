import pygame
from player import Player

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Game window size
clock = pygame.time.Clock()

# Create Player
player = Player(400, 550)
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(keys)  # Pass the keys to the player's update method

    all_sprites.draw(screen)
    player.draw(screen)  # Draw bullets

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()