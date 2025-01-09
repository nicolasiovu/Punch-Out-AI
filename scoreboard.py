import config


class Scoreboard:
    def __init__(self, fighters):
        self.fighters = fighters
        self.player_x, self.player_y = 0, 0
        self.opponent_x, self.opponent_y = 1094, 0

    def render(self):
        config.window.blit(config.player_score, (self.player_x, self.player_y))
        config.window.blit(config.opponent_score, (self.opponent_x, self.opponent_y))
        text_surface = config.FONT.render(str(self.fighters.get_player_score()), False, (0, 0, 0))
        text_surface2 = config.FONT.render(str(self.fighters.get_opponent_score()), False, (0, 0, 0))
        config.window.blit(text_surface, (self.player_x + 80, self.player_y + 24))
        config.window.blit(text_surface2, (self.opponent_x + 80, self.opponent_y + 24))
