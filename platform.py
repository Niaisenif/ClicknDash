import pygame
import pytmx


# noinspection SpellCheckingInspection
class TileLoader:
    def __init__(self, game):
        self.game = game

    # noinspection SpellCheckingInspection
    def load_all_tiles(self, screen, tmxdata=pytmx.load_pygame("assets/map 3.tmx")):
        for layer in tmxdata:
            for tile in layer.tiles():
                x_pixel = tile[0] * 64
                y_pixel = (tile[1] * 64) + 100
                screen.blit(tile[2], (x_pixel, y_pixel))
                self.game.all_tiles.add(Tile(tile[2], x_pixel, y_pixel))

    def blit_all_tiles(self, screen):
        self.game.all_tiles.draw(screen)


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, rect_x, rect_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
