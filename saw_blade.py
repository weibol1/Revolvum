import pygame

class Saw_blade(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # Phase 2 behavior
        self.blade_shown = False
        self.phase_2_stationary_timer = 0  # Timer for how long the blade remains still
        self.velocity_y = -10
        self.gravity = 0.5  # Gravity for downward motion
        self.bounce_velocity = -10  # Velocity when bouncing off the ground
        self.horizontal_speed = 10  # Speed for left/right movement
        self.bouncing = False
        self.moving_left = False
        self.moving_right = False

        # Reset movement position after its phase
        self.movement_speed = 5
        self.movement_position = False
        self.moving_position = False

        # Collision detection
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        # Ensure hitbox updates each frame
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

        # Draw the saw blade
        screen.blit(self.image, (self.x, self.y))

        # Debugging: Uncomment to visualize hitboxes
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)