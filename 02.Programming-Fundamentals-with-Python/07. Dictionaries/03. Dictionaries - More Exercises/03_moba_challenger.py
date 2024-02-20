players_pool = {}
command = input()
while command != "Season end":
    if "->" in command:
        current_command = command.split(" -> ")
        player, position, skill = current_command[0], current_command[1], int(current_command[2])
        if player not in players_pool.keys():
            players_pool[player] = {}
        if position not in players_pool[player].keys():
            players_pool[player][position] = skill
        elif skill > players_pool[player][position]:
            players_pool[player][position] = skill

    elif "vs" in command:
        current_command = command.split(" vs ")
        player_one, player_two = current_command[0], current_command[1]
        player_to_remove = ""
        if player_one in players_pool.keys() and player_two in players_pool.keys():
            for player_one_position in players_pool[player_one].keys():
                for player_two_position in players_pool[player_two].keys():
                    if player_one_position == player_two_position:
                        if sum(players_pool[player_one].values()) > sum(players_pool[player_two].values()):
                            player_to_remove = player_two
                        elif sum(players_pool[player_one].values()) < sum(players_pool[player_two].values()):
                            player_to_remove = player_one

        if player_to_remove:
            players_pool.pop(player_to_remove)

    command = input()

players_skills = {}
for current_player in players_pool.keys():
    players_skills[current_player] = sum(players_pool[current_player].values())
players_skills = dict(sorted(players_skills.items(), key=lambda x: x[-1], reverse=True))

for player, skills in players_skills.items():
    print(f"{player}: {skills} skill")
    players_pool[player] = dict(sorted(players_pool[player].items(), key=lambda x: x[-1], reverse=True))
    for position, points in players_pool[player].items():
        print(f"- {position} <::> {points}")
