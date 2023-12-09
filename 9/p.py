import sys
import numpy as np

with open(sys.argv[1], "r") as f:
    inp = [[int(y) for y in np.array(x.strip().split())] for x in f.readlines()]

part1 = []
part2 = []

for l in inp:
    curr = l
    tree = []
    ans = curr[-1] 
    while True:
        n = np.diff(curr)
        tree.append(curr)
        ans += n[-1] 
        if np.all(n == n[0]):
            tree.append(n)
            break
        curr = n
    ans2 = 0
    tree.reverse()
    for i in tree:
        ans2 = i[0] - ans2
    part1.append(ans)
    part2.append(ans2)

print("Part1:",sum(part1))
print("Part2:",sum(part2))
