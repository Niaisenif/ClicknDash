import pygame
import random
import animations


class Enemy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load("assets/enemy.png")), (128, 128))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 900
        self.rect.y = 400
        self.game.all_enemy.add(self)

    def check_player_collide(self):
        if self.game.check_collision(self, self.game.player.all_player) and self.game.player.is_dashing:
            self.game.all_enemy.remove(self)

    def shoot(self):
        self.game.enemy_projectile.new_projectile(self.rect.centerx, self.rect.centery, 5, 1, True)


class EnemyProjectile(animations.AnimateSprite):

    def __init__(self, game, x=0, y=0, velocity=0, size=1, guided=False):
        super().__init__('projectile')
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = velocity
        self.size = size
        self.guided = guided
        self.vector = None
        self.start_animation()

    def new_projectile(self, x, y, velocity, size=1, guided=False):
        self.game.all_enemy_projectiles.add(EnemyProjectile(self.game, x,  y, velocity, size, guided))
        print(self.guided)

    def update_animation(self):
        self.animate(loop=True)

    def move(self):
        if self.guided:
            self.vector = (pygame.Vector2(self.game.player.rect.center) - self.rect.center).normalize()
            self.rect.center += self.vector * self.velocity
        if not self.guided:
            self.rect.x -= self.velocity
        if self.rect.x < 50 or self.game.check_collision(self, self.game.all_tiles) or self.game.check_collision(self, self.game.player.all_player):
            self.game.all_enemy_projectiles.remove(self)
