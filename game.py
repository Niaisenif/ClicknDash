import pygame
from player import Player
from platform import TileLoader


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.player = Player(self)
        self.pressed = {}
        self.g_force_activated = False
        self.tile = TileLoader(self)
        self.all_tiles = pygame.sprite.Group()
        self.tile.load_all_tiles(self.screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def update_game(self):
        self.screen.blit(self.player.trail.image, (self.player.rect.x + self.player.trail.x_offset,
                                                   self.player.rect.y + self.player.trail.y_offset))
        self.screen.blit(self.player.image, self.player.rect)
        self.player.is_touching_ground()
        self.player.update_dash()
        self.player.update_y_value()
        self.tile.blit_all_tiles(self.screen)
        pygame.draw.circle(self.screen, 1, self.player.rect.center, 300, 1)

