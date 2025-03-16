import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image_path, bullet_group, screen_width):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.direction = random.choice([-1, 1])  # Move left or right initially
        self.change_direction_time = random.randint(60, 120)  # Time before changing direction
        self.screen_width = screen_width
        self.shoot_timer = random.randint(30, 90)  # Randomized shooting intervals
        self.bullet_group = bullet_group

    def update(self):
        # Move enemy left/right and switch direction occasionally
        self.rect.x += self.speed * self.direction
        
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.direction *= -1  # Change direction on hitting screen edges
        
        self.change_direction_time -= 1
        if self.change_direction_time <= 0:
            self.direction *= -1
            self.change_direction_time = random.randint(60, 120)

        # Enemy shooting behavior
        self.shoot_timer -= 1
        if self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = random.randint(30, 90)

    def shoot(self):
        enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
        self.bullet_group.add(enemy_bullet)

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 0, 0))  # Red bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()
