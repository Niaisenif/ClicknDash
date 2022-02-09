# import pygame
import game
import pytmx
from enemies import Enemy
from platform import TileLoader


class LevelLoader:

    def __init__(self, game):
        self.game = game
        self.TL = TileLoader(self.game)
        self.enemy_list = [[[self.game]]]
        self.dash_list = [[]]
        self.map_list = [pytmx.load_pygame("assets/map 3.tmx")]

    def load_level(self, level):  # difficulty will be here
        self.load_ennemies(self.enemy_list[level])
        self.TL.load_all_tiles(self.game.screen, self.map_list[level])
        self.load_dashes(self.dash_list[level])

    def load_ennemies(self, enemy_list):
        for enemy in enemy_list:
            self.game.all_enemy.add(Enemy(enemy[0]))

    def load_dashes(self, dash_list):
        a = dash_list
        return a
