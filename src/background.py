import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_SPEED

class ScrollingBackground:
    """Handles background image loading and scrolling."""
    
    def __init__(self, image_path, speed=BG_SPEED):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(SCREEN_WIDTH), SCREEN_HEIGHT))
        self.speed = speed
        self.y1 = 0
        self.y2 = -SCREEN_HEIGHT

    def update(self):
        """Moves the background downward to create a scrolling effect."""
        self.y1 += self.speed
        self.y2 += self.speed

        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = -SCREEN_HEIGHT
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = -SCREEN_HEIGHT

    def draw(self, screen):
        """Draws the background images to simulate infinite scrolling."""
        screen.blit(self.image, (0, self.y1))
        screen.blit(self.image, (0, self.y2))
