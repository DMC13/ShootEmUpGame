import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_SPEED, FPS, COLOR_BLACK
from player import Player
from enemy import Enemy
from bullet import Bullet

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((int(SCREEN_WIDTH), SCREEN_HEIGHT))
pygame.display.set_caption("Shoot 'Em Up Game")

# Load background image
background = pygame.image.load("assets/images/background2.jpg")
background = pygame.transform.scale(background, (int(SCREEN_WIDTH), SCREEN_HEIGHT))

# Background scrolling
bg_y1 = 0
bg_y2 = -SCREEN_HEIGHT

# Create player instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

# Enemy and bullet management
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

wave_count = 1
enemy_spawn_delay = 1000  # milliseconds
last_spawn_time = pygame.time.get_ticks()
enemies_per_wave = 5

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()

    # Update background scroll
    bg_y1 += BG_SPEED
    bg_y2 += BG_SPEED

    # Reset background position for infinite scrolling
    if bg_y1 >= SCREEN_HEIGHT:
        bg_y1 = -SCREEN_HEIGHT
    if bg_y2 >= SCREEN_HEIGHT:
        bg_y2 = -SCREEN_HEIGHT

    # Spawn enemy waves
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > enemy_spawn_delay and len(enemy_group) < enemies_per_wave:
        enemy = Enemy()  # Now properly spawns in lanes
        enemy_group.add(enemy)
        last_spawn_time = current_time

    # Increase difficulty over time
    if len(enemy_group) == 0:
        wave_count += 1
        enemies_per_wave += 2  # More enemies per wave

    # Update game objects
    player.update(keys)
    bullet_group.update()
    enemy_group.update(screen)

    # Check for collisions between bullets and enemies
    for enemy in enemy_group:
        bullet_hits = pygame.sprite.spritecollide(enemy, player.bullets, True)
        if bullet_hits:
            enemy.take_damage()  # Reduce enemy health when hit

    # Draw everything
    screen.fill(COLOR_BLACK)
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))
    
    player.draw(screen)
    bullet_group.draw(screen)

    # Ensure enemy health is drawn correctly
    for enemy in enemy_group:
        enemy.draw(screen)

    pygame.display.flip()

pygame.quit()
