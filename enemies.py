import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load("assets/enemmi.png")), (128, 128))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 900
        self.rect.y = 400
        self.game.all_enemy.add(self)

    def check_player_collide(self):
        if self.game.check_collision(self, self.game.player.all_player) and self.game.player.is_dashing:
            self.game.all_enemy.remove(self)

    def shoot(self):
        self.game.enemy_projectile.new_projectile(self.rect.x, self.rect.y, 5, 1)

class EnemyProjectile(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("assets/projectile.png")
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 0
        self.rect.y = 0
        self.velocity = 0
        self.size = 1
        print("hi")

    def new_projectile(self, x, y, velocity, size):
        self.game.all_enemy_projectiles.add(self)
        self.rect.x, self.rect.y = x, y
        self.velocity = velocity
        self.size = size

    def move(self):
        self.rect.x -= self.velocity
