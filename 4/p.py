import sys
import numpy as np
import regex as re

with open(sys.argv[1], "r") as f:
    inp = [np.array(re.findall(r"\d+", x[8:])) for x in f.readlines()]

part1 = 0 

# Add 1 for each card from the input
list_of_amnts = [1 for x in range(len(inp))]

for curr_i, line in enumerate(inp):
    unique_nums = np.unique(line)
    diff = len(line) - len(unique_nums)
    score = 2**(diff - 1) if diff > 0 else 0
    part1 += int(score)
    # Part 2
    amnt_of_curr_card = list_of_amnts[curr_i] 
    if score == 0:
        continue
    # For each won card from i+1 to i+1 + amount of winning nums
    for copy_i in range(curr_i + 1, curr_i + 1 + diff):
        # Add the amount of curr cards to the amount of won card
        list_of_amnts[copy_i] += amnt_of_curr_card 



print("Part 1:", part1)
print("Part 2:", sum(list_of_amnts))

