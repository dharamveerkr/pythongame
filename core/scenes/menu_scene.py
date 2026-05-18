import pygame

from core.settings import *

from core.ui.card import GameCard
from core.ui.navbar import Navbar

from core.effects.particles import ParticleSystem
from core.effects.glow import draw_glow

from core.game_registry import (
    get_games,
    run_game
)


class MenuScene:

    def __init__(
        self,
        screen,
        clock
    ):

        self.screen = screen

        self.clock = clock

        self.games = get_games()

        self.cards = []

        self.navbar = Navbar()

        self.particles = ParticleSystem()

        self.title_font = pygame.font.SysFont(
            "Arial",
            70,
            bold=True
        )

        self.build_cards()

    def build_cards(self):

        self.cards.clear()

        width, height = self.screen.get_size()

        card_width = 420
        card_height = 130

        spacing = 35

        total_height = (
            len(self.games) *
            (card_height + spacing)
        )

        start_y = (
            height // 2 -
            total_height // 2
        )

        for index, game in enumerate(self.games):

            x = width // 2 - card_width // 2

            y = start_y + index * (
                card_height + spacing
            )

            self.cards.append(

                GameCard(
                    game,
                    x,
                    y,
                    card_width,
                    card_height
                )

            )

    def run(self):

        running = True

        while running:

            mouse_pos = pygame.mouse.get_pos()

            width, height = self.screen.get_size()

            self.screen.fill(
                BACKGROUND_BOTTOM
            )

            self.particles.emit(
                mouse_pos[0],
                mouse_pos[1],
                1
            )

            self.particles.update()

            self.particles.draw(
                self.screen
            )

            self.navbar.draw(
                self.screen
            )

            title = self.title_font.render(
                "ARCADE HUB",
                True,
                TEXT_PRIMARY
            )

            title_rect = title.get_rect(
                center=(width // 2, 110)
            )

            draw_glow(
                self.screen,
                title_rect.center,
                ACCENT,
                120
            )

            self.screen.blit(
                title,
                title_rect
            )

            self.build_cards()

            for card in self.cards:

                card.draw(
                    self.screen,
                    mouse_pos
                )

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.VIDEORESIZE:

                    self.screen = pygame.display.set_mode(
                        (
                            event.w,
                            event.h
                        ),
                        pygame.RESIZABLE
                    )

                for card in self.cards:

                    if card.clicked(event):

                        result = run_game(
                            card.game["name"],
                            self.screen,
                            self.clock
                        )

                        if result == "quit":
                            return "quit"

            self.clock.tick(FPS)

        return "quit"
