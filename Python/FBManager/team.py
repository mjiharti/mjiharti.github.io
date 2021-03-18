import params
import random
import team_stats


def get_random_fit_change():
    return random.randint(1, params.MAX_FIT_DECREASE)

class Team:
    name = "NO_NAME"
    team_id = "NO_ID"
    first_squad_skill = -1
    second_squad_skill = -1
    is_user_team = False
    first_squad_fit = params.MAX_FIT
    second_squad_fit = params.MAX_FIT

    def __init__(self, team_id, name, first_squad_skill, second_squad_skill):
        self.team_id = team_id
        self.name = name
        self.first_squad_skill = first_squad_skill
        self.second_squad_skill = second_squad_skill
        self.stats = team_stats.TeamStats()

    def print_info(self):
        print(self.team_id, self.name, "\tskill1:", self.first_squad_skill, "\tskill2:", self.second_squad_skill,
              "\tfit1:", self.first_squad_fit, "\tfit2:", self.second_squad_fit, "\tWDL:", self.stats.get_season_wins(),
              "-", self.stats.get_season_draws(), "-", self.stats.get_season_losses(), "points:",
              self.stats.get_season_points())

    def print_short_info(self):
        temp = self.name
        if self.is_user_team is True:
            temp = self.name[1:]
        print(temp + ',', "Squad 1 fit:", self.first_squad_fit,
              "%, Squad 2 fit:", self.second_squad_fit, '%.')

    def decrease_or_increase_squad_fit(self, is_first_squad, is_increase):
        if is_increase:
            if is_first_squad:
                self.first_squad_fit += get_random_fit_change()
                if self.first_squad_fit > params.MAX_FIT:
                    self.first_squad_fit = params.MAX_FIT
            else:
                self.second_squad_fit += get_random_fit_change()
                if self.second_squad_fit > params.MAX_FIT:
                    self.second_squad_fit = params.MAX_FIT
        else:
            if is_first_squad:
                self.first_squad_fit -= get_random_fit_change()
                if self.first_squad_fit < params.MIN_FIT:
                    self.first_squad_fit = params.MIN_FIT
            else:
                self.second_squad_fit -= get_random_fit_change()
                if self.second_squad_fit < params.MIN_FIT:
                    self.second_squad_fit = params.MIN_FIT

    def reset_fit(self):
        self.first_squad_fit = params.MAX_FIT
        self.second_squad_fit = params.MAX_FIT

    def get_first_squad_skill(self):
        return self.first_squad_skill

    def get_second_squad_skill(self):
        return self.second_squad_skill

    def get_first_squad_fit(self):
        return self.first_squad_fit

    def get_second_squad_fit(self):
        return self.second_squad_fit

    def get_team_name(self):
        return self.name

    def get_team_id(self):
        return self.team_id

    def return_is_user_team(self):
        return self.is_user_team

    def set_user_team(self):
        self.is_user_team = True
        self.name = '*' + self.name

    def get_team_stats(self):
        return self.stats
