import pygame
import animations


class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, x=900, y=500, path="assets/enemy_2.png"):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load(path)), (128, 128))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = x
        self.rect.y = y
        self.max_health = 550
        self.health = self.max_health
        self.auto_shoot_counter = 0
        self.E_P = EnemyProjectile(self.game)

    def check_player_collide(self):
        if not self.game.is_paused:
            if self.game.check_collision(self, self.game.player.all_player) and self.game.player.is_dashing:
                if self.health <= 0:
                    self.game.all_enemy.remove(self)
                self.health -= self.game.player.damage
        pygame.draw.rect(self.game.screen, (255, 0, 0), pygame.Rect((926, 41, self.health - 1, 19)))

    def shoot(self):
        # self.game.enemy_projectile.new_projectile(self.rect.centerx, self.rect.centery, 5, 1, False)
        self.E_P.new_projectile(self.rect.centerx, self.rect.centery, 5, 1, False)

    def auto_shoot(self, frames):
        if self.auto_shoot_counter == 0:
            self.shoot()
            self.auto_shoot_counter = frames
        else:
            self.auto_shoot_counter -= 1


class EnemyProjectile(animations.AnimateSprite):

    def __init__(self, game, x=0, y=0, velocity=0, size=1, guided=False):
        super().__init__('projectile')
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity = velocity
        self.size = size
        self.damage = 10
        self.guided = guided
        self.vector = None
        self.start_animation()
        if not self.guided:
            self.vector = (pygame.Vector2(self.game.player.rect.center) - self.rect.center).normalize()

    def new_projectile(self, x, y, velocity, size=1, guided=False):
        self.game.all_enemy_projectiles.add(EnemyProjectile(self.game, x,  y, velocity, size, guided))

    def update_animation(self):
        self.animate(loop=True)

    def move(self):
        if self.guided:
            self.vector = (pygame.Vector2(self.game.player.rect.center) - self.rect.center).normalize()
            self.rect.center += self.vector * self.velocity
        if not self.guided:
            self.rect.center += self.vector * self.velocity
        if self.rect.x < 50 or self.game.check_collision(self, self.game.player.all_player):
            self.game.all_enemy_projectiles.remove(self)
            self.game.player.health -= self.damage
        if self.game.check_collision(self, self.game.all_tiles):
            self.game.all_enemy_projectiles.remove(self)
