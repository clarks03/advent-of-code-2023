with open("input", "r") as file:
    lines = file.read().split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    lines.pop(-1)
    acc = 0
    seen_coords = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] not in '0123456789.':  # character is a special symbol
                is_valid_gear = False
                gear_ratio_nums = []
                if lines[y][x] == "*":
                    is_valid_gear = True
                # look in adjacent squares

                # up
                if y - 1 >= 0 and lines[y - 1][x] in '0123456789' and (x, y - 1) not in seen_coords:

                    num = str(lines[y - 1][x])
                    seen_coords.append((x, y-1))
                    temp_x = x
                    while temp_x - 1 >= 0 and lines[y - 1][temp_x - 1] in '0123456789':
                        num = str(lines[y - 1][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y-1))
                        temp_x -= 1

                    temp_x = x
                    while temp_x + 1 <= len(lines[y - 1]) - 1 and lines[y - 1][temp_x + 1] in "0123456789":
                        num += str(lines[y - 1][temp_x + 1])
                        seen_coords.append((temp_x + 1, y-1))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False


                # down
                if y + 1 <= len(lines) - 1 and lines[y + 1][x] in '0123456789' and (x, y + 1) not in seen_coords:

                    num = str(lines[y + 1][x])
                    seen_coords.append((x, y+1))
                    temp_x = x
                    while temp_x - 1 >= 0 and lines[y + 1][temp_x - 1] in '0123456789':
                        num = str(lines[y + 1][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y+1))
                        temp_x -= 1

                    temp_x = x
                    while temp_x + 1 <= len(lines[y + 1]) - 1 and lines[y + 1][temp_x + 1] in "0123456789":
                        num += lines[y + 1][temp_x + 1]
                        seen_coords.append((temp_x + 1, y+1))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                # left
                if x - 1 >= 0 and lines[y][x - 1] in '0123456789' and (x - 1, y) not in seen_coords:

                    num = str(lines[y][x - 1])
                    seen_coords.append((x - 1, y))
                    temp_x = x - 1
                    while temp_x - 1 >= 0 and lines[y][temp_x - 1] in '0123456789':
                        num = str(lines[y][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y))
                        temp_x -= 1

                    temp_x = x - 1
                    while temp_x + 1 <= len(lines[y]) - 1 and lines[y][temp_x + 1] in "0123456789":
                        num += str(lines[y][temp_x + 1])
                        seen_coords.append((temp_x + 1, y))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                # right
                if x + 1 <= len(lines[y]) - 1 and lines[y][x + 1] in '0123456789' and (x + 1, y) not in seen_coords:

                    num = str(lines[y][x + 1])
                    seen_coords.append((x + 1, y))
                    temp_x = x + 1
                    while temp_x - 1 >= 0 and lines[y][temp_x - 1] in '0123456789':
                        num = str(lines[y][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y))
                        temp_x -= 1

                    temp_x = x + 1
                    while temp_x + 1 <= len(lines[y]) - 1 and lines[y][temp_x + 1] in "0123456789":
                        num += str(lines[y][temp_x + 1])
                        seen_coords.append((temp_x + 1, y))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                # up left
                if y - 1 >= 0 and x - 1 >= 0 and lines[y - 1][x - 1] in '0123456789' and (x - 1, y - 1) not in seen_coords:

                    num = str(lines[y - 1][x - 1])
                    seen_coords.append((x - 1, y - 1))
                    temp_x = x - 1
                    while temp_x - 1 >= 0 and lines[y - 1][temp_x - 1] in '0123456789':
                        num = str(lines[y - 1][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y - 1))
                        temp_x -= 1

                    temp_x = x - 1
                    while temp_x + 1 <= len(lines[y - 1])- 1 and lines[y - 1][temp_x + 1] in "0123456789":
                        num += str(lines[y - 1][temp_x + 1])
                        seen_coords.append((temp_x + 1, y - 1))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                # up right
                if y - 1 >= 0 and x + 1 <= len(lines[y - 1]) - 1 and lines[y - 1][x + 1] in '0123456789' and (x + 1, y - 1) not in seen_coords:

                    num = str(lines[y - 1][x + 1])
                    seen_coords.append((x + 1, y - 1))
                    temp_x = x + 1
                    while temp_x - 1 >= 0 and lines[y - 1][temp_x - 1] in '0123456789':
                        num = str(lines[y - 1][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y - 1))
                        temp_x -= 1

                    temp_x = x + 1
                    while temp_x + 1 <= len(lines[y - 1]) - 1 and lines[y - 1][temp_x + 1] in "0123456789":
                        num += str(lines[y - 1][temp_x + 1])
                        seen_coords.append((temp_x + 1, y - 1))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                # down left
                if y + 1 <= len(lines) - 1 and x - 1 >= 0 and lines[y + 1][x - 1] in '0123456789' and (x - 1, y + 1) not in seen_coords:

                    num = str(lines[y + 1][x - 1])
                    seen_coords.append((x - 1, y + 1))
                    temp_x = x - 1
                    while temp_x - 1 >= 0 and lines[y + 1][temp_x - 1] in '0123456789':
                        num = str(lines[y + 1][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y + 1))
                        temp_x -= 1

                    temp_x = x - 1
                    while temp_x + 1 <= len(lines[y + 1]) - 1 and lines[y + 1][temp_x + 1] in "0123456789":
                        num += str(lines[y + 1][temp_x + 1])
                        seen_coords.append((temp_x + 1, y + 1))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                # down right
                if y + 1 <= len(lines) - 1 and x + 1 <= len(lines[y + 1]) - 1 and lines[y + 1][x + 1] in '0123456789' and (x + 1, y + 1) not in seen_coords:

                    num = str(lines[y + 1][x + 1])
                    seen_coords.append((x + 1, y + 1))
                    temp_x = x + 1
                    while temp_x - 1 >= 0 and lines[y + 1][temp_x - 1] in '0123456789':
                        num = str(lines[y + 1][temp_x - 1]) + num
                        seen_coords.append((temp_x - 1, y + 1))
                        temp_x -= 1

                    temp_x = x + 1
                    while temp_x + 1 <= len(lines[y + 1]) - 1 and lines[y + 1][temp_x + 1] in "0123456789":
                        num += str(lines[y + 1][temp_x + 1])
                        seen_coords.append((temp_x + 1, y + 1))
                        temp_x += 1

                    if is_valid_gear:
                        gear_ratio_nums.append(int(num))
                        if len(gear_ratio_nums) > 2:
                            is_valid_gear = False

                if is_valid_gear and len(gear_ratio_nums) == 2:
                    acc += gear_ratio_nums[0] * gear_ratio_nums[1]

    print(acc)