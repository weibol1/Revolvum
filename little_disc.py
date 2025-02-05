import pygame
import math
import random

class Little_disc(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.original_image = self.image  # Keep a reference to the original unrotated image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.movement = False
        self.timer = 0
        self.little_phase = False
        self.stationary_disc = 0
        self.movement_speed = 10  # Speed of the disc

        # spinning stuff
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation_angle = 0  # Angle for visual spinning
        self.rotation_speed = 5  # Degrees to rotate per frame

        # hitboxes
        self.mask = pygame.mask.from_surface(self.image)

        # Debugging display mask
        self.mask_image = self.mask.to_surface()

        # movement stuff
        self.velocity = [math.cos(self.angle) * self.movement_speed,
                         math.sin(self.angle) * self.movement_speed]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self):
        if not self.movement:
            return

        # Update the position of the disc based on its velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Bounce off the walls (room boundaries)
        if self.x <= 0 or self.x >= 1280 - self.width:
            self.velocity[0] = -self.velocity[0]  # Reverse horizontal direction

        if self.y <= 0 or self.y >= 720 - self.height:
            self.velocity[1] = -self.velocity[1]  # Reverse vertical direction

    def draw(self, screen):
        # hitbox setting stuff
        self.rect.topleft = (self.x, self.y)

        # Rotate the visual image for spinning
        self.rotation_angle = (self.rotation_angle + self.rotation_speed) % 360
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation_angle)

        # Calculate the new blit position to center the rotated image
        rotated_rect = rotated_image.get_rect(center=self.rect.center)

        # Update the mask for the rotated image (important)
        self.mask = pygame.mask.from_surface(rotated_image)

        # Draw the rotated image on screen
        screen.blit(rotated_image, rotated_rect.topleft)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

        '''# --- Debugging: Draw the mask ---
        # Create a surface from the mask to visualize it
        mask_surface = self.mask.to_surface()
        mask_surface.set_colorkey((0, 0, 0))  # Make black (transparent) pixels invisible

        # Draw the mask over the player at the same position
        screen.blit(mask_surface, rotated_rect.topleft)  # Corrected to match the rotated image'''