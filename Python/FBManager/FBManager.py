# -*- coding: cp1252 -*-

import params
import team
import fixture_list
import ui
import league


# TODO read teams from file
teams = params.DIVISION_1_TEAMS
team_objects = []

def main():

    for index, i in enumerate(teams):
        new_team = team.Team(index, i[0], i[1], i[2])
        team_objects.append(new_team)

    ui.print_header()
    selected_user_team = ui.do_team_selection(team_objects)
    if selected_user_team == 0:
        exit()
    else:
        team_objects[selected_user_team-1].set_user_team()

    season_fixture_list = fixture_list.create_league_fixture_list(team_objects)
    league.run_matches(season_fixture_list, team_objects, selected_user_team)

if __name__ == "__main__":
    main()
