import pygame


class Overlay:

    def __init__(self, game):
        self.game = game
        self.dash_list = self.game.player.dash_list
        self.current_dash = 0
        self.all_panels = pygame.sprite.Group()
        self.update_overlay()

    def path_creator(self, place, i):
        if i == -1:
            dash = self.game.player.stored_dash
        else:
            dash_number = self.current_dash
            for x in range(i):
                dash_number += 1
                if dash_number > len(self.dash_list) - 1:
                    dash_number = 0
            dash = self.dash_list[dash_number]

        path = "assets/Dashes/"
        if place > 1:
            path += "little_"
        if dash[0] == "f":
            path += "free_"
        if dash[0] == "r":
            path += "right_"
        if dash[0] == "l":
            path += "left_"
        if dash[0] == "u":
            path += "up_"
        if dash[0] == "d":
            path += "down_"
        if dash[0] == "ru":
            path += "right-up_"
        if dash[0] == "rd":
            path += "right-down_"
        if dash[0] == "lu":
            path += "left-up_"
        if dash[0] == "ld":
            path += "left-down_"

        path += "normal.png"  # will be modified and extended
        return path

    def update_overlay(self):
        self.all_panels = pygame.sprite.Group()
        self.all_panels.add(DashPanel(self.path_creator(0, -1), 0))
        self.all_panels.add(DashPanel(self.path_creator(1, 0), 1))
        self.all_panels.add(DashPanel(self.path_creator(2, 1), 2))
        self.all_panels.add(DashPanel(self.path_creator(3, 2), 3))
        self.all_panels.add(DashPanel(self.path_creator(4, 3), 4))


class DashPanel(pygame.sprite.Sprite):

    def __init__(self, path, place):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.place = place
        if self.place == 0:
            self.rect.x, self.rect.y = 351, 16
        if self.place == 1:
            self.rect.x, self.rect.y = 501, 16
        if self.place == 2:
            self.rect.x, self.rect.y = 625, 36
        if self.place == 3:
            self.rect.x, self.rect.y = 726, 36
        if self.place == 4:
            self.rect.x, self.rect.y = 826, 36
