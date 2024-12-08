dat = open('input8.txt').read().splitlines()
xrange = range(len(dat[0]))
yrange = range(len(dat))

# part 1
antinodes = []
ants = {}
for y, line in enumerate(dat):
    for x, ch in enumerate(line):
        if ch=='.':
            continue
        if ch not in ants.keys():
            ants[ch] = []
        ants[ch].append((x,y))
for locs in ants.values():
    if len(locs)<2:
        continue
    pairs = [(a, b) for i, a in enumerate(locs) for b in locs[i+1:]]
    for pair in pairs:
        ax, ay = pair[0]
        bx, by = pair[1]
        dx, dy = bx-ax, by-ay
        if ax-dx in xrange and ay-dy in yrange:
            antinodes.append((ax-dx, ay-dy))
        if bx+dx in xrange and by+dy in yrange:
            antinodes.append((bx+dx, by+dy))
ans = len(set(antinodes))

# part 2
antinodes2 = []
for locs in ants.values():
    if len(locs)<2:
        continue
    pairs = [(a, b) for i, a in enumerate(locs) for b in locs[i+1:]]
    for pair in pairs:
        ax, ay = pair[0]
        bx, by = pair[1]
        dx, dy = bx-ax, by-ay
        x,y = ax+0, ay+0
        antinodes2.append((ax,ay))
        while True:
            if x-dx in xrange and y-dy in yrange:
                antinodes2.append((x-dx, y-dy))
                x,y = (x-dx, y-dy)
            else:
                break
        x,y = ax+0, ay+0
        while True:
            if x+dx in xrange and y+dy in yrange:
                antinodes2.append((x+dx, y+dy))
                x,y = (x+dx, y+dy)
            else:
                break
ans2 = len(set(antinodes2))