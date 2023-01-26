class GameStats():
    """отслеживание статистики"""

    def __init__(self, ai_game):
        """инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.score = 160
        pass