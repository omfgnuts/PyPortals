__author__ = 'Nuts)'
import pygame
class Platform(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load("data/brick_small.png")
        self.rect = self.image.get_rect(topleft=pos)