import pygame

class Button:
    def __init__(self, x, y, image, scale):
        height = image.get_height()
        width = image.get_width()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        # mouse position
        pos = pygame.mouse.get_pos()
        
        #screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pos):
            return True

        else:
            return False