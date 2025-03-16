import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # self.speed = random.randint(2, 4)
        self.speed = BG_SPEED

    def update(self):
        self.rect.y += self.speed

        # Remove enemy if it goes off-screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
