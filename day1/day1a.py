with open("input", "r") as file:
    acc = 0
    for line in file:
        digit1 = ""
        digit2 = ""
        for i in range(len(line)):
            if line[i] in "0123456789":
                digit1 = line[i]
                break
        for j in range(len(line) - 1, -1, -1):
            if line[j] in "0123456789":
                digit2 = line[j]
                break
        acc += int(f"{digit1}{digit2}")
    print(acc)
                
