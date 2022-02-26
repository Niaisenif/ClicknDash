import pygame


class MenuManager:

    def __init__(self):
        self.all_blitted_buttons = pygame.sprite.Group()

    def load_menu(self, menu):
        if menu == "start":
            self.all_blitted_buttons = pygame.sprite.Group()
            self.all_blitted_buttons.add(Button("assets/Play_Button.png", (800, 498), "level_menu", 0))
        if menu == "levels":
            self.all_blitted_buttons = pygame.sprite.Group()
            self.all_blitted_buttons.add(Button("assets/Play_Button.png", (600, 298), "launch_game", 0),
                                         Button("assets/Play_Button.png", (1000, 298), "launch_game", 0),
                                         Button("assets/Play_Button.png", (600, 698), "launch_game", 0),
                                         Button("assets/Play_Button.png", (1000, 698), "launch_game", 0))


class Button(pygame.sprite.Sprite):

    def __init__(self, path, rect, effect, effect_number):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = rect
        self.effect = effect
        self.effect_number = effect_number
