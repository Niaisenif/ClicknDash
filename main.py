import pygame as pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('ClickNDash !')
screen = pygame.display.set_mode((1600, 996))

pygame.display.init()

from game import Game

game = Game(screen)
play_button = pygame.image.load("assets/Play_Button.png")
play_button_rect = play_button.get_rect()
play_button_rect.x = 750
play_button_rect.y = 448
running = True

while running:

    screen.fill((9, 174, 75))

    if game.is_playing:
        game.update_game()

        if game.pressed.get(pygame.K_d):
            game.player.move_right()

        elif game.pressed.get(pygame.K_q):
            game.player.move_left()

        elif game.pressed.get(pygame.K_s):
            game.player.squeak()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.player.jump()
                    for enemy in game.all_enemy:
                        enemy.shoot()
                elif not event.key == pygame.K_SPACE:
                    game.pressed[event.key] = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game.player.dash()
                    game.Overlay.current_dash = game.player.dash_number
                    game.Overlay.update_overlay()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                if event.key == pygame.K_d or pygame.K_q:
                    game.player.trail.x_offset = 0
                if event.key == pygame.K_s:
                    game.player.unsqueak()

            if event.type == pygame.QUIT or game.player.health <= 0:
                game.is_playing = False
    else:
        screen.blit(play_button, play_button_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game.is_playing = True
                    game.__init__(screen)

    pygame.display.flip()
    clock.tick(FPS)
