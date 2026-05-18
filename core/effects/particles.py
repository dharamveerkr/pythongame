import pygame
import random


class Particle:

    def __init__(
        self,
        x,
        y
    ):

        self.x = x
        self.y = y

        self.radius = random.randint(2, 5)

        self.life = 60

        self.speed_x = random.uniform(-1, 1)

        self.speed_y = random.uniform(-2, 0)

    def update(self):

        self.x += self.speed_x

        self.y += self.speed_y

        self.life -= 1

    def draw(
        self,
        screen
    ):

        alpha = max(0, self.life * 4)

        surface = pygame.Surface(
            (
                self.radius * 2,
                self.radius * 2
            ),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            surface,
            (
                255,
                255,
                255,
                alpha
            ),
            (
                self.radius,
                self.radius
            ),
            self.radius
        )

        screen.blit(
            surface,
            (
                self.x,
                self.y
            )
        )


class ParticleSystem:

    def __init__(self):

        self.particles = []

    def emit(
        self,
        x,
        y,
        amount=2
    ):

        for _ in range(amount):

            self.particles.append(
                Particle(x, y)
            )

    def update(self):

        for particle in self.particles[:]:

            particle.update()

            if particle.life <= 0:

                self.particles.remove(
                    particle
                )

    def draw(
        self,
        screen
    ):

        for particle in self.particles:

            particle.draw(screen)
