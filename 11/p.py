import sys
import numpy as np

with open(sys.argv[1], "r") as f:
    inp = [list(x.strip()) for x in f.readlines()]

x_empty = []
y_empty = []
galaxies = []

for i,l in enumerate(inp):
    if "#" not in l:
        y_empty.append(i)
    else:
        for j,ll in enumerate(l):
            if ll == "#":
                galaxies.append((i,j))

for i,l in enumerate(np.transpose(inp)):
    if "#" not in l:
        x_empty.append(i)


def dist(a,b):
    addX1 = 0
    addX2 = 0
    addY1 = 0
    addY2 = 0
    dx = np.abs(a[1] - b[1])
    dy = np.abs(a[0] - b[0])
    for col in x_empty:
        if min(a[1],b[1]) < col < max(a[1],b[1]):
            addX1 += 1
            addX2 += 10**6 - 1 

    for row in y_empty:
        if min(a[0],b[0]) < row < max(a[0],b[0]):
            addY1 += 1
            addY2 += 10**6 -1 
    
    p1 = dy + addY1 + dx + addX1
    p2 = dy + addY2 + dx + addX2
    return p1, p2

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
