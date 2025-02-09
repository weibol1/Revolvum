import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.original_image = image  # Store the original image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.hitbox = pygame.rect.Rect(self.x, self.y + 58, 32, 8)

        # Movement & physics
        self.movement = False
        self.movement_speed = 4
        self.velocity_x = 0
        self.acceleration = 0.5
        self.friction = 0.8  # Smooth deceleration

        # Jumping & Gravity
        self.falling = True
        self.is_jumping = False
        self.jump_count = 30
        self.gravity = 13  # Falling speed

        # Dash stuff
        self.dashing = False
        self.dash_timer = 0
        self.last_movement = 'none'
        self.dash_velocity = 0
        self.dash_duration = 6
        self.dash_speed = 20
        self.can_dash = True  # Prevents midair spam dashing

        # intro stuff for the game
        self.intro_wall_shown2 = True
        self.text1 = True
        self.text2 = False
        self.text3 = False

        # Health
        self.health = 4
        self.hit_timer = 0

        # Game over
        self.game_over = False

        # Pygame mask (for pixel-perfect collision)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, pressed_key, jump_sound, dash_sound):
        """Handles player movement, jumping, and dashing."""
        if not self.movement:
            return

        self.hit_timer += 1
        self.dash_timer += 1

        # Left & Right Movement
        if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration
            self.last_movement = 'left'
        elif pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration
            self.last_movement = 'right'
        else:
            # Apply friction to slow down
            self.velocity_x *= self.friction

        # Cap velocity
        self.velocity_x = max(-self.movement_speed, min(self.velocity_x, self.movement_speed))
        self.x += self.velocity_x

        # Jumping
        if not self.is_jumping and (pressed_key[pygame.K_w] or pressed_key[pygame.K_UP] or pressed_key[pygame.K_SPACE]):
            jump_sound.play()
            self.is_jumping = True
            self.falling = False
            self.jump_count = 30

        if self.is_jumping:
            if self.jump_count >= -30:
                neg = 1 if self.jump_count > 0 else -1
                self.y -= (self.jump_count ** 2) * 0.020 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.falling = True
                self.jump_count = 30

        # Gravity (falling)
        if self.falling:
            self.y += self.gravity

        # Dashing
        if pressed_key[pygame.K_LSHIFT] and self.dash_timer >= 120 and not self.dashing and self.can_dash:
            dash_sound.play()
            self.dashing = True
            self.dash_timer = 0
            self.can_dash = False  # Prevents multiple dashes before touching the ground
            self.dash_velocity = self.dash_speed if self.last_movement == 'right' else -self.dash_speed

        if self.dashing:
            if self.dash_duration > 0:
                self.x += self.dash_velocity
                self.dash_duration -= 1
            else:
                self.dashing = False
                self.dash_duration = 6
                self.dash_velocity = 0

        # Prevent falling through the ground
        if self.y >= 540:
            self.y = 540
            self.falling = False
            self.can_dash = True  # Reset dash when touching the ground

        # Prevent going out of bounds
        self.x = max(0, min(self.x, 1248))

    def draw(self, screen, health_states, dash_states):
        """Updates player state and draws it on the screen."""
        # Update the position of the player's rectangle and hitbox
        self.rect.topleft = (self.x, self.y)
        self.hitbox.topleft = (self.x, self.y + 58)

        # Update mask for collision
        self.mask = pygame.mask.from_surface(self.image)

        # Draw health
        #health_states = [health_full, health1, health2, health3, health_empty]
        screen.blit(health_states[max(0, 4 - self.health)], (20, 15))

        if self.dash_timer <= 29:
            screen.blit(dash_states[0], (150, 15))

        if self.dash_timer >= 30:
            screen.blit(dash_states[1], (150, 15))

        if self.dash_timer >= 60:
            screen.blit(dash_states[2], (150, 15))

        if self.dash_timer >= 90:
            screen.blit(dash_states[3], (150, 15))

        if self.dash_timer >= 120:
            screen.blit(dash_states[4], (150, 15))

        # Draw player
        screen.blit(self.image, (self.x, self.y))

        '''# --- Debugging: Draw the mask ---
        # Create a surface from the mask to visualize it
        mask_surface = self.mask.to_surface()
        mask_surface.set_colorkey((0, 0, 0))  # Make black (transparent) pixels invisible

        # Draw the mask over the player at the same position
        screen.blit(mask_surface, self.rect.topleft)'''