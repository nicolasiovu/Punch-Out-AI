import config


class Scoreboard:
    def __init__(self, fighters):
        self.fighters = fighters
        self.player_x, self.player_y = 0, 0
        self.opponent_x, self.opponent_y = 1094, 0
        self.info_x, self.info_y = 540, 0
        self.round = 1
        self.round_scoring = [(0, 0), (0, 0), (0, 0), (0, 0)]
        self.timer = 180

    def tick_timer(self):
        self.timer -= 1

    def next_round(self):
        self.timer = 180
        self.round_scoring[self.round - 1] = \
            (self.fighters.get_player_score(), self.fighters.get_opponent_score())
        self.round += 1
        self.fighters.next_round()

    def render(self):
        config.window.blit(config.player_score, (self.player_x, self.player_y))
        config.window.blit(config.opponent_score, (self.opponent_x, self.opponent_y))
        config.window.blit(config.info_display, (self.info_x, self.info_y))

        player_score = config.FONT.render(str(self.fighters.get_player_score()), False, (0, 0, 0))
        opponent_score = config.FONT.render(str(self.fighters.get_opponent_score()), False, (0, 0, 0))

        minutes = self.timer // 60
        seconds = self.timer % 60
        timer_surface = config.FONT.render(f"{minutes}:{seconds:02}", False, (231, 255, 222))

        config.window.blit(player_score, (self.player_x + 80, self.player_y + 24))
        config.window.blit(opponent_score, (self.opponent_x + 80, self.opponent_y + 24))
        config.window.blit(timer_surface, (self.info_x + 55, self.info_y + 3))
        config.window.blit(config.round_numbers.get(self.round), (self.info_x + 60, self.info_y + 52))

