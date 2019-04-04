import pygame

from src.constants import particle_constants as p_c


class Particle:
    def __init__(
            self,
            coordinates,
            m=p_c.DEFAULT_PARTICLE_RADIUS,
            r=p_c.DEFAULT_PARTICLE_RADIUS,
            color=p_c.DEFAULT_PARTICLE_COLOR,
            thickness=p_c.DEFAULT_PARTICLE_THICKNESS
    ):
        self.m = m
        self.r = r
        self.coordinates = coordinates
        self.color = color
        self.thickness = thickness

    def display(self, screen):
        pygame.draw.circle(screen, self.color, self.coordinates, self.r, self.thickness)
