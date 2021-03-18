import params

class TeamStats:

    number_of_seasons = 0
    season_goals = 0
    season_goals_against = 0
    season_wins = 0
    season_draws = 0
    season_losses = 0
    season_points = 0
    season_games_played = 0
    current_season_position = 0

    all_time_goals = 0
    all_time_goals_against = 0
    all_time_wins = 0
    all_time_draws = 0
    all_time_losses = 0
    all_time_points = 0
    all_time_games_played = 0

    def get_number_of_seasons(self):
        return self.number_of_seasons

    def get_season_goals(self):
        return self.season_goals

    def get_season_goals_against(self):
        return self.season_goals_against

    def get_season_wins(self):
        return self.season_wins

    def get_season_draws(self):
        return self.season_draws

    def get_season_losses(self):
        return self.season_losses

    def get_season_points(self):
        return self.season_points

    def get_season_games_played(self):
        return self.season_games_played

    def get_all_time_goals(self):
        return self.all_time_goals

    def get_all_time_goals_against(self):
        return self.all_time_goals_against

    def get_all_time_wins(self):
        return self.all_time_wins

    def get_all_time_draws(self):
        return self.all_time_draws

    def get_all_time_lost(self):
        return self.all_time_losses

    def get_all_time_points(self):
        return self.all_time_points

    def get_all_time_games_played(self):
        return self.all_time_games_played

    def add_season_game_win(self, goals, goals_against):
        self.season_goals += goals
        self.season_goals_against += goals_against
        self.season_wins += 1
        self.season_points += params.POINTS_FOR_WIN
        self.all_time_wins += 1
        self.all_time_points += params.POINTS_FOR_WIN
        self.season_games_played += 1
        self.all_time_games_played += 1
        self.all_time_goals += goals
        self.all_time_goals_against += goals_against

    def add_season_game_draw(self, goals, goals_against):
        self.season_goals += goals
        self.season_goals_against += goals_against
        self.season_draws += 1
        self.season_points += params.POINTS_FOR_DRAW
        self.all_time_draws += 1
        self.all_time_points += params.POINTS_FOR_DRAW
        self.season_games_played += 1
        self.all_time_games_played += 1
        self.all_time_goals += goals
        self.all_time_goals_against += goals_against

    def add_season_game_loss(self, goals, goals_against):
        self.season_goals += goals
        self.season_goals_against += goals_against
        self.season_losses += 1
        self.season_points += params.POINTS_FOR_LOSS
        self.all_time_losses += 1
        self.all_time_points += params.POINTS_FOR_LOSS
        self.season_games_played += 1
        self.all_time_games_played += 1
        self.all_time_goals += goals
        self.all_time_goals_against += goals_against

    def set_current_season_position(self, position):
        print("update position,", self.current_season_position, "to", position)
        self.current_season_position = position

    def get_current_season_position(self):
        return self.current_season_position
