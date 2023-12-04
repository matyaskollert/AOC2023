import sys
import numpy as np
import regex as re

with open(sys.argv[1], "r") as f:
    inp = [np.array(re.findall(r"\d+", x[8:])) for x in f.readlines()]

part1 = 0 
amnt_of_wins = []

for line in inp:
    unique_nums = np.unique(line)
    diff = len(line) - len(unique_nums)
    score = 2**(diff - 1) if diff > 0 else 0
    part1 += int(score)
    amnt_of_wins.append(diff)

print("Part 1:", part1)
    
# Add 1 for each card from the input
list_of_amnts = [1 for x in range(len(inp))]
curr_index = 0

for curr_i in range(len(list_of_amnts)):
    amount = list_of_amnts[curr_i]
    score = amnt_of_wins[curr_i]
    if score == 0:
        continue
    # For each won card from i+1 to i+1+score
    for copy_i in range(curr_i + 1, curr_i + score + 1):
        # Add the amount of curr cards to the amount of won card
        list_of_amnts[copy_i] += amount

print("Part 2:", sum(list_of_amnts))

