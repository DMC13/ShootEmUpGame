import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def game_over_screen(screen):
    """Displays the Game Over screen with a dark overlay and allows restarting."""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill((0, 0, 0))  # Black overlay
    overlay.set_alpha(180)  # Transparency level (0 = invisible, 255 = fully opaque)
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 80)  # Large font size
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))  # White text
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    
    font_restart = pygame.font.Font(None, 40)  # Smaller font size
    restart_text = font_restart.render("Press R to Restart", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

    screen.blit(game_over_text, text_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()  # Update display

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Exit loop to restart the game

def pause_screen(screen):
    """Displays a pause screen and waits for player to resume."""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(150)
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 60)
    pause_text = font.render("PAUSED", True, (255, 255, 255))
    text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    font_resume = pygame.font.Font(None, 40)
    resume_text = font_resume.render("Press P to Resume", True, (255, 255, 255))
    resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

    screen.blit(pause_text, text_rect)
    screen.blit(resume_text, resume_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                waiting = False  # Resume game

def main_menu(screen):
    """Displays the main menu before the game starts."""
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 40)
    title_text = font.render("Shoot 'Em Up Game", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))

    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False  # Start game
