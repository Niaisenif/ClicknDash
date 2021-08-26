import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if not loop:
                    self.animation = False
            self.image = self.images[self.current_image]


def load_animation_images(sprite_name, number_of_images):
    images = []
    path = f'assets/{sprite_name}/{sprite_name}'
    for num in range(1, number_of_images):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    return images


animations = {
    'projectile': load_animation_images('projectile', 2)
}
