import pygame

class Hammer(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.original_image = image
        self.hitbox = pygame.Rect(self.x, self.y, 32, 32)
        self.movement = False
        self.movement_speed = 10
        self.firing = False
        self.intro_shown = True
        self.intro_wall_shown = True

        # stuff for pygame masks
        self.mask = pygame.mask.from_surface(self.image)

        #debugging display mask
        self.mask_image = self.mask.to_surface()

        # firing stuff
        self.firing_up = False
        self.firing_side = False
        self.firing_left = False
        self.firing_right = False
        self.firing = False
        self.firing_timer = 0

        # spinning for the image
        self.spinning = True
        self.angle = 0

    def move(self, pressed_key, hammer_sound, player_1_x, player_1_y, player_1_intro_x, player_1_intro_y, current_game_state, screen):
        self.firing_timer += 1

        # hammer firing the two sides
        if pressed_key[pygame.K_j] and self.firing_timer > 30 and not self.firing_up and not self.firing_right and not self.firing_side:
            hammer_sound.play()
            self.firing_side = True
            self.firing_timer = 0
            self.firing_left = True

        if pressed_key[pygame.K_l] and self.firing_timer > 30 and not self.firing_up and not self.firing_left and not self.firing_side:
            hammer_sound.play()
            self.firing_side = True
            self.firing_timer = 0
            self.firing_right = True

        if self.firing_right:
            self.draw(screen)
            self.x += self.movement_speed

        if self.firing_left:
            self.draw(screen)
            self.x -= self.movement_speed

        if self.x > 1280 or self.x < 0:
            self.firing_left = False
            self.firing_right = False
            self.firing_side = False
            self.x = player_1_x
            self.y = player_1_y
            if current_game_state == 'intro':
                self.x = player_1_intro_x
                self.y = player_1_intro_y

        # hammer firing up
        if pressed_key[pygame.K_i] and self.firing_timer > 30 and not self.firing_side and not self.firing_up:
            hammer_sound.play()
            self.firing_up = True
            self.firing_timer = 0

        if self.firing_up:
            self.draw(screen)
            self.y -= self.movement_speed

        if self.y <= 0:
            self.x, self.y = player_1_x, player_1_y
            if current_game_state == 'intro':
                self.x = player_1_intro_x
                self.y = player_1_intro_y
            self.firing_up = False

        # moving the hammer to the player x and y when updated
        if not self.firing_side and not self.firing_up:
            if self.x != player_1_x:
                self.x = player_1_x

            if self.y != player_1_y:
                self.y = player_1_y

            if current_game_state == 'intro':
                if self.x != player_1_intro_x:
                    self.x = player_1_intro_x

                if self.y != player_1_intro_y:
                    self.y = player_1_intro_y

        # spinning the hammer to hit the enemies
        self.angle += 5
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def draw(self, screen):
        # Update rect to match the new position (taking rotation into account)
        self.rect.topleft = (self.x, self.y)
        self.hitbox.x = self.x
        self.hitbox.y = self.y

        # Rotate the image around its center
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)

        # Update the mask for the rotated image (for accurate collision detection)
        self.mask = pygame.mask.from_surface(rotated_image)

        # Draw the rotated hammer image
        screen.blit(rotated_image, rotated_rect.topleft)

        '''# --- Debugging: Draw the mask ---
        # Create a surface from the mask to visualize it
        mask_surface = self.mask.to_surface()
        mask_surface.set_colorkey((0, 0, 0))  # Make black (transparent) pixels invisible

        # Draw the mask over the screen (with the same rotation and position)
        screen.blit(mask_surface, rotated_rect.topleft)'''