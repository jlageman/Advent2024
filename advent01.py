dat = open('input1.txt').read().splitlines()

# part 1
left, right = [], []
for line in dat:
    line = line.split('   ')
    left.append(int(line[0]))
    right.append(int(line[1]))
ans1 = 0
for l, r in zip(sorted(left), sorted(right)):
    ans1 += abs(l-r)
    
# part 2
ans2 = 0
for l in left:
    sim = sum([1 if x==l else 0 for x in right])
    ans2 += l*sim
    
