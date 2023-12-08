import sys
import regex as re
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    imp = [x.strip() for x in f.readlines()]

ins = imp[0]

d = defaultdict()
for i in range(2,len(imp)):
    curr = imp[i][:3]
    left = imp[i][7:10]
    right = imp[i][12:15]
    d[curr] = (left, right)

i = 0
curr_spot = "AAA"
steps = 0

while True:
    steps += 1
    curr = 0 if ins[i] == "L" else 1
    next_spot = d[curr_spot][curr] 
    i = (i + 1) % len(ins)
    curr_spot = next_spot
    if next_spot == "ZZZ":
        break

print("Part 1:", steps)

poss = [x[:3] for x in imp[2:]]

curr_spots = []
for p in poss:
    if p[2] == "A":
        curr_spots.append(p)
i = 0
steps = 0
lenn = len(curr_spots)
count = 0
steps_2 = [[0] for x in range(lenn)]

while True:
    steps += 1
    curr = 0 if ins[i] == "L" else 1
    i = (i + 1) % len(ins)
    for k,curr_spot in enumerate(curr_spots):
        next_spot = d[curr_spot][curr] 
        curr_spots[k] = next_spot
        if next_spot[2] == "Z":
            steps_2[k].append(steps)
            if len(steps_2[k]) != 2:
                steps_2[k][-1] = steps_2[k][-1] % steps_2[k][1]
            count += 1
            
    done = True 
    for k in steps_2:
        if len(k) < 2:
            done = False
    if done:
        break
    count = 0

# https://www.calculatorsoup.com/calculators/math/lcm.php gets you the answer
print("Part 2:", [x[1] for x in steps_2])
