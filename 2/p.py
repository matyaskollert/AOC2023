import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

dic = { "red": 12, "green": 13, "blue": 14 }

corr = []
max_colors = []

for i, line in enumerate(inp):
    game = line.split(": ")[1]
    wrong = False
    max_color = { "red": 0, "green": 0, "blue": 0 }
    for r in game.split("; "):
        for draw in r.split(", "):
            d = draw.split(" ")
            if dic[d[1]] < int(d[0]):
                wrong = True
            max_color[d[1]] = max(max_color[d[1]], int(d[0]))
    if wrong == False:
        corr.append(i+1)
    max_colors.append(max_color["red"] * max_color["green"] * max_color["blue"])

print("Part 1:", sum(corr))
print("Part 2:", sum(max_colors))
