import pygame
import random
import math

class Big_disc(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.original_image = self.image  # Keep a reference to the original unrotated image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # Movement stuff
        self.movement = False
        self.placement = False
        self.timer = 0
        self.stationary_disc = 0
        self.second_phase = False
        self.beginning_movement = True
        self.movement_speed = 4
        self.bouncing_speed = 4

        # Spinning stuff
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation_angle = 0  # Angle for visual spinning
        self.rotation_speed = 0  # Degrees to rotate per frame

        # Health stuff
        self.health = 50
        self.health_shown = False
        self.killed = False

        # Calculate velocity components from the angle
        self.velocity = [math.cos(self.angle) * self.bouncing_speed,
                         math.sin(self.angle) * self.bouncing_speed]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Stuff for pygame masks
        self.mask = pygame.mask.from_surface(self.image)

        # Killed boss stuff
        self.killed_timer = 0
        self.alpha = 0

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

    def draw(self, screen, left_eye_image, right_eye_image, font):
        # Update rect to match x and y
        self.rect.topleft = (self.x, self.y)

        # Rotate the visual image for spinning
        self.rotation_angle = (self.rotation_angle + self.rotation_speed) % 360
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation_angle)

        # Calculate the new blit position to center the rotated image
        rotated_rect = rotated_image.get_rect(center=self.rect.center)

        # Update the mask from the rotated image (Fixes collision issues)
        self.mask = pygame.mask.from_surface(rotated_image)

        # Blit the rotated image
        screen.blit(rotated_image, rotated_rect.topleft)
        screen.blit(left_eye_image, (self.x + 50, self.y + 40))
        screen.blit(right_eye_image, (self.x + 150, self.y + 40))

        max_health = 50  # Maximum health
        health_bar_width = 400  # Full width of the health bar
        health_bar_height = 15  # Height of the health bar
        health_bar_x = 448  # Positioning left of guy
        health_bar_y = 35  # Positioning above the guy
        current_health_width = (self.health / max_health) * health_bar_width  # Calculate current health width

        if self.health_shown:
            self.rotation_speed = 0.5
            # Draw the black border around the health bar
            pygame.draw.rect(screen, (0, 0, 0),
                             (health_bar_x - 5, health_bar_y - 5, health_bar_width + 10, health_bar_height + 10), 30)
            # Draw the health bar background (red for missing health)
            pygame.draw.rect(screen, (255, 255, 255), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
            # Draw the current health (green for remaining health)
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))

            # Boss name
            name_font = font
            name_text = name_font.render("Ironclad Washer", True, (0, 0, 0))
            screen.blit(name_text, (448, 3))

        '''# --- Debugging: Draw the mask ---
        # Create a surface from the mask to visualize it
        mask_surface = self.mask.to_surface()
        mask_surface.set_colorkey((0, 0, 0))  # Make black (transparent) pixels invisible

        # Draw the mask over the screen (with the same rotation and position)
        screen.blit(mask_surface, rotated_rect.topleft)'''