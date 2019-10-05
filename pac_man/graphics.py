from pac_man.gameState import *
import pygame

red_hue = (255, 0, 0)
pink_hue = (255, 192, 203)
blue_hue = (0, 255, 255)
frightened_hue = (0, 0, 255)
orange_hue = (255, 165, 0)
black_hue = (0, 0, 0)
yellow_hue = (255, 255, 153)
pac_man_hue = (204, 204, 0)

unit_size = 20


def print_maze(game_display, game_state):
    grid = game_state.grid
    for row_index in range(0, 28):
        for col_index in range(0, 31):
            if grid[row_index][col_index] == I:
                pygame.draw.rect(game_display, frightened_hue,
                                 [row_index * unit_size, 600 - col_index * unit_size, unit_size, unit_size])
            elif grid[row_index][col_index] == o:
                pygame.draw.circle(game_display, yellow_hue,
                                 [row_index * unit_size + int(unit_size / 2), 600 - col_index * unit_size + int(unit_size / 2)]
                                  , int(unit_size / 4))
            elif grid[row_index][col_index] == O:
                pygame.draw.circle(game_display, yellow_hue,
                                 [row_index * unit_size + int(unit_size / 2), 600 - col_index * unit_size + int(unit_size / 2)]
                                  , int(unit_size / 2.5))


def print_ghosts(game_display, game_state):
    red_x = game_state.red.pos["current"][0]
    red_y = game_state.red.pos["current"][1]
    pink_x = game_state.pink.pos["current"][0]
    pink_y = game_state.pink.pos["current"][1]
    blue_x = game_state.blue.pos["current"][0]
    blue_y = game_state.blue.pos["current"][1]
    orange_x = game_state.orange.pos["current"][0]
    orange_y = game_state.orange.pos["current"][1]

    red_ghost_color = red_hue
    if game_state.red.frightened_counter > 0:
        red_ghost_color = frightened_hue
    pink_ghost_color = pink_hue
    if game_state.pink.frightened_counter > 0:
        pink_ghost_color = frightened_hue
    blue_ghost_color = blue_hue
    if game_state.blue.frightened_counter > 0:
        blue_ghost_color = frightened_hue
    orange_ghost_color = orange_hue
    if game_state.orange.frightened_counter > 0:
        orange_ghost_color = frightened_hue

    pygame.draw.circle(game_display, red_ghost_color,
                       [red_x * unit_size + int(unit_size / 2), 600 - red_y * unit_size + int(unit_size / 2)]
                       , int(unit_size / 2.5))
    pygame.draw.circle(game_display, pink_ghost_color,
                       [pink_x * unit_size + int(unit_size / 2), 600 - pink_y * unit_size + int(unit_size / 2)]
                       , int(unit_size / 2.5))
    pygame.draw.circle(game_display, blue_ghost_color,
                       [blue_x * unit_size + int(unit_size / 2), 600 - blue_y * unit_size + int(unit_size / 2)]
                       , int(unit_size / 2.5))
    pygame.draw.circle(game_display, orange_ghost_color,
                       [orange_x * unit_size + int(unit_size / 2), 600 - orange_y * unit_size + int(unit_size / 2)]
                       , int(unit_size / 2.5))


def print_pac_man(game_display, game_state):
    pac_man_x = game_state.pacbot.pos[0]
    pac_man_y = game_state.pacbot.pos[1]
    pygame.draw.circle(game_display, pac_man_hue,
                       [pac_man_x * unit_size + int(unit_size / 2), 600 - pac_man_y * unit_size + int(unit_size / 2)]
                       , int(unit_size / 2.5))

def print_score_and_lives(game_display, game_state):
    font = pygame.font.Font('freesansbold.ttf', 18)

    score_text = font.render("Score: " + str(game_state.score), True, yellow_hue, blue)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (50, 300)
    game_display.blit(score_text, score_text_rect)

    lives_text = font.render("Lives: " + str(game_state.lives), True, yellow_hue, blue)
    lives_text_rect = lives_text.get_rect()
    lives_text_rect.center = (510, 300)
    game_display.blit(lives_text, lives_text_rect)
