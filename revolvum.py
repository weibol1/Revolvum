import pygame
import random
import math
import webbrowser
import sys
import os
import button
import little_disc
import big_disc
import big_screw
import little_screw
from pygame import mixer

def resource_path(relative_path):
    """ Get absolute path to resource, works for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller's temporary directory
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()
mixer.init()
screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Revolvum")

# scene image loading
arena_1 = pygame.image.load(resource_path("assets/img/boss_arena_1.png")).convert()
arena_1 = pygame.transform.scale(arena_1, (1280, 720))

# img load
disc_boss_img = pygame.image.load(resource_path("assets/img/washer_boss.png")).convert_alpha()
disc_boss_img = pygame.transform.scale(disc_boss_img, (225, 225))

disc_eye_right_img = disc_eye_left_img = pygame.image.load(resource_path("assets/img/washer_eye.png")).convert_alpha()
disc_eye_right_img = pygame.transform.scale(disc_eye_right_img, (24, 24))
disc_eye_left_img = pygame.transform.scale(disc_eye_left_img, (24, 24))
disc_eye_left_img = pygame.transform.flip(disc_eye_left_img, True, False)

hammer_img = pygame.image.load(resource_path("assets/img/hammer.png")).convert_alpha()
hammer_img = pygame.transform.scale(hammer_img, (32, 32))

little_disc_img = pygame.image.load(resource_path("assets/img/little_washer.png")).convert_alpha()
little_disc_img = pygame.transform.scale(little_disc_img, (75, 75))

player_img = pygame.image.load(resource_path("assets/img/player.png")).convert_alpha()
player_img = pygame.transform.scale(player_img, (32, 64))

screw_boss_img = pygame.image.load(resource_path("assets/img/screw_boss.png")).convert_alpha()
screw_boss_img = pygame.transform.scale(screw_boss_img, (90, 195))

screw_entrance_img = pygame.image.load(resource_path("assets/img/screw_entrance.png")).convert_alpha()
screw_entrance_img = pygame.transform.scale(screw_entrance_img, (224, 224))

screw_img = pygame.image.load(resource_path("assets/img/generic_screw.png")).convert_alpha()
screw_img = pygame.transform.scale(screw_img, (36, 58))

saw_shell_img = pygame.image.load(resource_path("assets/img/saw_boss_shell.png")).convert_alpha()
saw_shell_img = pygame.transform.scale(saw_shell_img, (290, 120))

saw_img = pygame.image.load(resource_path("assets/img/saw_boss_blade.png")).convert_alpha()
saw_img = pygame.transform.scale(saw_img, (110, 110))

game_over_img = pygame.image.load(resource_path("assets/img/game_over_screen.png")).convert()
game_over_img = pygame.transform.scale(game_over_img, (1280, 720))
game_over_img.set_alpha(200)

victory_img = pygame.image.load(resource_path("assets/img/victory_screen.png")).convert_alpha()
victory_img = pygame.transform.scale(victory_img, (504, 84))
victory_img.set_alpha(0)

# health and dash image loading
health_full = pygame.image.load(resource_path("assets/img/health_full.png")).convert_alpha()
health_full = pygame.transform.scale(health_full, (96, 96))

health1 = pygame.image.load(resource_path("assets/img/health_1.png")).convert_alpha()
health1 = pygame.transform.scale(health1, (96, 96))

health2 = pygame.image.load(resource_path("assets/img/health_2.png")).convert_alpha()
health2 = pygame.transform.scale(health2, (96, 96))

health3 = pygame.image.load(resource_path("assets/img/health_3.png")).convert_alpha()
health3 = pygame.transform.scale(health3, (96, 96))

health_empty = dash_empty = pygame.image.load(resource_path("assets/img/health_empty.png")).convert_alpha()
health_empty = pygame.transform.scale(health_empty, (96, 96))
dash_empty = pygame.transform.scale(dash_empty, (96, 96))

dash_full = pygame.image.load(resource_path("assets/img/dash_full.png")).convert_alpha()
dash_full = pygame.transform.scale(dash_full, (96, 96))

dash1 = pygame.image.load(resource_path("assets/img/dash_1.png")).convert_alpha()
dash1 = pygame.transform.scale(dash1, (96, 96))

dash2 = pygame.image.load(resource_path("assets/img/dash_2.png")).convert_alpha()
dash2 = pygame.transform.scale(dash2, (96, 96))

dash3 = pygame.image.load(resource_path("assets/img/dash_3.png")).convert_alpha()
dash3 = pygame.transform.scale(dash3, (96, 96))

# main menu image loading
start_button = pygame.image.load(resource_path("assets/img/start_button.png")).convert_alpha()
start_button = pygame.transform.scale(start_button, (212, 56))

options_button = pygame.image.load(resource_path("assets/img/options_button.png")).convert_alpha()
options_button = pygame.transform.scale(options_button, (280, 68))

credits_button = pygame.image.load(resource_path("assets/img/credits_button.png")).convert_alpha()
credits_button = pygame.transform.scale(credits_button, (276, 56))

exit_button = pygame.image.load(resource_path("assets/img/exit_button.png")).convert_alpha()
exit_button = pygame.transform.scale(exit_button, (148, 56))

title = pygame.image.load(resource_path("assets/img/title.png")).convert_alpha()
title = pygame.transform.scale(title, (672, 112))

# options menu loading images

left_arrow = right_arrow = pygame.image.load(resource_path("assets/img/left_arrow.png")).convert_alpha()
right_arrow = pygame.transform.rotate(right_arrow, 180)
left_arrow = pygame.transform.scale(left_arrow, (80, 130))
right_arrow = pygame.transform.scale(right_arrow, (80, 130))

apply_button = pygame.image.load(resource_path("assets/img/apply_button.png")).convert_alpha()
apply_button = pygame.transform.scale(apply_button, (200, 68))

# social links
discord_img = pygame.image.load(resource_path("assets/img/discord_logo.png")).convert_alpha()
discord_img = pygame.transform.scale(discord_img, (75, 57))

youtube_img = pygame.image.load(resource_path("assets/img/youtube_icon.png")).convert_alpha()
youtube_img = pygame.transform.scale(youtube_img, (75, 53))

ghastly_img = pygame.image.load(resource_path("assets/img/ghastly_games_logo.png")).convert_alpha()
ghastly_img = pygame.transform.scale(ghastly_img, (75, 77))

# intro area stuff
intro_area = pygame.image.load(resource_path("assets/img/intro_area.png")).convert()
intro_area = pygame.transform.scale(intro_area, (1280, 720))

intro_target = pygame.image.load(resource_path("assets/img/intro_target.png")).convert_alpha()
intro_target = pygame.transform.scale(intro_target, (32, 64))

intro_stone = pygame.image.load(resource_path("assets/img/hammer_stone.png")).convert_alpha()
intro_stone = pygame.transform.scale(intro_stone, (128, 56))

interact = pygame.image.load(resource_path("assets/img/interact.png")).convert_alpha()
interact = pygame.transform.scale(interact, (54, 42))

traffic_cone = pygame.image.load(resource_path("assets/img/traffic_cone.png")).convert_alpha()
traffic_cone = pygame.transform.scale(traffic_cone, (44, 64))

intro_sign = pygame.image.load(resource_path("assets/img/intro_sign.png")).convert_alpha()
intro_sign = pygame.transform.scale(intro_sign, (61, 78))

caution = pygame.image.load(resource_path("assets/img/caution.png")).convert_alpha()
caution = pygame.transform.scale(caution, (78, 48))

# sound effects that are loaded before the main game stuff
dash_sound = pygame.mixer.Sound(resource_path('assets/sounds/dash.ogg'))
hammer_sound = pygame.mixer.Sound(resource_path('assets/sounds/hammer.ogg'))
jump_sound = pygame.mixer.Sound(resource_path('assets/sounds/jump.ogg'))

# setting the icon for the game
pygame.display.set_icon(little_disc_img)

# classes

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = player_img
        self.original_image = player_img  # Store the original image
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
        self.game_over_timer = 0

        # Pygame mask (for pixel-perfect collision)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        """Handles player movement, jumping, and dashing."""
        if not self.movement:
            return

        self.hit_timer += 1
        self.dash_timer += 1

        # Left & Right Movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration
            self.last_movement = 'left'
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration
            self.last_movement = 'right'
        else:
            # Apply friction to slow down
            self.velocity_x *= self.friction

        # Cap velocity
        self.velocity_x = max(-self.movement_speed, min(self.velocity_x, self.movement_speed))
        self.x += self.velocity_x

        # Jumping
        if not self.is_jumping and (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]):
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
        if keys[pygame.K_LSHIFT] and self.dash_timer >= 120 and not self.dashing and self.can_dash:
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

    def draw(self):
        """Updates player state and draws it on the screen."""
        # Update the position of the player's rectangle and hitbox
        self.rect.topleft = (self.x, self.y)
        self.hitbox.topleft = (self.x, self.y + 58)

        # Update mask for collision
        self.mask = pygame.mask.from_surface(self.image)

        # Draw health
        health_states = [health_full, health1, health2, health3, health_empty]
        screen.blit(health_states[max(0, 4 - self.health)], (20, 15))

        if self.dash_timer <= 29:
            screen.blit(dash_empty, (150, 15))

        if self.dash_timer >= 30:
            screen.blit(dash3, (150, 15))

        if self.dash_timer >= 60:
            screen.blit(dash2, (150, 15))

        if self.dash_timer >= 90:
            screen.blit(dash1, (150, 15))

        if self.dash_timer >= 120:
            screen.blit(dash_full, (150, 15))

        # Draw player
        screen.blit(self.image, (self.x, self.y))

        '''# --- Debugging: Draw the mask ---
        # Create a surface from the mask to visualize it
        mask_surface = self.mask.to_surface()
        mask_surface.set_colorkey((0, 0, 0))  # Make black (transparent) pixels invisible

        # Draw the mask over the player at the same position
        screen.blit(mask_surface, self.rect.topleft)'''

class Saw_boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = saw_shell_img
        self.image2 = saw_img
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

    def draw(self):
        """Draws the boss and updates the hitbox each frame."""
        self.update_hitbox()
        self.hit_timer += 1

        # Draw the spinning blade
        if not saw_blade1.blade_shown:
            if self.pointing_right:
                screen.blit(self.image2, (self.x + 195, self.y + 35))
            else:
                screen.blit(self.image2, (self.x - 15, self.y + 35))

        # Draw the main boss image
        screen.blit(self.image, (self.x, self.y))

        # Debugging hitbox visualization (uncomment if needed)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

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
            name_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 24)
            name_text = name_font.render("Ripjaw", True, (0, 0, 0))
            screen.blit(name_text, (445, 3))

class Saw_blade(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = saw_img
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

    def draw(self):
        # Ensure hitbox updates each frame
        self.rect.topleft = (self.x, self.y)
        self.mask = pygame.mask.from_surface(self.image)

        # Draw the saw blade
        screen.blit(self.image, (self.x, self.y))

        # Debugging: Uncomment to visualize hitboxes
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Hammer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = hammer_img
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.original_image = hammer_img
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

    def move(self):
        self.firing_timer += 1

        # hammer firing the two sides
        if keys[pygame.K_j] and self.firing_timer > 30 and not self.firing_up and not self.firing_right and not self.firing_side:
            hammer_sound.play()
            self.firing_side = True
            self.firing_timer = 0
            self.firing_left = True

        if keys[pygame.K_l] and self.firing_timer > 30 and not self.firing_up and not self.firing_left and not self.firing_side:
            hammer_sound.play()
            self.firing_side = True
            self.firing_timer = 0
            self.firing_right = True

        if self.firing_right:
            hammer_1.draw()
            self.x += self.movement_speed

        if self.firing_left:
            hammer_1.draw()
            self.x -= self.movement_speed

        if self.x > 1280 or self.x < 0:
            self.firing_left = False
            self.firing_right = False
            self.firing_side = False
            self.x = player_1.x
            self.y = player_1.y
            if game_state.state == 'intro':
                self.x = player_1_intro.x
                self.y = player_1_intro.y

        # hammer firing up
        if keys[pygame.K_i] and self.firing_timer > 30 and not self.firing_side and not self.firing_up:
            hammer_sound.play()
            self.firing_up = True
            self.firing_timer = 0

        if self.firing_up:
            hammer_1.draw()
            self.y -= self.movement_speed

        if self.y <= 0:
            self.x, self.y = player_1.x, player_1.y
            if game_state.state == 'intro':
                self.x = player_1_intro.x
                self.y = player_1_intro.y
            self.firing_up = False

        # moving the hammer to the player x and y when updated
        if not self.firing_side and not self.firing_up:
            if self.x != player_1.x:
                self.x = player_1.x

            if self.y != player_1.y:
                self.y = player_1.y

            if game_state.state == 'intro':
                if self.x != player_1_intro.x:
                    self.x = player_1_intro.x

                if self.y != player_1_intro.y:
                    self.y = player_1_intro.y

        # spinning the hammer to hit the enemies
        self.angle += 5
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def draw(self):
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

class Options_references(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # controller and keyboard stuff
        self.keyboardcontrols = True
        self.controllercontrols = False
        self.noconshown = False

        # windowed and fullscreen
        self.windowedshown = True
        self.fullscreenshown = False

        # volume
        self.volume = 25

        # timer for the links
        self.link_timer = 0

        # timer for the ending of bosses to the next one
        self.boss_countdown = 3
        self.boss_countdown_timer = 0

        # game over timer
        self.game_over_num = 3
        self.game_over_timer = 0

class Controller_references(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.a_index = 0
        self.b_index = 1
        self.x_index = 2
        self.y_index = 3
        self.pause_index = 7
        self.b_timer = 0

# functions
def game_over_func():

    if player_1.game_over:
        hammer_1.firing_up = False
        hammer_1.firing_left = False
        hammer_1.firing_right = False
        hammer_1.firing_side = False
        player_1.movement = False
        player_1.is_jumping = False
        if player_1.game_over_timer < 240:
            screen.blit(game_over_img, (0, 0))

            game_over_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 144)
            gameover_text = game_over_font.render("Game Over", True, (255, 255, 255))
            countdown1 = game_over_font.render(f'{options_reference.game_over_num}', True, (255, 255, 255))
            screen.blit(gameover_text, (360, 270))
            screen.blit(countdown1, (630, 400))

            options_reference.game_over_timer += 1
            if options_reference.game_over_timer >= 60:
                options_reference.game_over_num -= 1
                options_reference.game_over_timer = 0

    if player_1.game_over_timer >= 240:
        player_1.x = 100
        player_1.y = 540
        player_1.game_over_timer = 0
        player_1.game_over = False
        options_reference.game_over_num = 6
        options_reference.game_over_timer = 0
        player_1.health = 4
        player_1.movement = True

class GameState:
    def __init__(self):
        self.state = 'level2'
        self.music_playing = False
        self.current_music = None  # Track the currently playing music
        self.intro_played = False  # Flag to track if intro music has been played

        # Loading the music for the bosses
        self.boss1_music = resource_path('assets/sounds/boss1.ogg')  # Store the path to the music file
        self.boss2_music = resource_path('assets/sounds/boss2.ogg')  # Store the path to the music file
        self.boss3_music = resource_path('assets/sounds/boss3.ogg')  # Store the path to the music file
        self.tutorial_music = resource_path('assets/sounds/tutorial.ogg')  # Store the path to the music file
        self.intro_music = resource_path('assets/sounds/intro.ogg')  # Store the path to the intro music file
        self.intermission_1 = resource_path('assets/sounds/intermission_1.ogg')
        self.intermission_2 = resource_path('assets/sounds/intermission_2.ogg')

        # Loading the sound effects
        self.target_sound = pygame.mixer.Sound(resource_path('assets/sounds/targethit.ogg'))
        self.lightning_sound = pygame.mixer.Sound(resource_path('assets/sounds/thunder.ogg'))
        self.player_hit = pygame.mixer.Sound(resource_path('assets/sounds/player_hit.ogg'))
        self.enemy_hit = pygame.mixer.Sound(resource_path('assets/sounds/enemy_hurt.ogg'))
        self.enemy_hit2 = pygame.mixer.Sound(resource_path('assets/sounds/enemy_hurt2.ogg'))
        self.enemy_hit3 = pygame.mixer.Sound(resource_path('assets/sounds/enemy_hurt3.ogg'))
        self.screw_fire = pygame.mixer.Sound(resource_path('assets/sounds/screwfire.ogg'))
        self.saw_left = pygame.mixer.Sound(resource_path('assets/sounds/saw_left.ogg'))
        self.saw_right = pygame.mixer.Sound(resource_path('assets/sounds/saw_right.ogg'))

    def play_music(self, music_file):
        if self.current_music != music_file:
            pygame.mixer.music.stop()  # Stop the current music
            pygame.mixer.music.load(music_file)  # Load the new music
            pygame.mixer.music.play(-1)  # Play the new music in a loop
            self.current_music = music_file  # Update the currently playing music
            self.music_playing = True  # Set the flag to indicate music is playing

    def single_play(self, music_file):
        if self.current_music != music_file:
            pygame.mixer.music.stop()  # Stop the current music
            pygame.mixer.music.load(music_file)  # Load the new music
            pygame.mixer.music.play(1)  # Play the new music in a loop
            self.current_music = music_file  # Update the currently playing music
            self.music_playing = True  # Set the flag to indicate music is playing

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None
        self.music_playing = False

    def mainmenu(self):
        global running
        screen.fill((20, 20, 20))

        # Set volume for music and sound effects
        mixer.music.set_volume(options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.target_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.player_hit, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.lightning_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.saw_right, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit2, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.screw_fire, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.saw_left, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit3, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(dash_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(hammer_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(jump_sound, options_reference.volume / 100)
        self.single_play(self.intro_music)

        # blitting the bosses
        big_disc_main_menu.draw(screen, disc_eye_left_img, disc_eye_right_img, pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 24))
        big_disc_main_menu.movement = True
        big_disc_main_menu.move()

        bigscrew_main_menu.draw(screen, pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 24))
        bigscrew_main_menu.align_with_mouse()

        saw_boss_main_menu.draw()
        saw_boss_main_menu.main_menu_movement()

        # blitting the title image
        screen.blit(title, (350, 20))

        # main menu buttons
        if start_button_menu.draw(screen):
            self.state = 'intro'

        if options_button_menu.draw(screen):
            self.state = 'optionsmenu'

        if credits_button_menu.draw(screen):
            self.state = 'creditsmenu'

        if exit_button_menu.draw(screen):
            running = False

        # buttons to the different links
        options_reference.link_timer += 1

        if youtube_button.draw(screen) and options_reference.link_timer >= 5:
            webbrowser.open("https://www.youtube.com/@GhastlyGamez")
            options_reference.link_timer = 0

        if discord_button.draw(screen) and options_reference.link_timer >= 5:
            webbrowser.open("https://discord.gg/jB7gUKPDK7")
            options_reference.link_timer = 0

        if website_button.draw(screen) and options_reference.link_timer >= 5:
            webbrowser.open("https://www.ghastlygames.net")
            options_reference.link_timer = 0

    def creditsmenu(self):
        screen.fill((20, 20, 20))

        # font & text
        credits_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 48)
        esc_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 72)
        title_text = esc_font.render("Revolvum", True, (255, 255, 255))
        credit2_text = credits_font.render('Team Members:', True, (255, 255, 255))
        credit3_text = credits_font.render('Lead Programmer & Art Designer: Corey Stuckey', True, (255, 255, 255))
        credit4_text = credits_font.render('Assistant Developer & Consultant: woogotheboogo', True, (255, 255, 255))
        credit5_text = credits_font.render('Audio Design: Crusty Trayson', True, (255, 255, 255))
        credit6_text = credits_font.render('Sound Design: Jakeb Ranew', True, (255, 255, 255))
        credit7_text = esc_font.render('Press [ESC] to Exit', True, (255, 255, 255))

        # blitting normal credits
        screen.blit(title_text, (100, 50))
        screen.blit(credit2_text, (100, 150))
        screen.blit(credit3_text, (100, 225))
        screen.blit(credit4_text, (100, 300))
        screen.blit(credit5_text, (100, 375))
        # screen.blit(credit6_text, (100, 450))
        screen.blit(credit7_text, (400, 625))

        if keys[pygame.K_ESCAPE]:
            self.state = 'mainmenu'

    def optionsmenu(self):
        global screen
        screen.fill((20, 20, 20))

        # music stuff for the game
        mixer.music.set_volume(options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.target_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.player_hit, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.lightning_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.saw_right, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit2, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.screw_fire, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.saw_left, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit3, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(dash_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(hammer_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(jump_sound, options_reference.volume / 100)

        # timers
        controller_reference.b_timer += 1

        # text for the options menu
        esc_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 72)
        credit7_text = esc_font.render('Press [ESC] to Exit', True, (255, 255, 255))
        credit7controler_text = esc_font.render('Press     to Exit', True, (255, 255, 255))

        volume_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 72)
        volume_text = volume_font.render(f'Volume: {options_reference.volume}', True, (255, 255, 255))

        windowed_text = esc_font.render('Windowed', True, (255, 255, 255))
        fullscreen_text = esc_font.render('Fullscreen', True, (255, 255, 255))

        # controls for keyboard
        controls_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 48)
        controls1key = controls_font.render('[J] or [L] : To Shoot left or right', True, (255, 255, 255))
        controls2key = controls_font.render('[I] : To Shoot Up', True, (255, 255, 255))
        controls3key = controls_font.render('[A] & [D] or [LEFT-ARROW] & [RIGHT-ARROW] : To Move', True, (255, 255, 255))
        controls4key = controls_font.render('[E] : To Interact', True, (255, 255, 255))
        controls5key = controls_font.render('[SPACE], [W] or [UP-ARROW] : To Jump', True, (255, 255, 255))
        controls6key = controls_font.render('[Shift] : To Dash', True, (255, 255, 255))

        # main code
        screen.blit(volume_text, (800, 360))
        screen.blit(controls1key, (10, 0))
        screen.blit(controls2key, (10, 50))
        screen.blit(controls3key, (10, 100))
        screen.blit(controls4key, (10, 150))
        screen.blit(controls5key, (10, 200))
        screen.blit(controls6key, (10, 250))
        screen.blit(credit7_text, (350, 630))

        # fullscreen and windowed options along with text
        if left_button2.draw(screen):
            options_reference.fullscreenshown = False
            options_reference.windowedshown = True

        if right_button2.draw(screen):
            options_reference.windowedshown = False
            options_reference.fullscreenshown = True

        if options_reference.windowedshown:
            screen.blit(windowed_text, (210, 370))
        if options_reference.fullscreenshown:
            screen.blit(fullscreen_text, (195, 370))

        # changing volume and max limits
        if options_reference.volume > 100:
            options_reference.volume = 100
        if options_reference.volume < 0:
            options_reference.volume = 0

        if left_button3.draw(screen) and controller_reference.b_timer >= 8:
            controller_reference.b_timer = 0
            options_reference.volume -= 1

        if right_button3.draw(screen) and controller_reference.b_timer >= 8:
            controller_reference.b_timer = 0
            options_reference.volume += 1

        # apply button for the changing of display
        if applybut.draw(screen) and controller_reference.b_timer >= 60:
            controller_reference.b_timer = 0
            if options_reference.fullscreenshown:
                screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
            if options_reference.windowedshown:
                screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)

        if options_reference.keyboardcontrols and keys[pygame.K_ESCAPE]:
            controller_reference.b_timer = 0
            self.state = 'mainmenu'

    def intro(self):
        screen.fill((20, 20, 20))
        screen.blit(intro_area, (0, 0))

        # music stuff
        pygame.mixer.music.set_volume(options_reference.volume / 100)
        game_state.play_music(self.tutorial_music)

        # text for the instructions
        instructions_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 36)
        instructions_text1 = instructions_font.render('Press [W] or [Space] to Jump!', True, (0, 0, 0))
        instructions_text2 = instructions_font.render('Use [A] & [D] to move', True, (0, 0, 0))
        instructions_text3 = instructions_font.render('Pickup the Hammer and use', True, (0, 0, 0))
        instructions_text4 = instructions_font.render('[i], [j], & [l] to shoot', True, (0, 0, 0))
        instructions_text5 = instructions_font.render('Press [Shift] to dash in', True, (0, 0, 0))
        instructions_text6 = instructions_font.render('the last direction you moved.', True, (0, 0, 0))
        instructions_text7 = instructions_font.render('Dash past the traffic cone!', True, (0, 0, 0))

        # blitting the introsign
        screen.blit(intro_sign, (1100, 525))

        # setting the text to the screen with the player x
        if player_1_intro.x >= 150 and not player_1_intro.text3:
            player_1_intro.text1 = False
            player_1_intro.text2 = True

        if player_1_intro.x >= 760:
            player_1_intro.text2 = False
            player_1_intro.text3 = True

        if player_1_intro.x <= 520:
            player_1_intro.dash_timer = 0

        if player_1_intro.x >= 1100:
            self.state = 'level1'

        if player_1_intro.text1:
            screen.blit(instructions_text1, (80, 300))
            screen.blit(instructions_text2, (20, 200))

        if player_1_intro.text2:
            screen.blit(instructions_text3, (350, 300))
            screen.blit(instructions_text4, (400, 400))

        if player_1_intro.text3:
            screen.blit(instructions_text5, (750, 200))
            screen.blit(instructions_text6, (800, 300))
            screen.blit(instructions_text7, (850, 400))

        # blitting the objects to screen
        screen.blit(intro_target, (650, 540))
        screen.blit(intro_stone, (225, 547))
        if hammer_1.intro_shown:
            screen.blit(hammer_img, (270, 510))

        # drawing player and early assignments
        player_1_intro.draw()
        player_1_intro.movement = True

        hammer_1.firing_timer += 1

        # hitboxes for the platforms and the target
        box1top = pygame.Rect(100, 470, 116, 5)
        box1bottomleft = pygame.Rect(100, 480, 40, 150)
        box1bottomright = pygame.Rect(178, 480, 40, 150)

        box2top = pygame.Rect(705, 470, 116, 5)
        box2bottomleft = pygame.Rect(705, 480, 40, 150)
        box2bottomright = pygame.Rect(780, 480, 40, 150)

        hammer_rect = pygame.Rect(220, 550, 128, 56)
        wall_rect = pygame.Rect(520, 220, 30, 400)
        target_rect = pygame.Rect(650, 540, 32, 65)
        wall2_rect = pygame.Rect(900, 220, 15, 400)

        # Check for collision using the overlap method
        if hammer_1.intro_wall_shown:
            screen.blit(traffic_cone, (520, 538))

        if player_1_intro.intro_wall_shown2:
            screen.blit(traffic_cone, (900, 538))

        if player_1_intro.x >= 920:
            player_1_intro.intro_wall_shown2 = False

        if hammer_1.hitbox.colliderect(target_rect) and hammer_1.intro_wall_shown:
            self.target_sound.play()
            hammer_1.intro_wall_shown = False
            hammer_1.firing_timer = 0
            hammer_1.x = player_1_intro.x
            hammer_1.y = player_1_intro.y
            hammer_1.firing_up = False
            hammer_1.firing_left = False
            hammer_1.firing_right = False
            hammer_1.firing_side = False

        # collisions for the sides of the platforms
        if player_1_intro.hitbox.colliderect(box1bottomleft):
            player_1_intro.x = 70

        if player_1_intro.hitbox.colliderect(box1bottomright):
            player_1_intro.x = 220

        if player_1_intro.hitbox.colliderect(box2bottomleft):
            player_1_intro.x = 670

        if player_1_intro.hitbox.colliderect(box2bottomright):
            player_1_intro.x = 820

        # collision with the invisible wall
        if player_1_intro.hitbox.colliderect(wall_rect) and hammer_1.intro_wall_shown:
            player_1_intro.x = 490

        # collision with the invisible wall 2
        if player_1_intro.hitbox.colliderect(wall2_rect) and player_1_intro.intro_wall_shown2 and not player_1_intro.dashing:
            player_1_intro.x = 870

        # collision for picking up the hammer
        if player_1_intro.hitbox.colliderect(hammer_rect) and hammer_1.intro_shown:
            screen.blit(interact,(player_1_intro.x - 10, player_1_intro.y - 75))
            if keys[pygame.K_e]:
                hammer_1.intro_shown = False

        # Check if player is standing on the box
        if player_1_intro.hitbox.colliderect(box1top):
            player_1_intro.is_jumping = False
            player_1_intro.y = box1top.top - 70  # Adjust player's position to stand on the platform
            if not player_1_intro.is_jumping:
                if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    jump_sound.play()
                    player_1_intro.is_jumping = True
                    player_1_intro.falling = False
                    player_1_intro.jump_count = 30  # Reset jump count for a new jump
            else:
                if player_1_intro.jump_count >= -30:
                    neg = 1
                    if player_1_intro.jump_count < 0:
                        neg = -1

                    player_1_intro.y -= (player_1_intro.jump_count ** 2) * 0.020 * neg
                    player_1_intro.jump_count -= 1

                else:
                    player_1_intro.is_jumping = False
                    player_1_intro.falling = True
                    player_1_intro.jump_count = 30
        else:
            if not player_1_intro.is_jumping:  # Only set falling to True if not jumping
                player_1_intro.falling = True

        if player_1_intro.hitbox.colliderect(box2top):
            player_1_intro.is_jumping = False
            player_1_intro.y = box2top.top - 70  # Adjust player's position to stand on the platform
            if not player_1_intro.is_jumping:
                if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    jump_sound.play()
                    player_1_intro.is_jumping = True
                    player_1_intro.falling = False
                    player_1_intro.jump_count = 30  # Reset jump count for a new jump
            else:
                if player_1_intro.jump_count >= -30:
                    neg = 1
                    if player_1_intro.jump_count < 0:
                        neg = -1

                    player_1_intro.y -= (player_1_intro.jump_count ** 2) * 0.020 * neg
                    player_1_intro.jump_count -= 1

                else:
                    player_1_intro.is_jumping = False
                    player_1_intro.falling = True
                    player_1_intro.jump_count = 30
        else:
            if not player_1_intro.is_jumping:  # Only set falling to True if not jumping
                player_1_intro.falling = True

        # final calling after everything else
        if player_1_intro.movement:
            player_1_intro.move()
            if not hammer_1.intro_shown:
                hammer_1.move()

    def level1(self):
        screen.fill((20, 20, 20))
        screen.blit(arena_1, (0, 0))

        pygame.mixer.music.set_volume(options_reference.volume / 100)

        # references
        little_guys_time = 1800 + 120 # this number determines how long the little guys last
        big_guys_time = 1800 + 120 # this number determines how long the big guy lasts

        # calling things to the screen
        if not big_disc_1.killed:
            big_disc_1.draw(screen, disc_eye_left_img, disc_eye_right_img, pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 24))
            big_disc_1.move()

        littlediscs = [littledisc1, littledisc2, littledisc3, littledisc4]

        # code for the movement of the little discs
        if littledisc1.little_phase and littledisc1.timer < little_guys_time and not big_disc_1.second_phase and big_disc_1.placement:
            littledisc1.timer += 1
            littledisc1.stationary_disc += 1

            for disc in littlediscs:
                if not big_disc_1.killed:
                    if littledisc1.stationary_disc > 120:  # stationary time for the little discs
                        disc.draw(screen)

                    if littledisc1.stationary_disc > 180:  # stationary time for the little discs
                        disc.move()

        if littledisc1.timer >= little_guys_time:
            littledisc1.timer = 0
            littledisc1.stationary_disc = 0
            big_disc_1.placement = False
            big_disc_1.second_phase = True
            littledisc1.x, littledisc1.y = (465, 250)
            littledisc2.x, littledisc2.y = (750, 100)
            littledisc3.x, littledisc3.y = (750, 250)
            littledisc4.x, littledisc4.y = (465, 100)
            for disc in littlediscs:
                disc.angle = random.uniform(0, 2 * math.pi)
                disc.velocity = [
                    math.cos(disc.angle) * disc.movement_speed,
                    math.sin(disc.angle) * disc.movement_speed
                ]

        # calling player to screen
        player_1.draw()
        player_1.move()

        # code for the big guy moving
        if big_disc_1.timer < big_guys_time + 120 and big_disc_1.second_phase:
            littledisc1.little_phase = False
            big_disc_1.timer += 1
            big_disc_1.stationary_disc += 1
            big_disc_1.move()

            if big_disc_1.stationary_disc >= 120:  # stationary time for the big disc
                big_disc_1.movement = True

        if big_disc_1.timer >= big_guys_time + 120:
            big_disc_1.movement = False
            big_disc_1.second_phase = False
            big_disc_1.timer = 0
            big_disc_1.stationary_disc = 0

        # Below is the code for moving back the disc to its position when it gets done moving
        if not big_disc_1.second_phase and not big_disc_1.beginning_movement and not littledisc1.little_phase:
            target_x, target_y = 535, 100
            tolerance = 5  # Allowable distance to stop movement

            # Move big_disc_1 towards the target position
            if abs(big_disc_1.x - target_x) > tolerance:
                big_disc_1.x += big_disc_1.movement_speed if big_disc_1.x < target_x else -big_disc_1.movement_speed

            if abs(big_disc_1.y - target_y) > tolerance:
                big_disc_1.y += big_disc_1.movement_speed if big_disc_1.y < target_y else -big_disc_1.movement_speed

            # Check if big_disc_1 is within the tolerance range of the target position
            if abs(big_disc_1.x - target_x) <= tolerance and abs(big_disc_1.y - target_y) <= tolerance:
                big_disc_1.x, big_disc_1.y = target_x, target_y  # Snap to target position
                if big_disc_1.x == target_x and big_disc_1.y == target_y:
                    big_disc_1.placement = True
                    littledisc1.little_phase = True

                # Change the angle when the disc reaches its target
                if not big_disc_1.movement:
                    big_disc_1.angle = random.uniform(0, 2 * math.pi)
                    big_disc_1.velocity = [
                        math.cos(big_disc_1.angle) * big_disc_1.bouncing_speed,
                        math.sin(big_disc_1.angle) * big_disc_1.bouncing_speed
                    ]

        # code for the beginning movement of the big disc
        if not littledisc1.little_phase and not big_disc_1.second_phase and not player_1.game_over:
            if big_disc_1.y <= 100:
                big_disc_1.y += 1.5

            if big_disc_1.y == 101:
                big_disc_1.placement = True
                littledisc1.little_phase = True
                big_disc_1.beginning_movement = False
                player_1.movement = True

                for disc in littlediscs:
                    disc.movement = True

        if big_disc_1.placement:
            big_disc_1.health_shown = True
            if not big_disc_1.killed:
                game_state.play_music(self.boss1_music)

        # noinspection PyTypeChecker
        if not big_disc_1.killed and not player_1.game_over and not player_1.dashing:
            if pygame.sprite.collide_mask(big_disc_1, player_1) and player_1.hit_timer >= 60 and big_disc_1.second_phase:
                self.player_hit.play()
                player_1.health -= 1
                player_1.hit_timer = 0

            for disc in littlediscs:
                if pygame.sprite.collide_mask(disc, player_1) and player_1.hit_timer >= 60 and littledisc1.little_phase and littledisc1.stationary_disc >= 120:
                    self.player_hit.play()
                    player_1.health -= 1
                    player_1.hit_timer = 0

            if pygame.sprite.collide_rect(hammer_1, big_disc_1):
                if pygame.sprite.collide_mask(hammer_1, big_disc_1) and hammer_1.firing_up or hammer_1.firing_side:
                    self.enemy_hit.play()
                    big_disc_1.health -= 1
                    hammer_1.firing_timer = 0
                    hammer_1.x = player_1.x
                    hammer_1.y = player_1.y
                    hammer_1.firing_up = False
                    hammer_1.firing_left = False
                    hammer_1.firing_right = False
                    hammer_1.firing_side = False

        hammer_1.firing_timer += 1
        if player_1.movement:
            hammer_1.move()

        if player_1.health <= 0:
            player_1.game_over_timer += 1
            player_1.game_over = True

        if player_1.game_over:
            game_over_func()
            big_disc_1.second_phase = False
            littledisc1.little_phase = False
            littledisc1.stationary_disc = 0
            big_disc_1.movement = False
            player_1.x = 100
            player_1.y = 540
            big_disc_1.x = 535
            big_disc_1.y = 100
            big_disc_1.health = 50
            littledisc1.x, littledisc1.y = 465, 250  # bottom left disc
            littledisc2.x, littledisc2.y = 750, 100  # top right disc
            littledisc3.x, littledisc3.y = 750, 250  # bottom right disc
            littledisc4.x, littledisc4.y = 465, 100  # top left disc
            player_1.dash_timer = 0

        if big_disc_1.health <= 0:
            big_disc_1.killed = True

        if big_disc_1.killed:
            if big_disc_1.alpha <= 2:
                self.single_play(self.intermission_1)
            screen.blit(victory_img, (380, 100))
            big_disc_1.alpha += 1
            victory_img.set_alpha(big_disc_1.alpha)

            # countdown to the next boss area
            num_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 84)
            countdown = num_font.render(f'{options_reference.boss_countdown}', True, (172, 50, 50))

            if big_disc_1.alpha >= 255:
                options_reference.boss_countdown_timer += 1
                screen.blit(countdown, (610, 230))
            if options_reference.boss_countdown_timer >= 60:
                options_reference.boss_countdown -= 1
                options_reference.boss_countdown_timer = 0

        # logic for moving to next boss area (based on the set_alpha variable)
        if big_disc_1.alpha >= 435:  # 6 seconds becase 255 is max value for set_alpha
            player_1.dash_timer = 0
            self.state = 'level2'
            victory_img.set_alpha(0)
            options_reference.boss_countdown_timer = 0
            options_reference.boss_countdown = 3

    def level2(self):
        screen.fill((20, 20, 20))
        screen.blit(arena_1, (0, 0))

        pygame.mixer.music.set_volume(options_reference.volume / 100)

        pygame.mixer.Sound.set_volume(self.lightning_sound, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.player_hit, options_reference.volume / 100)
        pygame.mixer.Sound.set_volume(self.enemy_hit, options_reference.volume / 100)

        # references
        phase_time = 720  # default is 1800 (30 seconds)

        # calling things to screen
        little_screw = [littlescrew1, littlescrew2, littlescrew3, littlescrew4, littlescrew5, littlescrew6,
                        littlescrew7, littlescrew8, littlescrew9, littlescrew10]

        bigscrew1.beginning_timer += 1

        if 26 <= bigscrew1.beginning_timer <= 28:
            game_state.play_music(self.boss2_music)
        if 240 > bigscrew1.beginning_timer > 60 and bigscrew1.opening_shown:
            screen.blit(screw_entrance_img, (535, 110))

        if bigscrew1.beginning_timer <= 1:
            self.lightning_sound.play()

        if bigscrew1.beginning_timer > 240 and bigscrew1.opening_shown:
            bigscrew1.opening_shown = False

        if not bigscrew1.killed and bigscrew1.beginning_timer >= 60:
            bigscrew1.draw(screen, pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 24))

        # noinspection PyTypeChecker
        if not bigscrew1.killed and not player_1.game_over and not player_1.dashing:
            # Check for collision with the screw group (first group)
            player_collisions = pygame.sprite.groupcollide(player_group, screw_group, False, False,pygame.sprite.collide_rect)
            if player_collisions and player_1.hit_timer >= 60 and littlescrew1.phase_1:
                # Check for precise collision using the mask if rect collision is detected
                if pygame.sprite.groupcollide(player_group, screw_group, False, False, pygame.sprite.collide_mask):
                    self.player_hit.play()
                    player_1.health -= 1
                    player_1.hit_timer = 0

            # Check for collision with the second screw group
            player_second_collisions = pygame.sprite.groupcollide(player_group, second_screw_group, False, False, pygame.sprite.collide_rect)
            if player_1.hit_timer >= 60:
                if player_second_collisions and (bigscrew1.firing or littlescrew1.firing_left or littlescrew1.firing_right) and bigscrew1.phase_2:
                    if pygame.sprite.groupcollide(player_group, second_screw_group, False, False,pygame.sprite.collide_mask):
                        self.player_hit.play()
                        player_1.health -= 1
                        player_1.hit_timer = 0

            # Hammer collision with big screw
            if pygame.sprite.collide_rect(hammer_1, bigscrew1):
                # Ensure hammer is firing up or sideways before checking mask collision
                if pygame.sprite.collide_mask(hammer_1, bigscrew1) and (hammer_1.firing_up or hammer_1.firing_side):
                    self.enemy_hit2.play()
                    bigscrew1.health -= 1
                    hammer_1.firing_timer = 0
                    hammer_1.x = player_1.x
                    hammer_1.y = player_1.y
                    hammer_1.firing_up = False
                    hammer_1.firing_left = False
                    hammer_1.firing_right = False
                    hammer_1.firing_side = False

        # code here for the entrance
        if bigscrew1.x == 600:
            bigscrew1.placement = True

        if bigscrew1.placement and not player_1.game_over and not bigscrew1.opening_shown:
            player_1.movement = True

        if not bigscrew1.opening_shown:
            bigscrew1.stationary_timer += 1
            bigscrew1.health_shown = True

        # showing the boss after every cycle
        if bigscrew1.placement and bigscrew1.stationary_timer >= 180 and not bigscrew1.phase_2 and not player_1.game_over:
            littlescrew1.phase_1 = True
            bigscrew1.opening_shown = False

        if littlescrew1.phase_1_timer >= phase_time:
            littlescrew1.phase_1 = False
            bigscrew1.placement = False
            bigscrew1.phase_2 = True
            bigscrew1.phase_2_timer = 0
            littlescrew11.x = bigscrew1.x + 24
            littlescrew11.y = bigscrew1.y + 200
            bigscrew1.firing = False
            bigscrew1.firing_timer = 0
            littlescrew1.y = -500
            littlescrew2.y = -100
            littlescrew3.y = -700
            littlescrew4.y = -100
            littlescrew5.y = -300
            littlescrew6.y = -100
            littlescrew7.y = -200
            littlescrew8.y = -100
            littlescrew9.y = -400
            littlescrew10.y = -100
            littlescrew1.phase_1_timer = 0
            littlescrew12.x = -57

        # code for the screws falling down (phase 1)
        if littlescrew1.phase_1:
            littlescrew1.phase_1_timer += 1

            for screw in little_screw:
                screw.draw(screen)
                screw.movement_speed = random.randint(9, 13)
                screw.y += screw.movement_speed

                if screw.y >= 800:
                    screw.x = random.randint(32, 1248)
                    screw.y = -100
                    screw.movement_speed = random.randint(8, 12)

            # code for the screw to move from either side
            littlescrew12.draw(screen)
            littlescrew1.firing_timer += 1

            if bigscrew1.stationary_timer >= 240:
                if littlescrew1.screw_side == 1 and not littlescrew1.firing_left and not littlescrew1.firing_right:
                    littlescrew12.x = -57
                    littlescrew12.rotate(90)
                    littlescrew1.firing_right = True
                if littlescrew1.screw_side == 2 and not littlescrew1.firing_left and not littlescrew1.firing_right:
                    littlescrew12.x = 1307
                    littlescrew12.rotate(-90)
                    littlescrew1.firing_left = True

                if littlescrew12.x >= 1310 and littlescrew1.firing_timer >= 360:  # 360 is four-second intervals
                    littlescrew12.x = 1307
                    littlescrew12.rotate(-90)
                    littlescrew1.firing_left = True
                    littlescrew1.firing_right = False
                    littlescrew1.firing_timer = 0
                if littlescrew12.x < -60 and littlescrew1.firing_timer >= 360:  # 360 is four-second intervals
                    littlescrew12.x = -57
                    littlescrew12.rotate(90)
                    littlescrew1.firing_right = True
                    littlescrew1.firing_left = False
                    littlescrew1.firing_timer = 0

                if littlescrew1.firing_right:
                    littlescrew12.x += 10
                if littlescrew1.firing_left:
                    littlescrew12.x -= 10

        # Code for the screw to follow the player and shoot screws at intervals (phase 2)
        if bigscrew1.phase_2_timer >= phase_time:
            bigscrew1.phase_2 = False
            bigscrew1.phase_2_stationary_timer = 0

        # firing for screw 11
        if bigscrew1.phase_2_stationary_timer >= 120:
            if bigscrew1.phase_2 or bigscrew1.firing:
                if not bigscrew1.firing:
                    bigscrew1.firing_timer += 1
                    littlescrew11.x = bigscrew1.x + 27
                    littlescrew11.y = bigscrew1.y + 200
                    if bigscrew1.firing_timer >= 30:
                        self.screw_fire.play()
                        bigscrew1.firing = True
                else:
                    littlescrew11.y += 15

                    if littlescrew11.y >= 750:
                        bigscrew1.firing = False
                        bigscrew1.firing_timer = 0

        if bigscrew1.firing and bigscrew1.phase_2_stationary_timer >= 120:
            littlescrew11.draw(screen)

        if bigscrew1.phase_2:
            bigscrew1.phase_2_timer += 1
            bigscrew1.phase_2_stationary_timer += 1

            if bigscrew1.phase_2_stationary_timer >= 60:
                littlescrew11.draw(screen)

            if bigscrew1.phase_2_timer <= phase_time and bigscrew1.phase_2_stationary_timer >= 120:
                # Define the target position for bigscrew1 with an offset
                target_x = player_1.x - 22

                # Move bigscrew1 toward the target position smoothly
                if bigscrew1.x < target_x:
                    bigscrew1.x += bigscrew1.movement_speed
                elif bigscrew1.x > target_x:
                    bigscrew1.x -= bigscrew1.movement_speed

                # Snap to the target position when close enough
                if abs(bigscrew1.x - target_x) < bigscrew1.movement_speed:
                    bigscrew1.x = target_x
                bigscrew1.stationary_timer = 0

        # moving the screw back to its position after phase 2
        tolerance = 3  # Adjust this value as needed
        if not bigscrew1.phase_2:
            if abs(bigscrew1.x - 600) <= tolerance:
                bigscrew1.x = 600  # Snap to 600
            elif bigscrew1.x < 600:
                bigscrew1.x += bigscrew1.movement_speed
            elif bigscrew1.x > 600:
                bigscrew1.x -= bigscrew1.movement_speed

        # calling player to screen
        player_1.draw()
        if not bigscrew1.opening_shown:
            player_1.movement = True
            player_1.move()
        if not player_1.game_over and not bigscrew1.opening_shown:
            hammer_1.firing_timer += 1
            hammer_1.move()

        if player_1.health <= 0:
            player_1.game_over_timer += 1
            player_1.game_over = True

        if bigscrew1.killed or player_1.game_over:
            bigscrew1.phase_2 = False
            littlescrew1.phase_1_timer = 0
            littlescrew1.phase_1 = False
            bigscrew1.x = 600
            littlescrew1.y = -500
            littlescrew2.y = -100
            littlescrew3.y = -700
            littlescrew4.y = -100
            littlescrew5.y = -300
            littlescrew6.y = -100
            littlescrew7.y = -200
            littlescrew8.y = -100
            littlescrew9.y = -400
            littlescrew10.y = -100
            bigscrew1.health = 50
            littlescrew12.x = -57
            player_1.dash_timer = 0
            if player_1.game_over:
                game_over_func()
                player_1.x = 100
                player_1.y = 540
                bigscrew1.stationary_timer = 0

        if bigscrew1.health <= 0:
            bigscrew1.killed = True

        if bigscrew1.killed:
            if 0 <= bigscrew1.killed_alpha <= 2:
                self.single_play(self.intermission_2)
            screen.blit(victory_img, (380, 100))
            bigscrew1.killed_alpha += 1
            victory_img.set_alpha(bigscrew1.killed_alpha)

            # countdown to the next boss area
            num_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 84)
            countdown = num_font.render(f'{options_reference.boss_countdown}', True, (172, 50, 50))

            if bigscrew1.killed_alpha >= 255:
                options_reference.boss_countdown_timer += 1
                screen.blit(countdown, (610, 230))
            if options_reference.boss_countdown_timer >= 60:
                options_reference.boss_countdown -= 1
                options_reference.boss_countdown_timer = 0

        # this is for the game over
        if bigscrew1.killed_alpha >= 435:
            player_1.dash_timer = 0
            self.state = 'level3'
            victory_img.set_alpha(0)
            options_reference.boss_countdown_timer = 0
            options_reference.boss_countdown = 3

    def level3(self):
        screen.fill((20, 20, 20))
        screen.blit(arena_1, (0, 0))

        # music stuff
        pygame.mixer.music.set_volume(options_reference.volume / 100)
        if 25.8 <= saw_boss1.beginning_movement_timer <= 27:
            game_state.play_music(self.boss3_music)

        # phases time
        phase_1_time = 720 + 120  # default is 1800
        phase_2_time = 720 + 120  # default is 1800

        # calling boss to screen
        if saw_blade1.blade_shown and not player_1.game_over and not saw_boss1.killed:
            saw_blade1.draw()

        if not saw_boss1.killed:
            saw_boss1.draw()

        # the opening movement of the saw boss
        if saw_boss1.beginning_movement:
            player_1.movement = False
            saw_boss1.opening_movement()

        saw_boss1.beginning_movement_timer += 1
        # phase 1 of the saw boss
        if saw_boss1.phase_1 and not saw_boss1.beginning_movement and saw_boss1.beginning_movement_timer >= 180:
            saw_blade1.bouncing = False
            saw_boss1.beginning_movement = False
            saw_blade1.blade_shown = False
            saw_boss1.phase_1_timer += 1
            saw_boss1.phase_1_attack_timer += 1

            if saw_boss1.phase_1_timer >= 120:
                saw_boss1.attacking = True

            # this is for the first caution
            if saw_boss1.y == 100 and saw_boss1.phase_1_attack_timer >= 120 and saw_boss1.first_time:
                screen.blit(caution, (600, 250))

            if saw_boss1.phase_1_attack_timer >= 180:
                saw_boss1.first_time = False  # cutting the first time off so that everything defualts to second caution

            # this is for every caution after the first one
            if saw_boss1.y < 100 and saw_boss1.phase_1_attack_timer >= 90 and not saw_boss1.first_time:
                screen.blit(caution, (600,150))

            saw_boss1.sfx_timer += 1

            if saw_boss1.y >= 470:
                if saw_boss1.pointing_right and saw_boss1.sfx_timer >= 60:
                    self.saw_right.play()
                    saw_boss1.sfx_timer = 0

                if saw_boss1.pointing_left and saw_boss1.sfx_timer >= 60:
                    self.saw_left.play()
                    saw_boss1.sfx_timer = 0

            if saw_boss1.attacking and saw_boss1.phase_1_attack_timer >= 150:

                if saw_boss1.y >= 470:
                    if saw_boss1.pointing_right:
                        saw_boss1.x += 25

                    if saw_boss1.pointing_left:
                        saw_boss1.x -= 25

                if saw_boss1.x >= 1400 or saw_boss1.x <= -400:
                    # Reset position and direction
                    saw_boss1.y = -200

                    position = random.randint(1, 2)

                    # Determine pointing direction
                    if position == 1:
                        if not saw_boss1.pointing_right:  # Flip only if changing direction
                            saw_boss1.image = pygame.transform.flip(saw_boss1.image, True, False)
                        saw_boss1.pointing_right = True
                        saw_boss1.pointing_left = False

                    elif position == 2:
                        if not saw_boss1.pointing_left:  # Flip only if changing direction
                            saw_boss1.image = pygame.transform.flip(saw_boss1.image, True, False)
                        saw_boss1.pointing_left = True
                        saw_boss1.pointing_right = False

                    # Reset position and attack timer
                    saw_boss1.x = 500
                    saw_boss1.phase_1_attack_timer = 0

                saw_boss1.y = min(saw_boss1.y + 20, 475)

        if saw_boss1.phase_1_timer >= phase_1_time:
            saw_boss1.phase_1 = False
            saw_boss1.phase_1_timer = 0
            saw_boss1.phase_1_attack_timer = 0
            saw_boss1.moving_position = True

        # moving the saw_boss1 back to his original position after phase 1
        if not saw_boss1.phase_1 and saw_boss1.moving_position:
            target_x, target_y = 500, 100
            tolerance = 5  # Allowable distance to stop movement

            # Move saw_boss1 towards the target position
            if abs(saw_boss1.x - target_x) > tolerance:
                saw_boss1.x += saw_boss1.movement_speed if saw_boss1.x < target_x else -saw_boss1.movement_speed

            if abs(saw_boss1.y - target_y) > tolerance:
                saw_boss1.y += saw_boss1.movement_speed if saw_boss1.y < target_y else -saw_boss1.movement_speed

            # Check if big_disc_1 is within the tolerance range of the target position
            if abs(saw_boss1.x - target_x) <= tolerance and abs(saw_boss1.y - target_y) <= tolerance:
                saw_boss1.x, saw_boss1.y = target_x, target_y  # Snap to target position
                if saw_boss1.x == target_x and saw_boss1.y == target_y:
                    saw_boss1.moving_position = False
                    saw_boss1.phase_2 = True

        # phase 2 of the saw boss
        if saw_boss1.phase_2:
            saw_boss1.phase_2_timer += 1
            saw_blade1.phase_2_stationary_timer += 1
            saw_blade1.blade_shown = True

            # Initialize position only once when the blade is shown
            if saw_blade1.blade_shown and saw_blade1.phase_2_stationary_timer < 120:
                if saw_boss1.pointing_right:
                    saw_blade1.x = 695
                    saw_blade1.y = 135
                elif saw_boss1.pointing_left:
                    saw_blade1.x = 485
                    saw_blade1.y = 135

            # After stationary phase ends, continuously update x
            if saw_blade1.phase_2_stationary_timer >= 180 and not saw_blade1.bouncing:
                if saw_blade1.y <= 200:
                    saw_blade1.y += 3
                if saw_boss1.pointing_right:
                    saw_blade1.x += 12  # Keep moving right
                elif saw_boss1.pointing_left:
                    saw_blade1.x -= 12  # Keep moving left

                if saw_blade1.x < -600:
                    saw_blade1.x = -550
                    saw_blade1.bouncing = True

                if saw_blade1.x > 1850:
                    saw_blade1.x = 1750
                    saw_blade1.bouncing = True

            if saw_blade1.bouncing:
                # Apply gravity to vertical velocity
                saw_blade1.velocity_y += saw_blade1.gravity
                saw_blade1.y += saw_blade1.velocity_y

                # Move the saw blade horizontally
                saw_blade1.x += saw_blade1.horizontal_speed

                # Check if the saw blade moves past the edges of the screen
                if saw_blade1.x > screen.get_width() + 200:  # Right edge (adjust margin if necessary)
                    saw_blade1.horizontal_speed = -abs(saw_blade1.horizontal_speed)  # Switch to moving left

                if saw_blade1.x < -200:  # Left edge (adjust margin if necessary)
                    saw_blade1.horizontal_speed = abs(saw_blade1.horizontal_speed)  # Switch to moving right

                # Check for collision with the ground
                if saw_blade1.y >= 500:
                    saw_blade1.y = 500  # Ensure it stays on the ground
                    saw_blade1.velocity_y = saw_blade1.bounce_velocity  # Reset to fixed upward velocity

        if saw_boss1.phase_2_timer >= phase_2_time:
            saw_boss1.phase_2 = False
            saw_boss1.first_time = True
            saw_blade1.bouncing = False
            saw_blade1.moving_position = True
            saw_boss1.phase_2_timer = 0
            saw_blade1.phase_2_stationary_timer = 0

        # doing the movement back for the saw blade
        if saw_boss1.pointing_right:
            target_x, target_y = 695, 135
        if saw_boss1.pointing_left:
            target_x, target_y = 485, 135

        if saw_blade1.moving_position:
            tolerance = 5  # Allowable distance to stop movement

            # Move saw blade towards the target position
            if abs(saw_blade1.x - target_x) > tolerance:
                saw_blade1.x += saw_blade1.movement_speed if saw_blade1.x < target_x else -saw_blade1.movement_speed

            if abs(saw_blade1.y - target_y) > tolerance:
                saw_blade1.y += saw_blade1.movement_speed if saw_blade1.y < target_y else -saw_blade1.movement_speed

            # Check if saw blade is within the tolerance range of the target position
            if abs(saw_blade1.x - target_x) <= tolerance and abs(saw_blade1.y - target_y) <= tolerance:
                saw_blade1.x, saw_blade1.y = target_x, target_y  # Snap to target position
                if saw_blade1.x == target_x and saw_blade1.y == target_y:
                    saw_blade1.moving_position = False
                    saw_boss1.phase_1 = True
                    saw_blade1.blade_shown = False

        # collisions with the objects
        if not saw_boss1.killed and not player_1.game_over and not player_1.dashing:
            # Check collision with saw_boss1 in phase 1
            if player_1.hit_timer >= 60 and saw_boss1.phase_1:
                if pygame.sprite.groupcollide(player_group, boss_group, False, False,pygame.sprite.collide_mask) and saw_boss1.phase_1:
                    self.player_hit.play()
                    player_1.health -= 1
                    player_1.hit_timer = 0

            # Check collision with enemy_group2 for phase 2
            player_second_collisions = pygame.sprite.groupcollide(player_group, enemy_group2, False, False,pygame.sprite.collide_rect)
            if player_1.hit_timer >= 60 and player_second_collisions and saw_boss1.phase_2:
                if pygame.sprite.groupcollide(player_group, enemy_group2, False, False, pygame.sprite.collide_mask):
                    self.player_hit.play()
                    player_1.health -= 1
                    player_1.hit_timer = 0

            # Hammer collision with saw_boss1
            if pygame.sprite.collide_rect(hammer_1, saw_boss1):
                # Check hammer firing and collision with saw_boss1 using mask
                if pygame.sprite.collide_mask(hammer_1, saw_boss1) and (hammer_1.firing_up or hammer_1.firing_side):
                    self.enemy_hit3.play()
                    saw_boss1.health -= 1
                    hammer_1.firing_timer = 0
                    hammer_1.x = player_1.x
                    hammer_1.y = player_1.y
                    hammer_1.firing_up = False
                    hammer_1.firing_left = False
                    hammer_1.firing_right = False
                    hammer_1.firing_side = False

        # calling player and hammer to screen
        player_1.draw()
        player_1.move()
        hammer_1.firing_timer += 1
        if not player_1.game_over and not saw_boss1.beginning_movement:
            player_1.movement = True
            hammer_1.move()

        # game over condition for the player
        if player_1.health <= 0:
            player_1.game_over_timer += 1
            player_1.game_over = True

        if saw_boss1.killed or player_1.game_over:
            saw_boss1.phase_2 = False
            saw_boss1.phase_1_timer = 0
            saw_boss1.beginning_movement_timer = 0
            saw_boss1.health = 50
            player_1.dash_timer = 0
            if player_1.game_over:
                game_over_func()
                if saw_boss1.pointing_right:
                    saw_blade1.x = 695
                    saw_blade1.y = 135
                if saw_boss1.pointing_left:
                    saw_blade1.x = 485
                    saw_blade1.y = 135
                player_1.x = 100
                player_1.y = 540
                saw_boss1.x = 500
                saw_boss1.y = 100
                saw_boss1.stationary_timer = 0
                saw_blade1.bouncing = False
                saw_boss1.phase_1 = True

        if saw_boss1.health <= 0:
            saw_boss1.killed = True

        if saw_boss1.killed:
            screen.blit(victory_img, (380, 100))
            saw_boss1.alpha += 1
            victory_img.set_alpha(saw_boss1.alpha)

            # countdown to the next boss area
            num_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 84)
            countdown = num_font.render(f'{options_reference.boss_countdown}', True, (172, 50, 50))

            if saw_boss1.alpha >= 255:
                options_reference.boss_countdown_timer += 1
                screen.blit(countdown, (610, 230))
            if options_reference.boss_countdown_timer >= 60:
                options_reference.boss_countdown -= 1
                options_reference.boss_countdown_timer = 0

        # this is for the game over
        if saw_boss1.alpha >= 435:
            player_1.dash_timer = 0
            self.state = 'end'
            victory_img.set_alpha(0)
            options_reference.boss_countdown_timer = 0
            options_reference.boss_countdown = 6

    @staticmethod
    def end():
        screen.fill((20, 20, 20))

        # text for the instructions
        game_end_font = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 96)
        game_end_font2 = pygame.font.Font(resource_path('assets/fonts/FieldGuide.ttf'), 72)
        game_end_text1 = game_end_font.render('Thank you', True, (255, 255, 255))
        game_end_text2 = game_end_font.render('for playing', True, (255, 255, 255))
        game_end_text3 = game_end_font.render('our Gamejam!', True, (255, 255, 255))
        game_end_text4 = game_end_font2.render('Click our links below to stay updated!', True, (255, 255, 255))


        screen.blit(game_end_text1, (50, 20))
        screen.blit(game_end_text2, (100, 150))
        screen.blit(game_end_text3, (150, 280))
        screen.blit(game_end_text4, (90, 520))
        screen.blit(disc_boss_img, (925, 100))
        screen.blit(disc_eye_left_img, (975, 140))
        screen.blit(disc_eye_right_img, (1075, 140))

        # buttons to the different links
        options_reference.link_timer += 1

        if youtube_button2.draw(screen) and options_reference.link_timer >= 5:
            webbrowser.open("https://www.youtube.com/@GhastlyGamez")
            options_reference.link_timer = 0

        if discord_button2.draw(screen) and options_reference.link_timer >= 5:
            webbrowser.open("https://discord.gg/jB7gUKPDK7")
            options_reference.link_timer = 0

        if website_button2.draw(screen) and options_reference.link_timer >= 5:
            webbrowser.open("https://www.ghastlygames.net")
            options_reference.link_timer = 0

    def state_manager(self):
        state_methods = {
            'mainmenu': self.mainmenu,
            'creditsmenu': self.creditsmenu,
            'optionsmenu': self.optionsmenu,
            # levels
            'intro': self.intro,
            'level1': self.level1,
            'level2': self.level2,
            'level3': self.level3,
            # game over stuff
            'end': self.end,
        }

        method = state_methods.get(self.state)
        if method:
            method()

# general class calling
player_1 = Player(100, 540)
hammer_1 = Hammer(100, 600)
controller_reference = Controller_references()

# main menu class calling
start_button_menu = button.Button(50, 250, start_button, 1)
options_button_menu = button.Button(50, 350, options_button, 1)
credits_button_menu = button.Button(50, 450, credits_button, 1)
exit_button_menu = button.Button(50, 550, exit_button, 1)
discord_button = button.Button(1180, 635, discord_img, 1)
youtube_button = button.Button(1080, 640, youtube_img, 1)
website_button = button.Button(980, 625, ghastly_img, 1)
discord_button2 = button.Button(690, 635, discord_img, 1)
youtube_button2 = button.Button(580, 640, youtube_img, 1)
website_button2 = button.Button(480, 625, ghastly_img, 1)
big_disc_main_menu = big_disc.Big_disc(535, 100, disc_boss_img)
bigscrew_main_menu = big_screw.Big_Screw(20, 10, screw_boss_img)
saw_boss_main_menu = Saw_boss(-300, 600)

# options menu class calling
options_reference = Options_references()
left_button2 = button.Button(100, 350, left_arrow, 1)
right_button2 = button.Button(500, 350, right_arrow, 1)
left_button3 = button.Button(700, 350, left_arrow, 1)
right_button3 = button.Button(1150, 350, right_arrow, 1)
applybut = button.Button(240, 500, apply_button, 1)

# intro class calling
player_1_intro = Player(20, 540)

# level 1 class calling
littledisc1 = little_disc.Little_disc(465, 250, little_disc_img)  # bottom left disc
littledisc2 = little_disc.Little_disc(750, 100, little_disc_img)  # top right disc
littledisc3 = little_disc.Little_disc(750, 250, little_disc_img)  # bottom right disc
littledisc4 = little_disc.Little_disc(465, 100, little_disc_img)  # top left disc
big_disc_1 = big_disc.Big_disc(535, -400, disc_boss_img)

littlediscs = [littledisc1, littledisc2, littledisc3, littledisc4]

# level 2 class calling
bigscrew1 = big_screw.Big_Screw(600, 120, screw_boss_img)
littlescrew1 = little_screw.Little_screw(random.randint(32, 1248), -500, screw_img)
littlescrew2 = little_screw.Little_screw(random.randint(32, 1248), -100, screw_img)
littlescrew3 = little_screw.Little_screw(random.randint(32, 1248), -700, screw_img)
littlescrew4 = little_screw.Little_screw(random.randint(32, 1248), -100, screw_img)
littlescrew5 = little_screw.Little_screw(random.randint(32, 1248), -300, screw_img)
littlescrew6 = little_screw.Little_screw(random.randint(32, 1248), -100, screw_img)
littlescrew7 = little_screw.Little_screw(random.randint(32, 1248), -200, screw_img)
littlescrew8 = little_screw.Little_screw(random.randint(32, 1248), -100, screw_img)
littlescrew9 = little_screw.Little_screw(random.randint(32, 1248), -400, screw_img)
littlescrew10 = little_screw.Little_screw(random.randint(32, 1248), -100, screw_img)
littlescrew11 = little_screw.Little_screw(100, 300, screw_img)
littlescrew12 = little_screw.Little_screw(-80, 560, screw_img)
littlescrew12.rotate(90)

# level 3 class calling
saw_boss1 = Saw_boss(-300, 100)
saw_blade1 = Saw_blade(-300, 100)

# putting in groups
little_screw = [littlescrew1, littlescrew2, littlescrew3, littlescrew4, littlescrew5, littlescrew6,
                        littlescrew7, littlescrew8, littlescrew9, littlescrew10]

hammer_group = pygame.sprite.Group()
hammer_group.add(hammer_1)

player_group = pygame.sprite.Group()
player_group.add(player_1)

second_screw_group = pygame.sprite.Group()
second_screw_group.add(littlescrew11)

enemy_group = pygame.sprite.Group()
enemy_group.add(big_disc_1)
enemy_group.add(bigscrew1)

screw_group = pygame.sprite.Group()
screw_group.add(littlescrew12)

for screw in little_screw:
    enemy_group.add(screw)
    screw_group.add(screw)

for disc in littlediscs:
    enemy_group.add(disc)

enemy_group2 = pygame.sprite.Group()
enemy_group2.add(saw_blade1)

boss_group = pygame.sprite.Group()
boss_group.add(big_disc_1)
boss_group.add(bigscrew1)
boss_group.add(saw_boss1)

# reference stuff
FPS = 60
clock = pygame.time.Clock()
game_state = GameState()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    game_state.state_manager()

    pygame.display.flip()
pygame.quit()
