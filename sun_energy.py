import sys
import pygame
from time import sleep

from sun_settings import Settings
from button import Button
from particle import Particle

class SunEnergy:
    # Overall class to manage program assets and behavior
    def __init__(self):
        # Initialize the program, and create resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((\
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Solar Energy Flow")

        # Make the starting buttons
        self.opt1, self.opt2, self.opt3, self.opt4, self.opt5 = \
        'Tiny star (r = 25) 10 particles', 'Small star (r = 50) 10 particles', \
        'Medium star (r = 100) 10 particles', \
        'Medium star (r = 200) 100 particles', \
        'Large star (r = 200) 10 particles'

        self.play_button = Button(self, self.opt1, self.opt2, self.opt3, \
            self.opt4, self.opt5)

        # Make the particles
        self.particles = pygame.sprite.Group()

        # Make the circle
        self.circle = pygame.draw.circle(self.screen, \
            self.settings.circle_color, self.settings.circle_pos, \
            self.settings.circle_radius, self.settings.circle_thickness)

        # Initialize number of moves
        self.num_moves = 0


    def run_program(self):
        # Start the main loop for the program
        while True:
            self._check_events()
            if self.settings.program_active:
                self._update_particles()

            pygame.time.Clock().tick(self.settings.frameratecap)
            self._update_screen()


    def _check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # Controls flags related to keypresses and button clicks
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        # Start the program when the user clicks any of the buttons
        button1_clicked = self.play_button.rect1.collidepoint(mouse_pos)
        if button1_clicked and not self.settings.program_active:
            self.settings.tiny_star()
            self.settings.particles_allowed = 10
            self._start_program()

        button2_clicked = self.play_button.rect2.collidepoint(mouse_pos)
        if button2_clicked and not self.settings.program_active:
            self.settings.small_star()
            self.settings.particles_allowed = 10
            self._start_program()

        button3_clicked = self.play_button.rect3.collidepoint(mouse_pos)
        if button3_clicked and not self.settings.program_active:
            self.settings.medium_star()
            self.settings.particles_allowed = 10
            self._start_program()

        button4_clicked = self.play_button.rect4.collidepoint(mouse_pos)
        if button4_clicked and not self.settings.program_active:
            self.settings.medium_star()
            self.settings.particles_allowed = 100
            self._start_program()

        button5_clicked = self.play_button.rect5.collidepoint(mouse_pos)
        if button5_clicked and not self.settings.program_active:
            self.settings.large_star()
            self.settings.particles_allowed = 10
            self._start_program()


    def _start_program(self):
        self.settings.program_active = True
        self.num_moves = 0
        self._create_particles()


    def _check_keydown_events(self, event):
        # Respond to keypresses
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()


    def _create_particles(self):
        # Create new particles and add them to the particles group
        for i in range(self.settings.particles_allowed):
            particle = Particle(self)
            self.particles.add(particle)


    def _update_particles(self):
        # Update position of particles and get rid of escaped particles
        for particle in self.particles:
            particle.update()
            self.num_moves += 1

        # Get rid of particles that have escaped
        for particle in self.particles.copy():
            distance = ((particle.x - 250)**2 + (particle.y - 250)**2)**0.5
            if distance > self.settings.circle_radius:
                self.particles.remove(particle)

        if not self.particles:
            self.settings.program_active = False


    def _display_total(self):
        num_moves_str = "{:,}".format(self.num_moves)
        font = pygame.font.Font(None, 36)
        text = font.render("Total photon movements: " + str(num_moves_str), \
            True, (255, 255, 255))
        self.screen.blit(text, (10, 10))


    def _update_screen(self):
        # Update images on the screen, and flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.circle = pygame.draw.circle(self.screen, \
            self.settings.circle_color, self.settings.circle_pos, \
            self.settings.circle_radius, self.settings.circle_thickness)

        for particle in self.particles.sprites():
            particle.draw_trail()
        for particle in self.particles.sprites():
            particle.draw_particle()

        
        # Draw the buttons if the program is inactive
        if not self.settings.program_active:
            self.play_button.draw_button()

        # Display the total number of particle movements
        self._display_total()

        # Make the most recently drawn screen visible
        pygame.display.flip()



if __name__ == '__main__':
    # Make a program instance, and run the program
    sun = SunEnergy()
    sun.run_program()