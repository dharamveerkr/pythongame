import pygame
import random

from core.game_registry import register


@register(
    name="Racing",
    controls="A/D or Arrow Keys",
    description="Endless high-speed highway racing."
)
def run(screen, clock):

    BLACK = (10, 10, 10)
    WHITE = (255, 255, 255)
    RED = (255, 60, 60)
    GREEN = (0, 255, 120)
    YELLOW = (255, 220, 0)
    ROAD = (35, 35, 35)
    GRAY = (180, 180, 180)

    font_big = pygame.font.SysFont(
        "Arial",
        60,
        bold=True
    )

    font_small = pygame.font.SysFont(
        "Arial",
        26
    )

    width, height = screen.get_size()

    car_width = 50
    car_height = 90

    road_width = width * 0.55

    road_x = (width - road_width) // 2

    player_x = width // 2 - car_width // 2

    player_y = height - 120

    road_y = 0

    road_speed = 10

    obstacles = []

    spawn_timer = 0

    score = 0

    game_over = False

    def create_obstacle():

        x = random.randint(
            int(road_x + 20),
            int(road_x + road_width - car_width - 20)
        )

        speed = random.randint(9, 14)

        obstacles.append([
            x,
            -car_height,
            speed
        ])

    while True:

        width, height = screen.get_size()

        road_width = width * 0.55

        road_x = (width - road_width) // 2

        player_y = height - 120

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:

                if game_over:

                    if event.key == pygame.K_RETURN:
                        return run(screen, clock)

                    if event.key == pygame.K_ESCAPE:
                        return "menu"

        if not game_over:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_x -= 9

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_x += 9

            player_x = max(
                road_x + 20,
                min(
                    road_x + road_width - car_width - 20,
                    player_x
                )
            )

            spawn_timer += 1

            if spawn_timer > 30:

                create_obstacle()

                spawn_timer = 0

            for obs in obstacles[:]:

                obs[1] += obs[2]

                if obs[1] > height:

                    obstacles.remove(obs)

                    score += 10

            player_rect = pygame.Rect(
                player_x,
                player_y,
                car_width,
                car_height
            )

            for obs in obstacles:

                obs_rect = pygame.Rect(
                    obs[0],
                    obs[1],
                    car_width,
                    car_height
                )

                if player_rect.colliderect(obs_rect):
                    game_over = True

        screen.fill(BLACK)

        # Road
        pygame.draw.rect(
            screen,
            ROAD,
            (
                road_x,
                0,
                road_width,
                height
            )
        )

        # Road borders
        pygame.draw.line(
            screen,
            WHITE,
            (road_x, 0),
            (road_x, height),
            5
        )

        pygame.draw.line(
            screen,
            WHITE,
            (road_x + road_width, 0),
            (road_x + road_width, height),
            5
        )

        # Road lane animation
        road_y += road_speed

        if road_y >= 100:
            road_y = 0

        for i in range(-2, 10):

            y = (
                i * 100 +
                road_y
            ) % (height + 100)

            pygame.draw.rect(
                screen,
                WHITE,
                (
                    width // 2 - 6,
                    y,
                    12,
                    60
                )
            )

        # Obstacles
        for obs in obstacles:

            pygame.draw.rect(
                screen,
                RED,
                (
                    obs[0],
                    obs[1],
                    car_width,
                    car_height
                ),
                border_radius=12
            )

        # Player car
        pygame.draw.rect(
            screen,
            GREEN,
            (
                player_x,
                player_y,
                car_width,
                car_height
            ),
            border_radius=12
        )

        # HUD
        score_text = font_small.render(
            f"Score: {score}",
            True,
            WHITE
        )

        speed_text = font_small.render(
            f"Speed: {road_speed * 10} km/h",
            True,
            YELLOW
        )

        screen.blit(score_text, (20, 20))
        screen.blit(speed_text, (20, 55))

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

            title = font_big.render(
                "CRASHED!",
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

            final_score = font_small.render(
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

            retry = font_small.render(
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

            back = font_small.render(
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

        clock.tick(60)
