import sys
import numpy as np 

with open(sys.argv[1], "r") as f:
    inp = [list(x.strip()) for x in f.readlines()]

S = (0,0)
for i, l in enumerate(inp):
    if "S" in l:
        S = (i, l.index("S"))

starts = []
for dy in [1,0,-1]:
    for dx in [1,0,-1]:
        if dy == 0 and dx == 0:
            continue
        if len(inp)<S[0]+dy<0 or len(inp[0])<S[1]+dx<0:
            continue
        starts.append((S[0] + dy, S[1] + dx))

print("Starts",starts)

def mapp(x):
    l = inp[x[0]][x[1]] 
    #print(l)
    n = []
    if l == "-":
        n = [(x[0],x[1]-1),(x[0],x[1]+1)]
    elif l == "|":
        n = [(x[0]+1,x[1]),(x[0]-1,x[1])]
    elif l == "F":
        n = [(x[0]+1,x[1]),(x[0],x[1]+1)]
    elif l == "7":
        n = [(x[0]+1,x[1]),(x[0],x[1]-1)]
    elif l == "L":
        n = [(x[0]-1,x[1]),(x[0],x[1]+1)]
    elif l == "J":
        n = [(x[0]-1,x[1]),(x[0],x[1]-1)]
    else:
        return [-1,-1]

    for nn in n:
        if len(inp)<nn[0]<0 or len(inp[0])<nn[1]<0:
            return [-1,-1]
    else:
        return n

visited = []
for s in starts:
    prev = S
    curr = s
    nextt = (-1,-1) 
    visited = []
    #print("*" * 20)
    while curr != S:
        #print(prev,curr,nextt)
        i1, i2 = mapp(curr)
        #print(i1,i2)
        if i1 == -1:
            break
        if prev == i1:
            nextt = i2
        elif prev == i2:
            nextt = i1
        else:
            #print("end", prev)
            break
        visited.append(curr)
        prev = curr
        curr = nextt
    if curr == S:
        break

#print("Visited indices",visited)
#print("Visited letters",[inp[x[0]][x[1]] for x in visited])

mid = np.round(len(visited) / 2)

print("Part 1", int(mid))

with open("test", "w") as f:
    text = "" 
    for i in range(len(inp)):
        line = ""
        for j in range(len(inp[0])):
            if (i,j) in visited or inp[i][j] == ".":
                line += inp[i][j]
            else:
                line += " "
                
        text += line + "\n"
    f.write(text)
