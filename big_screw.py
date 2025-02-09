import pygame
import math

class Big_Screw(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.original_image = self.image  # Keep the original image for rotation
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.movement = False
        self.placement = False
        self.firing = False
        self.firing_timer = 0
        self.stationary_timer = 0
        self.beginning_timer = 0
        self.movement_speed = 3  # Speed of the big Screw

        # Stuff for the phases
        self.phase_2 = False
        self.phase_2_timer = 0
        self.phase_3 = False
        self.phase_3_timer = 0
        self.opening_shown = True
        self.phase_2_stationary_timer = 0

        # Stuff for pygame masks
        self.mask = pygame.mask.from_surface(self.image)

        # Health stuff for the boss
        self.health = 50  # Default is 50
        self.hit_timer = 0
        self.health_shown = False

        # Screw dying
        self.killed = False
        self.alpha = 255  # Start with full opacity
        self.killed_alpha = 0  # Start with full opacity

        # Current rotation angle
        self.rotation_angle = 0

    def align_with_mouse(self, max_turn_degree=10):
        """
        Align the bottom point of the screw with the mouse, with a maximum turning degree limit.
        :param max_turn_degree: The maximum degrees the screw can turn in one frame.
        """
        mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position

        # Calculate the center of the screw
        screw_center_x = self.x + self.rect.width // 2
        screw_center_y = self.y + self.rect.height // 2

        # Calculate the target angle
        dx = mouse_pos[0] - screw_center_x
        dy = mouse_pos[1] - screw_center_y
        target_angle = math.degrees(math.atan2(dy, dx)) - 90  # Subtract 90 to align bottom point

        # Calculate the angle difference
        angle_difference = (target_angle - self.rotation_angle + 180) % 360 - 180  # Shortest angle difference

        # Clamp the angle difference to the max turning degree
        if angle_difference > max_turn_degree:
            angle_difference = max_turn_degree
        elif angle_difference < -max_turn_degree:
            angle_difference = -max_turn_degree

        # Update the current rotation angle
        self.rotation_angle += angle_difference

        # Rotate the image around its center
        self.image = pygame.transform.rotate(self.original_image, -self.rotation_angle)
        self.rect = self.image.get_rect(center=(screw_center_x, screw_center_y))

    def draw(self, screen, font):
        self.hit_timer += 1

        # Update the rect's center based on the sprite's position
        self.rect = self.image.get_rect(center=(self.x + self.rect.width // 2, self.y + self.rect.height // 2))

        # Update the mask to match the current image
        self.mask = pygame.mask.from_surface(self.image)

        # Draw the boss image
        if self.killed:
            self.image.set_alpha(self.alpha)  # Apply alpha transparency
            self.alpha -= 1  # Gradually reduce alpha
            if self.alpha <= 0:
                self.kill()  # Remove the sprite from the game
        screen.blit(self.image, self.rect.topleft)

        # Draw the health bar
        max_health = 50  # Maximum health
        health_bar_width = 400  # Full width of the health bar
        health_bar_height = 15  # Height of the health bar
        health_bar_x = 448  # Positioning left of guy
        health_bar_y = 35  # Positioning above the guy

        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

        # Calculate current health width
        current_health_width = (self.health / max_health) * health_bar_width

        if self.health_shown:
            # Draw the border around the health bar
            pygame.draw.rect(screen, (0, 0, 0),
                             (health_bar_x - 5, health_bar_y - 5, health_bar_width + 10, health_bar_height + 10), 30)

            # Draw the health bar background (red for missing health)
            pygame.draw.rect(screen, (255, 255, 255), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

            # Draw the current health (green for remaining health)
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))

            # Boss name
            name_font = font
            name_text = name_font.render("Screw Archmage", True, (0, 0, 0))
            screen.blit(name_text, (445, 3))