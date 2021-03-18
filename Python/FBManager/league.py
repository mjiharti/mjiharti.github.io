import params
import ui
import random

def run_matches(season_fixture_list, team_objects, selected_user_team):
    number_of_rounds = (len(team_objects) - 1) * params.MATCHES_AGAINST_EACH_OTHER

    for current_round in range(1, number_of_rounds + 1):
        ui.print_league_table(0, team_objects)
        print("NEXT MATCHES:")
        ui.print_league_fixture_list(current_round, season_fixture_list, len(team_objects), False)
        print()
        print(team_objects[selected_user_team - 1].get_team_stats().get_current_season_position())
        team_objects[selected_user_team - 1].print_short_info()
        squad_selection = ui.do_user_squad_selection()

        for i in season_fixture_list:
            if i[0] == current_round:
                # TODO User team matches handling
                home_skill = i[1].get_first_squad_skill()
                home_first_squad = True
                home_fit = i[1].get_first_squad_fit()

                if (i[1].return_is_user_team() is True and squad_selection == '2') or \
                        (i[1].return_is_user_team() is not True and
                         (i[1].get_second_squad_fit() > i[1].get_first_squad_fit())):
                    home_skill = i[1].get_second_squad_skill()
                    home_fit = i[1].get_second_squad_fit()
                    home_first_squad = False

                visitor_skill = i[2].get_first_squad_skill()
                visitor_first_squad = True
                visitor_fit = i[2].get_first_squad_fit()

                if (i[2].return_is_user_team() is True and squad_selection == '2') or \
                        (i[2].return_is_user_team() is not True and
                         (i[2].get_second_squad_fit() > i[2].get_first_squad_fit())):
                    visitor_skill = i[2].get_second_squad_skill()
                    visitor_fit = i[2].get_second_squad_fit()
                    visitor_first_squad = False

                home_goals = 0
                visitor_goals = 0
                for goal_h in range(1, home_skill):
                    rnd = (100 / home_fit) * random.randint(1, 100)
                    if rnd <= params.HOME_TEAM_GOAL_CHANCE:
                        home_goals += 1
                for goal_v in range(1, visitor_skill):
                    rnd = (100 / visitor_fit) * random.randint(1, 100)
                    if rnd <= params.VISITOR_TEAM_GOAL_CHANCE:
                        visitor_goals += 1

                do_fit_changes(i[1], i[2], home_first_squad, visitor_first_squad)

                home_stats = i[1].get_team_stats()
                visitor_stats = i[2].get_team_stats()
                update_stats(home_stats, visitor_stats, home_goals, visitor_goals)

                # i[1].print_info()
                # i[2].print_info()
                i[3] = home_goals
                i[4] = visitor_goals
                # print("home", home_goals, "visitor", visitor_goals)

        current_round += 1
        # ui.print_league_fixture_list(0, season_fixture_list, len(team_objects), True)
    ui.print_league_table(0, team_objects)
    print("END OF SEASON!")

def update_stats(home_stats, visitor_stats, home_goals, visitor_goals):
    if home_goals > visitor_goals:
        home_stats.add_season_game_win(home_goals, visitor_goals)
        visitor_stats.add_season_game_loss(visitor_goals, home_goals)
    elif visitor_goals > home_goals:
        visitor_stats.add_season_game_win(visitor_goals, home_goals)
        home_stats.add_season_game_loss(home_goals, visitor_goals)
    else:
        home_stats.add_season_game_draw(home_goals, visitor_goals)
        visitor_stats.add_season_game_draw(home_goals, visitor_goals)

def do_fit_changes(home_team, visitor_team, home_first_squad, visitor_first_squad):
    if home_first_squad is True:
        home_team.decrease_or_increase_squad_fit(True, False)
        home_team.decrease_or_increase_squad_fit(False, True)
    else:
        home_team.decrease_or_increase_squad_fit(False, False)
        home_team.decrease_or_increase_squad_fit(True, True)
    if visitor_first_squad is True:
        visitor_team.decrease_or_increase_squad_fit(True, False)
        visitor_team.decrease_or_increase_squad_fit(False, True)
    else:
        visitor_team.decrease_or_increase_squad_fit(False, False)
        visitor_team.decrease_or_increase_squad_fit(True, True)
