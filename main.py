import pygame
import sys
import random


from settings import Settings

from game_stats import GameStats
from button import Button
from timer import Timer
from gamers import Gamer
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
class Wffamily:
    """Класс для управления ресурсами и поведением игры"""


    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.settings = Settings()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("wffamily")
        self.stats = GameStats(self)


        #self.gamer = Gamer(self, (0, 0, 0), 10, 10, 1)

        self.gamers = pygame.sprite.Group()

        self._create_comand()




        self.play_button = Button(self, "Конец хода")
        self.timer1 = Timer(self, self.settings.counter_timer1, self.settings.screen_width // 2 + 150, 40)
        self.timer2 = Timer(self, self.settings.counter_timer2, self.settings.screen_width // 2 - 150, 40)
        self.width, self.height = self.settings.screen_width - 200, self.settings.screen_height - 140
        self.surf = pygame.Surface((self.width, self.height))
        self.surf_pol = pygame.Surface((self.width - 150, self.height - 80))
        self.surf_pol.set_alpha(150)
        #print(self.width, self.height)
        self.surf.fill((0, 0, 255))
        self.surf_pol.fill((0, 160, 160))
        #self.width_p, self.height_p = ((self.width - 100) // 4), ((self.height - 40) // 3)

        #print(self.width_p, self.height_p)
        """ Рисуем поле """
        for y in range(0, self.surf_pol.get_height(), self.surf_pol.get_height() // 3):

            for x in range(0, self.surf_pol.get_width(), self.surf_pol.get_width() // 4):

                rect = (x, y, self.surf_pol.get_width() // 4, self.surf_pol.get_height() // 3)
                pygame.draw.rect(self.surf_pol, (255, 255, 255), rect, 1)

        #pygame.draw.circle(self.surf_pol, (0, 0, 0), (250, 350), 40)
    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            #self.gamer.update()

            self._update_screen()
    def _check_events(self):
            #отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # переместить игрока вправо
                    self.gamer.moving_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.gamer.moving_right = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #print(mouse_pos)
                self._check_play_button(mouse_pos)
                """self._check_go_gamer(mouse_pos)"""


            elif event.type == pygame.USEREVENT:
                self.timer1.counter -= 1
                if self.timer1.counter <= 0:
                    self.timer1.counter = self.settings.counter_timer1
                    print('BooV!!!')
                self.timer2.counter -= 1
                if self.timer2.counter <= 0:
                    sys.exit()

                self.timer1.prep_score()
                self.timer2.prep_score()
        self.clock.tick(self.FPS)


    def _check_play_button(self, mouse_pos):
        """Если курсор мыши на кнопке"""
        if self.play_button.rect.collidepoint(mouse_pos):
            print("bum!!!")



    def _create_comand(self):
        """Создание команды одного игрока"""
        gamer = Gamer(self, BLACK, 20, 20)
        gamer_width = gamer.rect.width

        # Создание команды
        for gamer_number in range(1, 12):
            gamer = Gamer(self, RED, 20, 20)
            gamer.x = gamer_width + 150 + (gamer_width + 10) * gamer_number
            #print(gamer.x)
            gamer.rect.x = gamer.x
            self.gamers.add(gamer)
            print(len(self.gamers))
    """Выбор игрока"""
    """def _check_go_gamer(self, mouse_pos):
        mx, my = pygame.mouse.get_pos()
        mb1, mb2, mb3 = pygame.mouse.get_pressed()
        for i in range(len(self.gamers)):
            self.g = self.gamers[i]
            if mb1 and (self.g[0] - mx) ** 2 + (self.g[1] - my) ** 2 < 15 ** 2:
                color = 'black'
                #print(g)
                self.g[0] = mx
                self.g[1] = my
            #print(self.g)
            #if self.g.collidepoint(mouse_pos):
                print('XLOP!!!!')
            # self.gamer.color = (0, 0, 50)
            # print(self.gamers.color)"""


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.screen.blit(self.surf, (100, 100))
        self.surf.blit(self.surf_pol, (75, 40))
        #x = 200
        #num = 1
        #block_list = pygame.sprite.Group()

        """for num in range(1, 12):
            self.gamer = Gamer(BLACK, 50, 50, 70)
            self.gamer.rect.x = random.randrange(900)
            self.gamer.rect.y = random.randrange(500)

            print(self.gamer.rect.x, self.gamer.rect.y)
            block_list.add(self.gamer)
            print((block_list))
            block_list.draw(self.screen)"""
            #self.gamer.blitme()
        #print(self.gamer.gamer_color)
        self.play_button.draw_button()
        self.timer1.show_score()
        self.timer2.show_score()
        self.gamers.draw(self.screen)

                # отображение последнего прорисованого экрана.
        pygame.display.flip()
if __name__ == '__main__':
    # создание экземпляра и запуск игры
    wf = Wffamily()
    wf.run_game()