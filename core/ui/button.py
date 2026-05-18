import pygame

from core.settings import *


class Button:

    def __init__(
        self,
        text,
        rect
    ):

        self.text = text

        self.rect = pygame.Rect(rect)

        self.font = pygame.font.SysFont(
            "Arial",
            28,
            bold=True
        )

    def draw(
        self,
        screen,
        mouse_pos
    ):

        hovered = self.rect.collidepoint(
            mouse_pos
        )

        color = CARD_HOVER if hovered else CARD_COLOR

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=20
        )

        text = self.font.render(
            self.text,
            True,
            TEXT_PRIMARY
        )

        text_rect = text.get_rect(
            center=self.rect.center
        )

        screen.blit(
            text,
            text_rect
        )

    def clicked(
        self,
        event
    ):

        return (
            event.type ==
            pygame.MOUSEBUTTONDOWN
            and
            self.rect.collidepoint(
                event.pos
            )
        )
