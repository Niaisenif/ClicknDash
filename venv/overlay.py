import pygame

class Overlay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/health adn dash.png")
        self.rect = self.image.get_rect()