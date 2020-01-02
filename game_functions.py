import sys
from settings import Settings

import pygame


def checks_events(ship):
    """Handle Mouse and Keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_setting, screen, ship):
    """Update images and flip on the screen"""
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    pygame.display.flip()
