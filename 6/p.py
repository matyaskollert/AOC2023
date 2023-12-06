import sys
import regex as re
import numpy as np

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

times = [int(x) for x in re.findall(r"\d+", inp[0])]
dists = [int(x) for x in re.findall(r"\d+", inp[1])]
part1 = 1 

for ind,time in enumerate(times):
    dist = dists[ind]
    r1,r2 = (np.roots([1,-time,dist]))
    part1 *= int(np.ceil(r1) - np.floor(r2)) - 1 


print("Part 1:",part1)

time = int(inp[0].replace("Time:", "").replace(" ", ""))
dist = int(inp[1].replace("Distance:", "").replace(" ", ""))

r1,r2 = np.roots([1, -time, dist])

part2 = int(np.ceil(r1) - np.floor(r2)) - 1 
print("Part 2:",part2)
