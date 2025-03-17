import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_SPEED

# Define the number of lanes
# LANE_COUNT = random.randint(1, 5)  # Random number of lanes from 1 to 5
LANE_COUNT = 2
LANE_WIDTH = SCREEN_WIDTH // LANE_COUNT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png")
        self.rect = self.image.get_rect()
        
        # Randomly assign health between 1 and 5
        self.health = random.randint(1, 5)
        
        # Assign a random lane
        lane = random.randint(0, LANE_COUNT - 1)
        self.rect.x = lane * LANE_WIDTH + (LANE_WIDTH - self.rect.width) // 2
        self.rect.y = random.randint(-100, -40)  # Start off-screen at random heights
        
        # self.speed = random.randint(2, 5)
        self.speed = 1

    def update(self, screen):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
        # Draw the enemy with health automatically in update
        self.draw(screen)
    
    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        # Draw health as text in the center of the enemy
        font = pygame.font.Font(None, 80)
        health_text = font.render(str(self.health), True, (255, 255, 255))
        text_rect = health_text.get_rect(center=self.rect.center)
        screen.blit(health_text, text_rect)
