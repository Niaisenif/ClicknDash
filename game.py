import pygame
from player import Player
from overlay import Overlay
from levels import LevelLoader


class Game:

    def __init__(self, screen, level):
        self.is_playing = True
        self.is_paused = False
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.pressed = {}
        self.g_force_activated = False

        self.player = Player(self)

        self.all_enemy = pygame.sprite.Group()
        self.all_enemy_projectiles = pygame.sprite.Group()
        self.all_tiles = pygame.sprite.Group()

        self.LL = LevelLoader(self)
        if level > -1:
            self.LL.load_level(level)
            self.Overlay = Overlay(self)

    @staticmethod  # idk why but pycharm is happier with that
    def check_collision(sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def update_game(self):
        self.screen.blit(pygame.image.load('assets/Overlay.png'), (0, 0))
        self.LL.TL.blit_all_tiles(self.screen)
        self.screen.blit(self.player.trail.image, (self.player.rect.x + self.player.trail.x_offset,
                                                   self.player.rect.y + self.player.trail.y_offset))
        self.screen.blit(self.player.image, self.player.rect)
        self.all_enemy.draw(self.screen)
        self.all_enemy_projectiles.draw(self.screen)
        self.Overlay.all_panels.draw(self.screen)

        for enemy in self.all_enemy:
            enemy.check_player_collide()

        self.player.update_health()
        if not self.is_paused:
            for projectile in self.all_enemy_projectiles:
                projectile.move()
                projectile.update_animation()
            self.player.is_touching_ground()
            self.player.update_dash()
            self.player.update_y_value()
        pygame.draw.circle(self.screen, 1, self.player.rect.center, 300, 1)
