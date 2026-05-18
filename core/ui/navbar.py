import pygame

from core.settings import *


class Navbar:

    def __init__(self):

        self.font = pygame.font.SysFont(
            "Arial",
            24,
            bold=True
        )

    def draw(
        self,
        screen
    ):

        width, _ = screen.get_size()

        pygame.draw.rect(
            screen,
            (10, 12, 30),
            (
                0,
                0,
                width,
                70
            )
        )

        text = self.font.render(
            "🎮 Python Arcade",
            True,
            TEXT_PRIMARY
        )

        screen.blit(text, (30, 20))
