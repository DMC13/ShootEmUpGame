import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH, INIT_SHOOT_INTERVAL, INIT_HEALTH
from bullet import auto_shoot

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))  # Player size
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = INIT_HEALTH
        self.bullets = pygame.sprite.Group()
        self.shoot_timer = [0]  # Store the last shoot time
        self.shoot_interval = INIT_SHOOT_INTERVAL
        self.damage_timer = pygame.time.get_ticks()  # Timer to track damage intervals

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def take_damage(self):
        """Reduces player health and checks for game over."""
        # current_time = pygame.time.get_ticks()
        # if current_time - self.damage_timer > 1000:  # Damage every second
        self.health -= 1
            # self.damage_timer = current_time  # Reset timer
            # print(f"Player Health: {self.health}")  # Debugging

    def update(self, keys):
        self.move(keys)
        auto_shoot(self.rect.centerx, self.rect.top, self.bullets, self.shoot_timer, self.shoot_interval)
        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)
        self.draw_health(screen)

    def draw_health(self, screen):
        """Displays player health at the top-right corner."""
        font = pygame.font.Font(None,40)
        health_text = font.render(f"hp {self.health}", True, (255, 255, 255))
        screen.blit(health_text, (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 50))
