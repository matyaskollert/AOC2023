import sys
import regex as re

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]



def eval_inner(card, ind):
    unique = "".join(set(card))
    if len(unique) == 1:
        return min(0,ind)
    # Full house of 4
    if len(unique) == 2:
        # 4
        if card.count(unique[0]) == 4 or card.count(unique[0]) == 1:
            return min(1,ind) 
        # Full house
        else:
            return min(2,ind) 
    # 2 Pairs of 3
    if len(unique) == 3:
        # 3
        if card.count(unique[1]) == 3 or card.count(unique[0]) == 3 or card.count(unique[2]) == 3:
            return min(3,ind) 
        # 2 Pairs
        else:
            return min(4,ind) 
    # 1 Pair or High Card
    return min(len(unique) + 1, ind)

str8 = [str(x) for x in range(2,10)] + ["T","Q","K","A"]

def eval(card_o, bid, p2):
    ind = 10 

    if "J" not in card_o or not p2:
        ind = eval_inner(card_o,ind)
    else:
        for s in str8:
            card = card_o.replace("J",s)
            ind = eval_inner(card,ind)

    groups[ind].append([card_o, bid])

#### PART 1

groups = [[],[],[],[],[],[],[]]
part1 = []

for i in inp:
    card, bid = i.split(" ")
    eval(card, bid, False)

def sortFunc(x):
    y = x[0].replace("A","Z").replace("K", "Y").replace("T", "B")
    return y

c = len(inp)
for g in groups:
    g.sort(key=sortFunc,reverse=True)
    for hand in g:
        part1.append(int(hand[1]) * c)
        c -= 1 

print("Part 1:", sum(part1))

#### PART 2

groups = [[],[],[],[],[],[],[]]
part2 = []

for i in inp:
    card, bid = i.split(" ")
    eval(card, bid, True)

def sortFunc2(x):
    y = x[0].replace("A","Z").replace("K", "Y").replace("T", "B").replace("J", "1")
    return y

c = len(inp)
for g in groups:
    g.sort(key=sortFunc2,reverse=True)
    for gg in g:
        part2.append(int(gg[1]) * c)
        c -= 1 

print("Part 2:", sum(part2))
