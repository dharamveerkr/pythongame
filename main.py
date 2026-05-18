import pygame

from core.settings import *

from core.game_registry import discover_games

from core.scenes.menu_scene import MenuScene


pygame.init()

flags = pygame.RESIZABLE

if FULLSCREEN:
    flags |= pygame.FULLSCREEN

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    flags
)

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

discover_games()

menu = MenuScene(
    screen,
    clock
)

result = menu.run()

if result == "quit":
    pygame.quit()
