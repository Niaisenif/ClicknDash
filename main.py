import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('Platformer attempt')
screen = pygame.display.set_mode((1600, 896))

pygame.display.init()

from game import Game

game = Game(screen)

running = True

while running:

    screen.fill((255, 255, 255))

    game.update_game()

    if game.pressed.get(pygame.K_d):
        game.player.move_right()

    elif game.pressed.get(pygame.K_q):
        game.player.move_left()

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.jump()
            elif not event.key == pygame.K_SPACE:
                game.pressed[event.key] = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game.player.dash()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            if event.key == pygame.K_d or pygame.K_q:
                game.player.trail.x_offset = 0

        elif event.type == pygame.QUIT:
            running = False
            pygame.quit

    pygame.display.flip()
    clock.tick(FPS)
