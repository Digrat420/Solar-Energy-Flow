import pygame.font

class Button:

    def __init__(self, sun_program, msg1, msg2, msg3, msg4, msg5):
        # Initialize button attributes
        self.screen = sun_program.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the buttons
        self.width, self.height = 290, 25
        self.button_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)

        # Build the buttons' rect objects and center them
        self.rect1 = pygame.Rect(0, 0, self.width, self.height)
        self.rect1.center = (self.screen_rect.centerx, \
            self.screen_rect.centery - 60)

        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
        self.rect2.center = (self.screen_rect.centerx, \
            self.screen_rect.centery - 30)

        self.rect3 = pygame.Rect(0, 0, self.width, self.height)
        self.rect3.center = (self.screen_rect.centerx, \
            self.screen_rect.centery)

        self.rect4 = pygame.Rect(0, 0, self.width, self.height)
        self.rect4.center = (self.screen_rect.centerx, \
            self.screen_rect.centery + 30)

        self.rect5 = pygame.Rect(0, 0, self.width, self.height)
        self.rect5.center = (self.screen_rect.centerx, \
            self.screen_rect.centery + 60)

        # The button messages need to be prepped only once
        self._prep_msg(msg1, msg2, msg3, msg4, msg5)


    def _prep_msg(self, msg1, msg2, msg3, msg4, msg5):
        # Turn msg into a rendered image and center text on the button
        self.msg1_image = self.font.render(msg1, True, self.text_color,\
            self.button_color)
        self.msg1_image_rect = self.msg1_image.get_rect()
        self.msg1_image_rect.center = self.rect1.center

        self.msg2_image = self.font.render(msg2, True, self.text_color,\
            self.button_color)
        self.msg2_image_rect = self.msg2_image.get_rect()
        self.msg2_image_rect.center = self.rect2.center

        self.msg3_image = self.font.render(msg3, True, self.text_color,\
            self.button_color)
        self.msg3_image_rect = self.msg3_image.get_rect()
        self.msg3_image_rect.center = self.rect3.center

        self.msg4_image = self.font.render(msg4, True, self.text_color,\
            self.button_color)
        self.msg4_image_rect = self.msg4_image.get_rect()
        self.msg4_image_rect.center = self.rect4.center

        self.msg5_image = self.font.render(msg5, True, self.text_color,\
            self.button_color)
        self.msg5_image_rect = self.msg5_image.get_rect()
        self.msg5_image_rect.center = self.rect5.center

    def draw_button(self):
        # Draw blank buttons and then draw messages
        self.screen.fill(self.button_color, self.rect1)
        self.screen.blit(self.msg1_image, self.msg1_image_rect)

        self.screen.fill(self.button_color, self.rect2)
        self.screen.blit(self.msg2_image, self.msg2_image_rect)

        self.screen.fill(self.button_color, self.rect3)
        self.screen.blit(self.msg3_image, self.msg3_image_rect)

        self.screen.fill(self.button_color, self.rect4)
        self.screen.blit(self.msg4_image, self.msg4_image_rect)

        self.screen.fill(self.button_color, self.rect5)
        self.screen.blit(self.msg5_image, self.msg5_image_rect)