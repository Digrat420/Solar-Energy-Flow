class Settings:
    # A class to store all the settings for Sun Energy program

    def __init__(self):
        # Initialize the program's static settings
        # Screen settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (10, 10, 120)
        self.frameratecap = 288000

        # Start the program in an inactive state
        self.program_active = False

        # Circle settings (the Sun)
        self.circle_pos = (250, 250)
        self.circle_radius = 100
        self.circle_color = (196, 180, 84)
        self.circle_thickness = 0
        # This last setting makes a solid circle

        # Particle settings
        self.particle_color = (255, 0, 0)
        self.trail_color = (20, 20, 20)
        self.particle_size = 5
        self.particles_allowed = 10

    def tiny_star(self):
        self.circle_radius = 25

    def small_star(self):
        self.circle_radius = 50

    def medium_star(self):
        self.circle_radius = 100

    def large_star(self):
        self.circle_radius = 200