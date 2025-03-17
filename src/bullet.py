import pygame

# Initialize pygame mixer (if not initialized elsewhere)
pygame.mixer.init()

# Load the shooting sound
shoot_sound = pygame.mixer.Sound("assets/sounds/Gunfire And Voices.mp3")
shoot_sound.set_volume(0.1)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, shoot_sound=shoot_sound):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Bullet size
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10  # Move upward
        
        # Play the shoot sound when a bullet is created
        shoot_sound.play()

    def update(self):
        """Move the bullet upward and remove it if it leaves the screen."""
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet from the sprite group

def auto_shoot(player_x, player_y, bullets_group, shoot_timer, shoot_interval):
    """Automatically shoots bullets at a fixed interval."""
    current_time = pygame.time.get_ticks()
    if current_time - shoot_timer[0] > shoot_interval:
        bullet = Bullet(player_x, player_y)
        bullets_group.add(bullet)
        shoot_timer[0] = current_time
