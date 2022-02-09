import pygame


class DashPanel(pygame.sprite.Sprite):

    def __init__(self, path, place):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.number = place
