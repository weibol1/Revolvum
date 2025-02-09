import pygame
import random

class Little_screw(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.original_image = image  # Store the original image to avoid permanent rotation
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.phase_1 = False
        self.phase_1_timer = 0
        self.movement_speed = 10  # Speed of the disc

        # Stuff for the firing of the screw to the left and right
        self.screw_side = random.randint(1, 2)
        self.firing_right = False
        self.firing_left = False
        self.firing_timer = 0

        # Rotation angle for this instance
        self.angle = 0  # Initial angle

        # Stuff for pygame masks
        self.mask = pygame.mask.from_surface(self.image)

    def rotate(self, angle):
        """Rotate the image by the specified angle."""
        self.angle = angle
        # Rotate the original image, and update the image and rect accordingly
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)  # Keep the position the same

        # Update the mask after rotation
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        self.rect.topleft = (self.x, self.y)

        # Update the mask before drawing (in case position changed)
        self.mask = pygame.mask.from_surface(self.image)

        screen.blit(self.image, self.rect.topleft)

        # Uncomment to see the mask rectangle for debugging
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)