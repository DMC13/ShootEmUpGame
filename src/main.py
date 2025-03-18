import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player
from enemy import Enemy
from bullet import Bullet
from background import ScrollingBackground
from ui import game_over_screen, pause_screen, main_menu

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((int(SCREEN_WIDTH), SCREEN_HEIGHT))
pygame.display.set_caption("Shoot 'Em Up Game")

main_menu(screen)

# Initialize background
background = ScrollingBackground("assets/images/background2.jpg")

def run_game():
    """Main game loop."""
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
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause_screen(screen)

        # Update background
        background.update()

        # Get key states
        keys = pygame.key.get_pressed()

        # Spawn enemy waves
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > enemy_spawn_delay and len(enemy_group) < enemies_per_wave:
            enemy = Enemy()
            enemy_group.add(enemy)
            last_spawn_time = current_time

        # Increase difficulty over time
        if len(enemy_group) == 0:
            wave_count += 1
            enemies_per_wave += 2  # More enemies per wave

        # Update game objects
        player.update(keys)
        bullet_group.update()
        
        for enemy in enemy_group:
            enemy.update(screen, player)  # Pass the player object

        # Check for collisions between bullets and enemies
        for enemy in enemy_group:
            bullet_hits = pygame.sprite.spritecollide(enemy, player.bullets, True)
            if bullet_hits:
                enemy.take_damage()

        # Draw everything
        background.draw(screen)
        player.draw(screen)
        bullet_group.draw(screen)

        for enemy in enemy_group:
            enemy.draw(screen)

        pygame.display.flip()

        # Check for game over
        if player.health <= 0:
            game_over_screen(screen)
            return

while True:
    run_game()
