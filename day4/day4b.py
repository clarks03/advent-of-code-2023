with open("input", "r") as file:
    # now we need a dict for duplicate cards
    duplicate_dict = {i: 1 for i in list(range(1, 209))}

    for line in file:
        # this is where we will store duplicate cards for the current game
        duplicate_cards = 1

        line = line.strip()

        # getting the game number
        game_number = int(line.split(":")[0].strip().split(' ')[-1])

        # removing the card column, getting the list of numbers
        numbers = line.split(":")[1].strip()

        # splitting the numbers into winning numbers and user numbers
        winning_numbers = numbers.split("|")[0].strip().split(' ')
        your_numbers = numbers.split("|")[1].strip().split(' ')

        # determining winning numbers (number of scratch cards)
        for number in your_numbers:

            # sometimes double spaces occur; this gets rid of them (in a stupid way, to be fair)
            if number == "":
                continue

            # if we duplicate a card
            if number in winning_numbers:

                # NOTE: we only duplicate cards up until 209.
                if game_number + duplicate_cards > 209:
                    continue

                # adding duplicate cards for the next card numbers depending on the number of cards we currently have
                duplicate_dict[game_number + duplicate_cards] += duplicate_dict[game_number]
                duplicate_cards += 1

    # now we sum up all of the entries in duplicate_dict!
    acc = 0
    for key in duplicate_dict:
        acc += duplicate_dict[key]
    print(acc)





