import sys
import pygame


class Minesweeper():

    def __init__(self):
        pygame.init()

        # Set size of game screen
        self.screen = pygame.display.set_mode((250, 320))
        pygame.display.set_caption("Minesweeper")

    def run_game(self):

        while True:
            # Listen for user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show the most recently drawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    game = Minesweeper()
    game.run_game()