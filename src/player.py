import pygame
from bullet import auto_shoot

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Player size
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.bullets = pygame.sprite.Group()  # Bullet storage
        self.shoot_timer = [0]  # Store the last shoot time

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:  # Adjust width accordingly
            self.rect.x += self.speed

    def update(self, keys):
        self.move(keys)
        auto_shoot(self.rect.centerx, self.rect.top, self.bullets, self.shoot_timer)
        self.bullets.update()  # Update all bullets

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)  # Draw bullets on the screen