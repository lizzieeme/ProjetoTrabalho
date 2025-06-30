import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    # Constructor for initiating the game with pygame and setting the window dimensions
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # Loop for showing the menu while the game is playing
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            else:
                if MENU_OPTION[1]:
                    pygame.quit() # Close window
                    quit() # end pygame



