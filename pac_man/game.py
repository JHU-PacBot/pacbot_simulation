from graphics import *
from gameState import *
import schedule
import sys

# Usage: python game.py num
# where num is the number of runs you want to do (default 1)
# set allow_display to true to watch pacman

allow_display = True #set to True to watch the pacman
scores = []

def update_game(game_state):
    if not game_state.play:
        game_state.next_step()

def main():
    game_state = GameState()

    update = lambda : update_game(game_state) if not game_state.kill else schedule.CancelJob

    if allow_display:
        schedule.every(0.05).seconds.do(update)
    else:
        schedule.every(0.00001).seconds.do(update)

    if allow_display:
        pygame.init()
        game_display = pygame.display.set_mode((560, 620))

        pygame.display.set_caption("Game")

    gameExit = False

    while not gameExit:
        if allow_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
        if game_state.kill:
            scores.append(game_state.score)
            gameExit = True
        if allow_display:
            game_display.fill((0, 0, 0))
            print_maze(game_display, game_state)
            print_ghosts(game_display, game_state)
            print_pac_man(game_display, game_state)
            print_score_and_lives(game_display, game_state)
        schedule.run_pending()
        if allow_display:
            pygame.display.update()

    if allow_display:
        pygame.quit()
    # quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        times = int(sys.argv[1])
    else:
        times = 1
    for i in range(times):
        print('Run {}'.format(i+1))
        main()
    print('Average score: {}'.format(sum(scores)/len(scores)))
    quit()
