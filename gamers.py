import pygame
from pygame.sprite import Sprite

class Gamer(Sprite):
    """Класс представляющий одного игрока"""
    def __init__(self, wf_game, color, width, height):
        """Инициирует игрока и задает начальную позицию"""
        super().__init__()
        self.screen = wf_game.screen
        """рисуем игрока """
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + 150
        self.rect.y = self.rect.height + 510

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #print(self.x, self.y)
