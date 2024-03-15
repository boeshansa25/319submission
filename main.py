"""
This file acts as the main file for the game. It initializes the game and sets up 
the window.
"""

import pygame
import sys
from dashboard import Dashboard
from strategy import Strategy
from gameEngine import Game
from siminterface import SimInterface

"""
# Initialize the game
pygame.init()

# Set up the window
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Manager")

clock = pygame.time.Clock()

game = Game(screen)
dashboard = Dashboard(screen)
strategy = Strategy(screen)
siminterface = SimInterface(screen)
game.set_dashboard(dashboard)
game.set_strategy(strategy)
game.set_simulation(siminterface)

# Game loop
FPS = 60
running = True
current_screen = "dashboard"
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            strategy.handle_event(event)
    
    
    # Draw
    screen.fill((255, 255, 255))
    #dashboard.draw()
    strategy.draw()

    # Flip the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()


"""

# Initialize the game
pygame.init()

# Set up the window
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Manager")

clock = pygame.time.Clock()

game = Game(screen)
dashboard = Dashboard(screen, game)
strategy = Strategy(screen, game)
siminterface = SimInterface(screen, game)
game.set_dashboard(dashboard)
game.set_strategy(strategy)
game.set_simulation(siminterface)
game.active_screen = dashboard

# Game loop
game.run()

# Quit the game
pygame.quit()
