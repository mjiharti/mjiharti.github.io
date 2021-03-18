# -*- coding: cp1252 -*-

import params


total_amount_of_matches = 0
mark_for_user_team = '*'
league_fixture_list = []

def create_league_fixture_list(team_objects):
    """ Creates a list which contains arrays {round_number, home_team_object,
    away_team_object, home_goals, away_goals} """
    number_of_teams = len(team_objects)

    for k in range(0, params.MATCHES_AGAINST_EACH_OTHER):
        for i in range(number_of_teams - 1):
            mid = int(number_of_teams / 2)
            l1 = team_objects[:mid]
            l2 = team_objects[mid:]
            l2.reverse()
            round_number_modifier = (number_of_teams - 1) * k
            # Switch sides after each round
            if i % 2 == 1 or k % 2 == 1:
                team_pair = zip(l1, l2)
                for teams in team_pair:
                    match = [round_number_modifier + i + 1, teams[0], teams[1], 0, 0]
                    league_fixture_list.append(match)
            else:
                team_pair = zip(l2, l1)
                for teams in team_pair:
                    match = [round_number_modifier + i + 1, teams[0], teams[1], 0, 0]
                    league_fixture_list.append(match)

            team_objects.insert(1, team_objects.pop())
    return league_fixture_list

def create_cup_fixture_list():
    # TODO
    pass
