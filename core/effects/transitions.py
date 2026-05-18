import pygame


def fade(
    screen
):

    width, height = screen.get_size()

    overlay = pygame.Surface(
        (width, height)
    )

    overlay.fill((0, 0, 0))

    for alpha in range(0, 255, 20):

        overlay.set_alpha(alpha)

        screen.blit(
            overlay,
            (0, 0)
        )

        pygame.display.update()

        pygame.time.delay(10)
