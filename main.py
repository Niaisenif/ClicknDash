import pygame as pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption('ClickNDash !')
screen = pygame.display.set_mode((1600, 996))

pygame.display.init()

from game import Game
from menu import MenuManager

game = Game(screen, -1)
MM = MenuManager()
running = True
in_start_menu = True
MM.load_menu("start")
game.is_playing, game.is_paused = False, False


while running:

    screen.fill((9, 174, 75))

    if game.is_playing:
        game.update_game()
        if not game.is_paused:
            if game.pressed.get(pygame.K_d):
                game.player.move_right()

            elif game.pressed.get(pygame.K_q):
                game.player.move_left()

            elif game.pressed.get(pygame.K_s):
                game.player.squeak()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if not game.is_paused:
                    if event.key == pygame.K_SPACE:
                        game.player.jump()
                        for enemy in game.all_enemy:
                            enemy.shoot()

                    elif event.key == pygame.K_g:
                        game.player.swap_dash()
                        game.Overlay.update_overlay()

                if event.key == pygame.K_p:
                    if game.is_paused:
                        game.is_paused = False
                    else:
                        game.is_paused = True

                else:
                    game.pressed[event.key] = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not game.is_paused:
                        game.player.dash()
                        game.Overlay.current_dash = game.player.dash_number
                        game.Overlay.update_overlay()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                if event.key == pygame.K_d or pygame.K_q:
                    game.player.trail.x_offset = 0
                if event.key == pygame.K_s:
                    game.player.un_squeak()

            if event.type == pygame.QUIT or game.player.health <= 0:
                game.is_paused = True
                player_is_dead = True
                MM.load_menu("dead")
    else:
        if in_start_menu:
            MM.all_blitted_buttons.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # noinspection PyStatementEffect
                pygame.quit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in MM.all_blitted_buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.effect == "launch_game":
                            game.is_playing = True
                            game.__init__(screen, button.effect_number)
                        if button.effect == "level_menu":
                            MM.load_menu("levels")

    pygame.display.flip()
    clock.tick(FPS)
