import sys

with open(sys.argv[1], "r") as f:
    inp = [x.strip() for x in f.readlines()]

nums = []

for line in inp:
    digits = [] 
    for l in line:
        if l.isdigit():
            digits.append(l)
    nums.append(int(digits[0] + digits[-1]))

print("Part 1: " , sum(nums))

nums2 = []

for line in inp:
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        for k, val in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
            if line[i:].startswith(val):
                digits.append(str(k+1))
    nums2.append(int(digits[0] + digits[-1]))

print("Part 2: " , sum(nums2))
