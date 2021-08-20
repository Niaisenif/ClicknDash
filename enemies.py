import pygame


class Ennemies(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.transform.scale((pygame.image.load("assets/enemmi.png")), (128, 128))
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = 900
        self.rect.y = 400
        self.game.all_ennemies.add(self)

    def check_player_collide(self):
        if self.game.check_collision(self, self.game.player.all_player) and self.game.player.is_dashing:
            self.game.all_ennemies.remove(self)
