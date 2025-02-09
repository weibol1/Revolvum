import pygame
import random

class Saw_boss(pygame.sprite.Sprite):
    def __init__(self, x, y, image, blade_img):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.image2 = blade_img
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.movement_speed = 6

        # Beginning movement of the saw boss
        self.beginning_movement = True
        self.beginning_movement_timer = 0
        self.beginning_movement_speed = 18
        self.moving_right = True
        self.moving_left = False
        self.beginning_falling = False

        # Blade positioning
        self.pointing_right = True
        self.pointing_left = False

        # Phase variables
        self.phase_1 = True
        self.phase_1_timer = 0
        self.phase_2 = False
        self.phase_2_timer = 0
        self.first_time = True
        self.sfx_timer = 0

        # Phase 1 attack
        self.attacking = False
        self.phase_1_attack_timer = 0

        # Returning to position
        self.moving_position = False

        # Health variables
        self.health = 50
        self.hit_timer = 0
        self.health_shown = False

        # Death handling
        self.killed = False
        self.alpha = 0

        # Mask for accurate collisions
        self.update_hitbox()
        

    def update_hitbox(self):
        """Ensures the hitbox and mask update correctly every frame."""
        self.rect.topleft = (self.x, self.y)  # Update rect position
        self.mask = pygame.mask.from_surface(self.image)  # Regenerate mask

    def opening_movement(self):
        if self.moving_right:
            self.x += self.beginning_movement_speed
            if self.x > 1500:
                self.moving_right = False
                self.image = pygame.transform.flip(self.image, True, False)
                self.pointing_right = False
                self.pointing_left = True
                self.moving_left = True
                self.update_hitbox()  # Update hitbox after transformation

        if self.moving_left:
            self.x -= self.beginning_movement_speed
            if self.x < -401:
                self.moving_left = False
                self.y = -200
                self.x = 500
                position = random.randint(1, 2)
                if position == 1:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.pointing_right = True
                    self.pointing_left = False
                else:
                    self.pointing_left = True
                    self.pointing_right = False
                self.beginning_falling = True
                self.update_hitbox()  # Update hitbox after transformation

        if self.beginning_falling:
            self.y += 2
            if self.y >= 100:
                self.beginning_falling = False
                self.phase_1 = True
                self.beginning_movement = False
                self.health_shown = True

        self.update_hitbox()

    def main_menu_movement(self):
        self.beginning_movement_speed = 5
        if self.moving_right:
            self.x += self.beginning_movement_speed
            if self.x > 1500:
                self.moving_right = False
                self.image = pygame.transform.flip(self.image, True, False)
                self.pointing_right = False
                self.pointing_left = True
                self.moving_left = True
                self.update_hitbox()  # Update hitbox after transformation

        if self.moving_left:
            self.x -= self.beginning_movement_speed
            if self.x < -401:
                self.moving_right = True
                self.image = pygame.transform.flip(self.image, True, False)
                self.pointing_right = True
                self.pointing_left = False
                self.moving_left = False
                self.update_hitbox()  # Update hitbox after transformation

        self.update_hitbox()

    def draw(self, saw_blade_shown, screen, font):
        """Draws the boss and updates the hitbox each frame."""
        self.update_hitbox()
        self.hit_timer += 1

        # Draw the spinning blade
        if not saw_blade_shown:
            if self.pointing_right:
                screen.blit(self.image2, (self.x + 195, self.y + 35))
            else:
                screen.blit(self.image2, (self.x - 15, self.y + 35))

        # Draw the main boss image
        screen.blit(self.image, (self.x, self.y))

        # Debugging hitbox visualization (uncomment if needed)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

        # Draw health bar
        if self.health_shown:
            max_health = 50
            health_bar_width = 400
            health_bar_height = 15
            health_bar_x = 448
            health_bar_y = 35
            current_health_width = (self.health / max_health) * health_bar_width

            pygame.draw.rect(screen, (0, 0, 0), (health_bar_x - 5, health_bar_y - 5, health_bar_width + 10, health_bar_height + 10), 30)
            pygame.draw.rect(screen, (255, 255, 255), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
            pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, current_health_width, health_bar_height))

            # Draw boss name
            name_font = font
            name_text = name_font.render("Ripjaw", True, (0, 0, 0))
            screen.blit(name_text, (445, 3))