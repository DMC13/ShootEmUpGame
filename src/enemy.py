import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SPEED, LANE_COUNT, LANE_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png")
        self.rect = self.image.get_rect()
        self.health = self._assign_random_health()
        self.rect.x, self.rect.y = self._assign_random_position()
        self.speed = ENEMY_SPEED

    def _assign_random_health(self):
        return random.randint(1, 5)

    def _assign_random_position(self):
        lane = random.randint(0, LANE_COUNT - 1)
        x = lane * LANE_WIDTH + (LANE_WIDTH - self.rect.width) // 2
        y = random.randint(-100, -40)
        return x, y

    def update(self, screen):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        self.draw(screen)

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self._draw_health(screen)

    def _draw_health(self, screen):
        font = pygame.font.Font(None, 80)
        health_text = font.render(str(self.health), True, (255, 255, 255))
        text_rect = health_text.get_rect(center=self.rect.center)
        screen.blit(health_text, text_rect)
