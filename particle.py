import pygame
import random as rand
from pygame.sprite import Sprite

class Particle(Sprite):
    # A class to generate point particles
    
    def __init__(self, sun_program):
        super().__init__()
        self.screen = sun_program.screen
        self.settings = sun_program.settings

        self.point_pos = (250, 250)
        self.color = self.settings.particle_color
        self.trail_color = self.settings.trail_color
        self.point_size = self.settings.particle_size

        # Create a particle rect at (250, 250)
        self.rect = pygame.Rect(250, 250, self.point_size, self.point_size)

        # Store the particle's position as a decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Create a list to store the particle's previous positions
        self.prev_positions = []


    def update(self):
        # Move the particle around the screen
        self.xrand = rand.random()
        self.yrand = rand.random()

        # Store the particle's current position
        self.prev_positions.append((int(self.x), int(self.y)))

        # Update the decimal position of the particle
        self.x += (2 * self.xrand - 1)
        self.y += (2 * self.yrand - 1)

        # Update the rect position
        self.rect.x = self.x
        self.rect.y = self.y

        self.point_pos = (self.x, self.y)

        # Remove the oldest position if the list is too long
        if len(self.prev_positions) > 5000:
            self.prev_positions.pop(0)

    def draw_particle(self):
        # Draw the particle to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

    def draw_trail(self):
        # Draw a line connecting the particle's previous positions
        # to create a trail.
        if len(self.prev_positions) > 2:
            pygame.draw.lines(self.screen, self.trail_color, False, \
                self.prev_positions, 1)