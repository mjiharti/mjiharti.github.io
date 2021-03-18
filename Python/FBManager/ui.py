import os
import params

def print_header():
    print("FBManager 0.1")
    print("*************\n")

def do_user_squad_selection():
    while True:
        selection = input("PROCEED WITH A SQUAD 1 OR 2 (0=quit): ")
        if selection.isnumeric() and 1 <= int(selection) <= 2:
            break
        elif selection.isnumeric() and int(selection) == 0:
            exit()
        else:
            continue
    return selection

def do_team_selection(teams):
    print("SELECT YOUR TEAM:")
    number_of_teams = len(teams)
    for team in teams:
        print('(' + str((team.get_team_id()+1)) + ')', team.get_team_name())
    print()
    while True:
        selection = input("YOUR CHOICE 1-" + str(number_of_teams) + " (0=quit): ")
        if selection.isnumeric() and 0 <= int(selection) < (len(teams) + 1):
            return int(selection)
        else:
            continue

def print_league_fixture_list(round_number, match_list, number_of_teams, show_goals):
    """ Prints matches from certain round, round_number = 0 prints whole season """
    n = len(match_list)
    matches_per_round = number_of_teams / 2
    for i in range(0, n):
        result_string = ""
        if show_goals is True:
            result_string = "\t" + str(match_list[i][3]) + " - " + str(match_list[i][4])
        match_list_round_number = str(match_list[i][0]).ljust(2)
        if not i % matches_per_round == 0:
            match_list_round_number = "  "
        if round_number == 0:
            print(match_list_round_number, match_list[i][1].get_team_name().ljust(10), "-",
                  match_list[i][2].get_team_name().ljust(10), result_string)
        elif round_number == match_list[i][0]:
            print(match_list_round_number, match_list[i][1].get_team_name().ljust(10), "-",
                  match_list[i][2].get_team_name().ljust(10), result_string)

def print_league_table(division, teams):
    """ Prints league table ordered by points """
    temp_teams = teams.copy()
    table_header = division == 0 and params.DIVISION_0_NAME + " TABLE" or "DIVISION " + str(division) + " TABLE"
    print("\n" + table_header)
    for j in range(0, len(temp_teams)):
        for k in range(j+1, len(temp_teams)):
            stats_j = temp_teams[j].get_team_stats()
            stats_k = temp_teams[k].get_team_stats()
            if stats_k.get_season_points() > stats_j.get_season_points():
                temp = temp_teams[j]
                temp_teams[j] = temp_teams[k]
                temp_teams[k] = temp
                print(teams[temp_teams[k].get_team_id()].get_team_name(), temp_teams[k].get_team_name(),
                      teams[temp_teams[j].get_team_id()].get_team_name(), temp_teams[j].get_team_name())
                teams[temp_teams[k].get_team_id()].get_team_stats().set_current_season_position(j+1)
                teams[temp_teams[j].get_team_id()].get_team_stats().set_current_season_position(k+1)
            elif stats_k.get_season_points() == stats_j.get_season_points():
                goal_diff_k = stats_k.get_season_goals() - stats_k.get_season_goals_against()
                goal_diff_j = stats_j.get_season_goals() - stats_j.get_season_goals_against()
                if goal_diff_k > goal_diff_j:
                    temp = temp_teams[j]
                    temp_teams[j] = temp_teams[k]
                    temp_teams[k] = temp
                    teams[temp_teams[k].get_team_id()].get_team_stats().set_current_season_position(j+1)
                    teams[temp_teams[j].get_team_id()].get_team_stats().set_current_season_position(k+1)

    # TODO set teams season positions correctly
    print("".ljust(10) + "\t", "P   W   D   L   GS  GA  GD  Pts")
    print("------------------------------------------------")
    for i in temp_teams:
        stats_object = i.get_team_stats()
        print(i.get_team_name().ljust(10) + "\t", str(stats_object.get_season_games_played()).ljust(3),
              str(stats_object.get_season_wins()).ljust(3),
              str(stats_object.get_season_draws()).ljust(3), str(stats_object.get_season_losses()).ljust(3),
              str(stats_object.get_season_goals()).ljust(3), str(stats_object.get_season_goals_against()).ljust(3),
              str(stats_object.get_season_goals() - stats_object.get_season_goals_against()).ljust(3),
              str(stats_object.get_season_points()).ljust(3))
    print("------------------------------------------------")

def clear_ui():
    os.system('cls')
