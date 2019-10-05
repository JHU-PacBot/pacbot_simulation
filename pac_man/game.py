from pac_man.graphics import *
from pac_man.gameState import *
import schedule

game_state = GameState()


def update_game():
    if not game_state.play:
        game_state.next_step()


schedule.every(0.5).seconds.do(update_game)

print("Welcome to PyGame!")

pygame.init()
game_display = pygame.display.set_mode((560, 620))

pygame.display.set_caption("Game")

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_state.pacbot.direction = left
            elif event.key == pygame.K_RIGHT:
                game_state.pacbot.direction = right
            elif event.key == pygame.K_DOWN:
                game_state.pacbot.direction = down
            elif event.key == pygame.K_UP:
                game_state.pacbot.direction = up
            elif event.key == pygame.K_SPACE:
                game_state.play = not game_state.play
    game_display.fill((0, 0, 0))
    print_maze(game_display, game_state)
    print_ghosts(game_display, game_state)
    print_pac_man(game_display, game_state)
    print_score_and_lives(game_display, game_state)
    schedule.run_pending()
    pygame.display.update()

pygame.quit()
quit()
