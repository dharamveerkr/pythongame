import pygame
import random

from core.game_registry import register


@register(
    name="Snake",
    controls="Arrow Keys",
    description="Classic arcade snake with modern visuals."
)
def run(screen, clock):

    CELL = 20

    BLACK = (10, 10, 18)
    GREEN = (0, 255, 120)
    RED = (255, 70, 70)
    WHITE = (255, 255, 255)
    GRAY = (180, 180, 180)

    title_font = pygame.font.SysFont(
        "Arial",
        60,
        bold=True
    )

    font = pygame.font.SysFont(
        "Arial",
        28
    )

    width, height = screen.get_size()

    snake = [[200, 200]]

    direction = "RIGHT"

    food = [
        random.randrange(0, width, CELL),
        random.randrange(0, height, CELL)
    ]

    score = 0

    game_over = False

    while True:

        width, height = screen.get_size()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:

                if game_over:

                    if event.key == pygame.K_RETURN:
                        return run(screen, clock)

                    if event.key == pygame.K_ESCAPE:
                        return "menu"

                else:

                    if event.key == pygame.K_UP and direction != "DOWN":
                        direction = "UP"

                    elif event.key == pygame.K_DOWN and direction != "UP":
                        direction = "DOWN"

                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        direction = "LEFT"

                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        direction = "RIGHT"

        if not game_over:

            head_x, head_y = snake[0]

            if direction == "UP":
                head_y -= CELL

            elif direction == "DOWN":
                head_y += CELL

            elif direction == "LEFT":
                head_x -= CELL

            elif direction == "RIGHT":
                head_x += CELL

            new_head = [head_x, head_y]

            if (
                head_x < 0 or
                head_x >= width or
                head_y < 0 or
                head_y >= height or
                new_head in snake
            ):
                game_over = True

            snake.insert(0, new_head)

            if new_head == food:

                score += 1

                food = [
                    random.randrange(0, width, CELL),
                    random.randrange(0, height, CELL)
                ]

            else:
                snake.pop()

        screen.fill(BLACK)

        # Grid
        for x in range(0, width, CELL):

            pygame.draw.line(
                screen,
                (20, 20, 30),
                (x, 0),
                (x, height)
            )

        for y in range(0, height, CELL):

            pygame.draw.line(
                screen,
                (20, 20, 30),
                (0, y),
                (width, y)
            )

        # Snake
        for segment in snake:

            pygame.draw.rect(
                screen,
                GREEN,
                (
                    segment[0],
                    segment[1],
                    CELL,
                    CELL
                ),
                border_radius=5
            )

        # Food
        pygame.draw.rect(
            screen,
            RED,
            (
                food[0],
                food[1],
                CELL,
                CELL
            ),
            border_radius=20
        )

        # Score
        score_text = font.render(
            f"Score: {score}",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (20, 20)
        )

        if game_over:

            overlay = pygame.Surface(
                (width, height)
            )

            overlay.set_alpha(220)

            overlay.fill((0, 0, 0))

            screen.blit(
                overlay,
                (0, 0)
            )

            title = title_font.render(
                "GAME OVER",
                True,
                RED
            )

            title_rect = title.get_rect(
                center=(width // 2, height // 2 - 120)
            )

            screen.blit(
                title,
                title_rect
            )

            final_score = font.render(
                f"Final Score: {score}",
                True,
                WHITE
            )

            score_rect = final_score.get_rect(
                center=(width // 2, height // 2 - 20)
            )

            screen.blit(
                final_score,
                score_rect
            )

            retry = font.render(
                "ENTER = Try Again",
                True,
                GREEN
            )

            retry_rect = retry.get_rect(
                center=(width // 2, height // 2 + 50)
            )

            screen.blit(
                retry,
                retry_rect
            )

            back = font.render(
                "ESC = Back To Menu",
                True,
                GRAY
            )

            back_rect = back.get_rect(
                center=(width // 2, height // 2 + 100)
            )

            screen.blit(
                back,
                back_rect
            )

        pygame.display.update()

        clock.tick(12)
