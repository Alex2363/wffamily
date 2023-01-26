import pygame.font

class Button():

    def __init__(self, wf_game, msg):

        self.screen = wf_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 100, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20)

        self.rect = pygame.Rect(400, 0, self.width, self.height)
        self.rect.x = self.screen_rect.centerx - self.width//2
        self.rect.y = self.screen_rect.top + self.height//2

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """преобразует сообщение в прямоугольник и выравнивает текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        #Отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



