import pygame


def draw_glow(
    screen,
    center,
    color,
    radius
):

    glow = pygame.Surface(
        (
            radius * 2,
            radius * 2
        ),
        pygame.SRCALPHA
    )

    for i in range(radius, 0, -8):

        alpha = max(0, 150 - i)

        pygame.draw.circle(
            glow,
            (*color, alpha),
            (radius, radius),
            i
        )

    screen.blit(
        glow,
        (
            center[0] - radius,
            center[1] - radius
        ),
        special_flags=pygame.BLEND_RGBA_ADD
    )
