with open("input", "r") as file:
    acc = 0
    for line in file:
        print(line)
        line = line.strip()
        game = line.split(":")
        game_number = game[0][5:]

        games = game[1].strip().split(';')
        print(games)
        is_invalid = False
        for game in games:
            game = game.strip()
            game = game.split(',')
            for colour in game:
                colour = colour.strip()
                print(colour)

                if "red" in colour:
                    num = colour.split(' ')
                    if int(num[0]) > 12:
                        is_invalid = True
                        break

                elif "green" in colour:
                    num = colour.split(' ')
                    if int(num[0]) > 13:
                        is_invalid = True
                        break

                elif "blue" in colour:
                    num = colour.split(' ')
                    if int(num[0]) > 14:
                        is_invalid = True
                        break

            if is_invalid:
                break
        if not is_invalid:
            acc += int(game_number)

    print(acc)
