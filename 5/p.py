import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

# Parse the input into seeds
seeds = [int(x) for x in inp[0].replace("seeds: ", "").split(" ")]

maps = []

# Parse the input string into maps
for i in range(2,len(inp)):
    if "map" in inp[i]:
        mapp = []
        for j in range(i+1,len(inp)):
            if inp[j] == "":
                maps.append(mapp)
                i = j
                break
            mapp.append([int(x) for x in inp[j].split(" ")])
        if j+1 == len(inp):
            maps.append(mapp)


part1 = []

for seed in seeds:
    num = seed
    for mapp in maps:
        for interval in mapp:
            if interval[1]<=num<=(interval[1]+interval[2]):
                num = num - interval[1] + interval[0]
                break
    part1.append(num)

print("Part 1:", min(part1))

# Add the default seed ranges to the ranges list
ranges = []
for i in range(0,len(seeds),2):
    ranges.append([seeds[i],seeds[i] + seeds[i+1] - 1])

for mapp in maps:
    # Used to store the newly created ranges for the next map
    next_ranges = []
    for interval in mapp:
        # Used to store the ranges that were converted
        # Can't remove immediately because of the iterator
        remove_ranges = []
        for r in ranges:
            interval_s = [interval[1], interval[1]+interval[2]-1]
            interval_d = [interval[0], interval[0]+interval[2]-1]
            # outside the interval - ignore
            if r[1] < interval_s[0] or r[0] > interval_s[1]: 
                continue

            # The new min value of the range in the destination
            _min = r[0] - interval_s[0] + interval_d[0]
            # The new max value of the range in the destination
            _max = interval_d[1] - interval_s[1] + r[1] 
            remove_ranges.append(r)

            # fully in interval - convert the whole thing
            if r[0] >= interval_s[0] and r[1] <= interval_s[1]:
                next_ranges.append([_min,_max])

            # both sides are over the interval - convert into 3
            elif r[0] < interval_s[0] and r[1] > interval_s[1]:
                _min = interval_d[0]
                _max = interval_d[1]
                next_ranges.append(interval_d)
                ranges.append([r[0], interval_s[0] - 1])
                ranges.append([interval_s[1] + 1, r[1]])

            # left side is over - convert into 2
            elif r[0] < interval_s[0] and r[1] <= interval_s[1]:
                next_ranges.append([interval_d[0], _max])
                ranges.append([r[0], interval_s[0] - 1])

            # right side is over - convert into 2
            elif r[0] >= interval_s[0] and r[1] > interval_s[1]:
                next_ranges.append([_min, interval_d[1]])
                ranges.append([interval_s[1] + 1, r[1]])

        for r in remove_ranges:
            ranges.remove(r)
            
    for i in range(len(ranges)):
        next_ranges.append(ranges[i])
    ranges = next_ranges 

mins = [x[0] for x in ranges]
print("Part 2:", min(mins))
