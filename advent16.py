dat = open('input16.txt').read().splitlines()
grid = {}
for y, line in enumerate(dat):
    for x, pos in enumerate(line):
        grid[(x,y)] = pos
        if pos=='S':
            start = (x,y,1,0)
        elif pos=='E':
            finish = [(x,y,1,0), (x,y,0,1), (x,y,-1,0), (x,y,0,-1)]

# part 1
def get_steps(grid, current):
    x, y, dx, dy = current
    steps, points = [],[]
    if 0 <= (x+dx) <= max(grid.keys())[0]:
        if 0 <= (y+dy) <= max(grid.keys())[1]:
            if grid[(x+dx,y+dy)] != '#':
                steps.append((x+dx, y+dy, dx, dy))
                points.append(1)
    if dx == 0:
        steps.extend([(x,y,1,0), (x,y,-1,0)])
        if not (x,y,dx,dy) in finish:
            points.extend([1000,1000])
        else:
            points.extend([0,0])
    elif dy == 0:
        steps.extend([(x,y,0,1), (x,y,0,-1)])
        if not (x,y,dx,dy) in finish:
            points.extend([1000,1000])
        else:
            points.extend([0,0])
    return steps, points

def find_shortest_path(grid, start, finish):
    dist = {}
    d = {}
    for x in range(max(grid.keys())[0]):
        for y in range(max(grid.keys())[1]):
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                dist[(x, y, dx, dy)] = 999999
    visited = []
    dist[start] = 0
    current = start
    while current not in finish:
        steps, points = get_steps(grid, current)
        for s, p in zip(steps, points):
            if s in visited:
                continue
            if p + dist[current] < dist[s]:
                dist[s] = p + dist[current]
        visited.append(current)
        if not current in finish:
            d[current] = dist[current]
            del dist[current]
        current = min(dist, key = dist.get)
    ans = min([dist[f] for f in finish])
    return ans, d

ans, d = find_shortest_path(grid, start, finish)

# part 2
_, fd = find_shortest_path(grid, finish[0], [start])
good_seats = []
for tile, dist in d.items():
    x, y, dx, dy = tile
    if (x, y, dx*-1, dy*-1) not in fd.keys():
        continue
    if dist + fd[(x, y, dx*-1, dy*-1)]==ans:
        good_seats.append((x,y))
ans2 = len(set(good_seats))+1