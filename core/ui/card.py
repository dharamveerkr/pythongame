import pygame

from core.settings import *

from core.effects.glow import draw_glow


class GameCard:

    def __init__(
        self,
        game,
        x,
        y,
        width,
        height
    ):

        self.game = game

        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        self.title_font = pygame.font.SysFont(
            "Arial",
            34,
            bold=True
        )

        self.info_font = pygame.font.SysFont(
            "Arial",
            20
        )

    def draw(
        self,
        screen,
        mouse_pos
    ):

        hovered = self.rect.collidepoint(
            mouse_pos
        )

        color = (
            CARD_HOVER
            if hovered
            else CARD_COLOR
        )

        if hovered:

            draw_glow(
                screen,
                self.rect.center,
                ACCENT,
                90
            )

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=28
        )

        pygame.draw.rect(
            screen,
            ACCENT,
            self.rect,
            width=2,
            border_radius=28
        )

        title = self.title_font.render(
            self.game["name"],
            True,
            TEXT_PRIMARY
        )

        title_rect = title.get_rect(
            center=(
                self.rect.centerx,
                self.rect.y + 35
            )
        )

        screen.blit(
            title,
            title_rect
        )

        controls = self.info_font.render(
            self.game["controls"],
            True,
            TEXT_SECONDARY
        )

        screen.blit(
            controls,
            (
                self.rect.x + 25,
                self.rect.y + 70
            )
        )

        desc = self.info_font.render(
            self.game["description"],
            True,
            TEXT_SECONDARY
        )

        screen.blit(
            desc,
            (
                self.rect.x + 25,
                self.rect.y + 95
            )
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
