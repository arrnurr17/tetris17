from tetris.game import TetrisGame
from tetris.constants import FPS

def main():
    game = TetrisGame()
    running = True

    while running:
        game.clock.tick(FPS)
        running = game.handle_input()
        game.update()
        game.render()

if __name__ == "__main__":
    main()