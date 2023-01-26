
import pygame.font


class Timer():
    def __init__(self, ai_game, counter, xpos, ypos):
        self.screen = ai_game.screen
        """инициализация таймера"""
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.counter = counter
        self.xpos = xpos
        self.ypos = ypos
        self.mins, self.secs = (divmod(self.counter, 60))
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()

    """def stats_score_update(self):
        if self.event.type == pygame.USEREVENT:
            self.counter -= 1
            self.mins, self.secs = divmod(self.counter, 60)
        self.stats.score = '{:02d}:{:02d}'.format(self.mins, self.secs) if self.counter > 0 else 'boom!'
        print(self.stats.score)"""
    def prep_score(self):
        self.mins, self.secs = divmod(self.counter, 60)
        score_str = str('{:02d}:{:02d}'.format(self.mins, self.secs))

        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.xpos
        self.score_rect.top = self.ypos

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
