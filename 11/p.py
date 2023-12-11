import sys
import numpy as np

with open(sys.argv[1], "r") as f:
    inp = np.array([list(x.strip()) for x in f.readlines()])

x_space = []
y_space = []
galaxies = []

for i,l in enumerate(inp):
    if "#" not in l:
        y_space.append(i)
    else:
        for j,ll in enumerate(l):
            if ll == "#":
                galaxies.append((i,j))

for i,l in enumerate(np.transpose(inp)):
    if "#" not in l:
        x_space.append(i)


def dist(a,b):
    addX1 = 0
    addX2 = 0
    addY1 = 0
    addY2 = 0
    dx = np.abs(a[1] - b[1])
    dy = np.abs(a[0] - b[0])
    min_x = min(a[1],b[1])
    max_x = max(a[1],b[1])
    min_y = min(a[0],b[0])
    max_y = max(a[0],b[0])
    for s in x_space:
        if min_x < s < max_x:
            addX1 += 1
            addX2 += 1000000 - 1 

    for s in y_space:
        if min_y < s < max_y:
            addY1 += 1
            addY2 += 1000000 -1 
    
    return [dy+addY1+dx+addX1, dy+addY2+dx+addX2]
    

part1 = []
part2 = [] 

for i in range(len(galaxies)):
    g1 = galaxies[i]
    for j in range(i+1,len(galaxies)):
        g2 = galaxies[j]
        d1, d2 = dist(g1,g2)
        part1.append(d1)
        part2.append(d2)
        

part2_b = np.array(part2, dtype='int64')
print("Part 1", sum(part1))
print("Part 2", sum(part2_b))
