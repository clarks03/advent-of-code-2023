nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open("input", "r") as file:
    acc = 0
    for line in file:
        line = line.strip()

        digit1 = ""
        for i in range(len(line)):

            # number
            if line[i] in "0123456789":
                digit1 = line[i]
                break

            # alphanumeric
            if_found = False
            for j in range(3, 6):
                if line[i:i+j] in nums:
                    digit1 = str(nums.index(line[i:i+j]) + 1)
                    if_found = True
                    break
            if if_found:
                if_found = False
                break

        digit2 = ""
        for i in range(len(line) - 1, -1, -1):

            # number
            if line[i] in "0123456789":
                digit2 = line[i]
                break

            # alphanumeric
            if_found = False
            for j in range(3, 6):
                print(line[i-j+1:i+1])
                if line[i-j+1:i+1] in nums:
                    print("Winner!")
                    digit2 = str(nums.index(line[i-j+1:i+1]) + 1)
                    if_found = True
                    break

            if if_found:
                if_found = False
                break
        
        print(f"{line}, {digit1}, {digit2}")
        acc += int(f"{digit1}{digit2}")

    print(acc)

        



            

