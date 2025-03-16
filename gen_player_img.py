import pygame
import os

pygame.init()
player_image = pygame.Surface((50, 50))  # Create a 50x50 square
# player_image.fill((0, 255, 0))  # Fill with green color
player_image.fill((255, 0, 0))  # Fill with red color

# save_path = os.path.join("assets/images", "player.png")
save_path = os.path.join("assets/images", "enemy.png")

os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists
pygame.image.save(player_image, save_path)

print(f"Placeholder player sprite saved at {save_path}")