import pygame
from player import Player
from platform import TileLoader
from enemies import Enemy, EnemyProjectile
from overlay import DashPanel
from levels import LevelLoader


class Game:

    def __init__(self, screen):
        self.is_playing = True
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.pressed = {}
        self.g_force_activated = False

        # self.overlay = Overlay()
        self.player = Player(self)

        self.all_enemy = pygame.sprite.Group()
        self.all_enemy_projectiles = pygame.sprite.Group()
        self.all_tiles = pygame.sprite.Group()

        self.LL = LevelLoader(self)
        self.LL.load_level(0)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def update_game(self):
        self.screen.blit(pygame.image.load('assets/Overlay.png'), (0, 0))
        self.LL.TL.blit_all_tiles(self.screen)
        self.screen.blit(self.player.trail.image, (self.player.rect.x + self.player.trail.x_offset,
                                                   self.player.rect.y + self.player.trail.y_offset))
        self.screen.blit(self.player.image, self.player.rect)
        self.all_enemy.draw(self.screen)
        self.all_enemy_projectiles.draw(self.screen)
        for enemy in self.all_enemy:
            enemy.check_player_collide()
        self.player.update_health()
        for projectile in self.all_enemy_projectiles:
            projectile.move()
            projectile.update_animation()
        self.player.is_touching_ground()
        self.player.update_dash()
        self.player.update_y_value()
        pygame.draw.circle(self.screen, 1, self.player.rect.center, 300, 1)
