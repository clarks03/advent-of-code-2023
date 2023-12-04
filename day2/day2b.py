with open("input", "r") as file:
    acc = 0
    for line in file:
        line = line.strip()
        game = line.split(":")
        game_number = game[0][5:]

        games = game[1].strip().split(';')
        games_dict = {'red': 0, 'green': 0, 'blue': 0}

        for game in games:
            game = game.strip()
            game = game.split(',')
            for colour in game:
                colour = colour.strip()

                if "red" in colour:
                    num = colour.split(' ')
                    if int(num[0]) > games_dict['red']:
                        games_dict['red'] = int(num[0])

                elif "green" in colour:
                    num = colour.split(' ')
                    if int(num[0]) > games_dict['green']:
                        games_dict['green'] = int(num[0])

                elif "blue" in colour:
                    num = colour.split(' ')
                    if int(num[0]) > games_dict['blue']:
                        games_dict['blue'] = int(num[0])

        power = 1
        for key in games_dict:
            power *= games_dict[key]
        acc += power

    print(acc)
