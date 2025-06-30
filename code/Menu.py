import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_PURPLE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    # Constructor for the window and sets menu background
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # Loop that initiates the menu and sets soundtrack
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Projeto', C_PURPLE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'GAME', C_PURPLE, ((WIN_WIDTH / 2), 120))

            # Sets menu options, play or exit in cons.py
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
                # Menu selection through the keyboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # UPPER KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option -= 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    # Specific text characteristics
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)