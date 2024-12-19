dat = open('input19.txt').read().splitlines()
towels = [t for t in dat[0].split(', ')]
designs = [d for d in dat[2:]]

# part 1
def match_pattern(design, towels):
    for t in towels:
        if design.find(t)==0:
            if len(design[len(t):]) < 1:
                return 1
            else:
                found = match_pattern(design[len(t):], towels)
                if found:
                    return 1
    return 0

possible_designs = []
for design in designs:
    if match_pattern(design, towels):
        possible_designs.append(design)
ans = len(possible_designs)

# part 2
def count_match_pattern(design, towels, cache):
    if design in cache.keys():
        return cache[design], cache
    count = 0
    for t in towels:
        if design.find(t)==0:
            if len(design[len(t):]) < 1:
                count += 1
            else:
                c, cache = count_match_pattern(design[len(t):], towels, cache)
                count += c
    cache[design] = count         
    return count, cache

ans2 = 0
cache = {}
for design in possible_designs:
    count, cache = count_match_pattern(design, towels, cache)
    ans2 += count