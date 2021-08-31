import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = (self.game.screen_width / 2) - (self.image.get_width() / 2)
        self.rect.y = (self.game.screen_height / 2) - (self.image.get_height() / 2)
        self.trail = PlayerTrail(self.game, self)
        self.g_force = 0
        self.g_force_activated = False
        self.jump_force = 0
        self.is_jumping = False
        self.dash_x_distance = 0
        self.dash_y_distance = 0
        self.dash_counter = 101
        self.x_destination = 0
        self.y_destination = 0
        self.is_dashing = False
        self.dash_vector = None
        self.modified_dash_vector = None
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self)

    def update_y_value(self):
        if not self.is_dashing:
            self.rect.y -= self.jump_force
            if self.jump_force > 0 and self.is_jumping:
                self.jump_force -= 1
                if self.game.check_collision(self, self.game.all_tiles):
                    self.jump_force -= 0
                    while self.game.check_collision(self, self.game.all_tiles):
                        self.rect.y += 1
            if self.jump_force == 0:
                self.is_jumping = False
            if self.g_force_activated:
                self.rect.y += self.g_force
                if self.g_force < 10 and self.g_force_activated:
                    self.g_force += 1
            while self.game.check_collision(self, self.game.all_tiles):
                self.rect.y -= 1

    def is_touching_ground(self):
        if not self.is_dashing:
            if self.game.check_collision(self, self.game.all_tiles):
                self.g_force = 0
                self.g_force_activated = False
            else:
                self.g_force_activated = True

    def dash(self):
        if not self.is_dashing:
            self.dash_vector = (pygame.Vector2(pygame.mouse.get_pos()) - self.rect.center).normalize()
            self.modified_dash_vector = (self.dash_vector * 25)
            self.dash_counter = 0
            self.is_dashing = True

    def update_dash(self):
        if self.is_dashing:

            if self.game.check_collision(self, self.game.all_tiles):
                while self.game.check_collision(self, self.game.all_tiles):
                    self.rect.center -= self.dash_vector * 2  # (without * 2 it loop indefinitely idk why)
                self.dash_counter = 19

            if self.dash_counter <= 11:
                self.g_force_activated = False
                self.rect.center += self.modified_dash_vector
                self.dash_counter += 1

            if 13 >= self.dash_counter >= 12:
                self.g_force_activated = False
                self.rect.center += (self.modified_dash_vector / 2)
                self.dash_counter += 1

            if 14 <= self.dash_counter <= 18:
                self.g_force_activated = False
                self.dash_counter += 1

            if self.dash_counter == 19:
                self.is_dashing = False
                self.g_force_activated = True

    def jump(self):
        if not self.is_dashing:
            self.jump_force = 20
            self.is_jumping = True
            self.g_force_activated = True

    def move_right(self):
        if not self.is_dashing:
            if self.rect.x < 1600 and not self.game.check_collision(self, self.game.all_tiles):
                self.rect.x += 10
            self.trail.follow_right()
            while self.game.check_collision(self, self.game.all_tiles):
                self.rect.x -= 1

    def move_left(self):
        if not self.is_dashing:
            if self.rect.x > 0 and not self.game.check_collision(self, self.game.all_tiles):
                self.rect.x -= 10
            self.trail.follow_left()
            while self.game.check_collision(self, self.game.all_tiles):
                self.rect.x += 1


class PlayerTrail(pygame.sprite.Sprite):
    def __init__(self, game, player):
        super().__init__()
        self.game = game
        self.player = player
        self.image = pygame.image.load('assets/player_trail_left.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.player.rect.x, self.player.rect.y
        self.y_offset = 0
        self.x_offset = 0

    def follow_left(self):
        self.x_offset = 60

    def follow_right(self):
        self.x_offset = -60
