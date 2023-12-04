with open("input", "r") as file:
    acc = 0
    for line in file:
        line = line.strip()

        # defining score
        score = 0

        # removing the card column, getting the list of numbers
        numbers = line.split(":")[1].strip()

        # splitting the numbers into winning numbers and user numbers
        winning_numbers = numbers.split("|")[0].strip().split(' ')
        your_numbers = numbers.split("|")[1].strip().split(' ')

        # determining winning numbers
        for number in your_numbers:

            # sometimes double spaces occur; this gets rid of them (in a stupid way, to be fair)
            if number == "":
                continue

            if number in winning_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        # adding the score of this card to the accumulator
        acc += score
    # printing out the acc
    print(acc)



