import pygame
import random
from entity import EntityObject
from config import SCREEN_HEIGHT, ENEMY_SPEED, LANE_COUNT, LANE_WIDTH

default_image = pygame.image.load("assets/images/enemy.png")

class Enemy(EntityObject):
    def __init__(self, image=default_image, damage_per_second=1):
        health = self._assign_random_health()
        super().__init__(image, health, ENEMY_SPEED)
        self.damage_per_second = damage_per_second
        self.last_damage_time = pygame.time.get_ticks()

    def _assign_random_health(self):
        return random.randint(1, 5)

    def update(self, screen, player):
        super().update(player, screen)
        if self.collided_with_player:
            self.deal_damage(player)
    
    def on_collision_with_player(self, player):
        self.deal_damage(player)

    def deal_damage(self, player):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_damage_time >= 1000:  # damage every 1 sec
            player.take_damage(self.damage_per_second)
            self.take_damage()
            self.last_damage_time = current_time

    def take_damage(self):
        """Reduces enemy health and checks for death."""
        self.health -= 1