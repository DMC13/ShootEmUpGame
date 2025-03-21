import pygame
import random
from config import SCREEN_HEIGHT, LANE_COUNT, LANE_WIDTH, ENTITY_SPEED

class EntityObject(pygame.sprite.Sprite):
    def __init__(self, image, health, speed=ENTITY_SPEED, x=None, y=None):
        super().__init__()
        self.image = image
        self.health = health
        self.speed = speed

        self.rect = self.image.get_rect()
        if x is None or y is None:
            x, y = self._assign_random_position()
        self.rect.x, self.rect.y = x,y

        self.collided_with_player = False

    def _assign_random_position(self):
        lane = random.randint(0, LANE_COUNT - 1)
        x = lane * LANE_WIDTH + (LANE_WIDTH - self.rect.width) // 2
        y = random.randint(-100, -40)
        return x, y

    def update(self, player, screen):
        if not self.collided_with_player:
            self.rect.y += self.speed

        if self._check_collide_with_player(player):
            self.collided_with_player = True
            # self.on_collision_with_player(player)
        
        if self.health <= 0:
            self.kill()

        self.draw(screen)

    def _check_collide_with_player(self, player):
        return self.rect.bottom >= player.rect.top

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self._draw_health(screen)

    def _draw_health(self, screen):
        font = pygame.font.Font(None, 40)
        health_text = font.render(str(self.health), True, (255, 255, 255))
        text_rect = health_text.get_rect(center=self.rect.center)
        screen.blit(health_text, text_rect)

    # def take_damage(self, amount):
    #     self.health -= amount
    #     if self.health <= 0:
    #         self.on_destroy()

    def on_collision_with_player(self, player):
        pass  # Overridden by subclasses