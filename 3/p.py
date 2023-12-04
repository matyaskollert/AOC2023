import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

part1 = []
part2 = {}

for i in range(len(inp)):
    last_num = "0"
    # For Part 1
    isPart = False
    # For Part 2
    gears = []
    gearAdded = False
    for j in range(len(inp[0])):
        curr_char = inp[i][j]
        if curr_char.isdigit():
            if last_num == "0":
                last_num = curr_char
            else:
                last_num += curr_char
            # Go over all the squares around the current character
            for di in [-1,0,1]:
                newI = i + di
                # if the square is out of bounds then skip
                if newI < 0 or newI >= len(inp):
                    continue
                for dj in [-1,0,1]:
                    newJ = j + dj
                    # if the square is useless/out of bounds then skip
                    if (di == 0 and dj == 0) or (newJ < 0 or newJ >= len(inp[0])):
                        continue
                    adj_char = inp[newI][newJ]
                    if not adj_char.isdigit() and adj_char != ".":
                        # Part 2 - if the adj char is a * then add the position to the gears
                        if adj_char == "*" and not gearAdded:
                            gearAdded = True
                            gears.append(str(newI) + "," + str(newJ))
                        isPart = True
        # if the current character isn't a digit or it is at the end of a line
        if not curr_char.isdigit() or (j + 1) == len(inp[0]):
            if isPart:
                part1.append(int(last_num))
            if last_num != "0":
                # For each gear around the curr number, add the number to the gear list
                for gear in gears:
                    if gear not in part2.keys():
                        part2[gear] = []
                    part2[gear].append(int(last_num))
                    gearAdded = False
                    gears = []
            last_num = "0"
            isPart = False

print("Part 1:", sum(part1))

# Get all the gears that have two adjecent numbers and multiply the numbers
part2_res = 0
for key in part2.keys():
    if len(part2[key]) == 2:
        part2_res += part2[key][0] * part2[key][1]

print("Part 2:", part2_res)

