import pygame


class FadeTransition:

    def __init__(
        self,
        screen
    ):

        self.screen = screen

    def fade_in(self):

        width, height = self.screen.get_size()

        overlay = pygame.Surface(
            (width, height)
        )

        overlay.fill((0, 0, 0))

        for alpha in range(255, -1, -15):

            overlay.set_alpha(alpha)

            self.screen.blit(
                overlay,
                (0, 0)
            )

            pygame.display.update()

            pygame.time.delay(10)
