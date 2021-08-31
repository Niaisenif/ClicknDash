import pygame
from player import Player
from platform import TileLoader
from enemies import Enemy, EnemyProjectile


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.player = Player(self)
        self.all_enemy = pygame.sprite.Group()
        self.all_enemy_projectiles = pygame.sprite.Group()
        self.enemy = Enemy(self)
        self.enemy_projectile = EnemyProjectile(self)
        self.pressed = {}
        self.g_force_activated = False
        self.tile = TileLoader(self)
        self.all_tiles = pygame.sprite.Group()
        self.tile.load_all_tiles(self.screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollideany(sprite, group)

    def update_game(self):
        self.tile.blit_all_tiles(self.screen)
        self.screen.blit(self.player.trail.image, (self.player.rect.x + self.player.trail.x_offset,
                                                   self.player.rect.y + self.player.trail.y_offset))
        self.screen.blit(self.player.image, self.player.rect)
        self.all_enemy.draw(self.screen)
        self.all_enemy_projectiles.draw(self.screen)
        self.enemy.check_player_collide()
        for projectile in self.all_enemy_projectiles:
            projectile.move()
            projectile.update_animation()
        self.player.is_touching_ground()
        self.player.update_dash()
        self.player.update_y_value()
        pygame.draw.circle(self.screen, 1, self.player.rect.center, 300, 1)

