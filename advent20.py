dat = open('input20.txt').read().splitlines()
grid = {}
for y, line in enumerate(dat):
    for x, pos in enumerate(line):
        grid[(x,y)] = pos
        if pos=='S':
            start = (x,y)
        elif pos=='E':
            finish = (x,y)

# part 1
route = []
current = start
while current != finish:
    route.append(current)
    x, y = current
    if x-1 >= 0 and grid[(x-1,y)]!='#' and (x-1,y) not in route:
        current = (x-1,y)
        continue
    if x+1 <= max(grid.keys())[0] and grid[(x+1,y)]!='#' and (x+1,y) not in route:
        current = (x+1,y)
        continue
    if y-1 >= 0 and grid[(x,y-1)]!='#' and (x,y-1) not in route:
        current = (x,y-1)
        continue
    if y+1 <= max(grid.keys())[1] and grid[(x,y+1)]!='#' and (x,y+1) not in route:
        current = (x,y+1)
route.append(finish)

cheats = []
for i, step in enumerate(route[:-102]):
    x, y = step
    if (x+1,y) not in route and (x+2,y) in route[i+102:]:
        cheats.append((step, x+2, y))
    if (x,y+1) not in route and (x,y+2) in route[i+102:]:
        cheats.append((step, x, y+2))
    if (x-1,y) not in route and (x-2,y) in route[i+102:]:
        cheats.append((step, x-2, y))
    if (x,y-1) not in route and (x,y-2) in route[i+102:]:
        cheats.append((step, x, y-2))
ans = len(cheats)

# part 2
time_saved = 100
cheats2 = []
for i, step in enumerate(route[:-(time_saved+2)]):
    x, y = step
    for cheat_time in range(3, 21):
        for c in range(cheat_time+1):
            if i+time_saved+cheat_time >= len(route):
                break
            if (x+c, y+(cheat_time-c)) in route[i+time_saved+cheat_time:]:
                cheats2.append((step, (x+c, y+(cheat_time-c))))
            if (x+c, y-(cheat_time-c)) in route[i+time_saved+cheat_time:]:
                cheats2.append((step, (x+c, y-(cheat_time-c))))
            if (x-c, y+(cheat_time-c)) in route[i+time_saved+cheat_time:]:
                cheats2.append((step, (x-c, y+(cheat_time-c))))
            if (x-c, y-(cheat_time-c)) in route[i+time_saved+cheat_time:]:
                cheats2.append((step, (x-c, y-(cheat_time-c))))
ans2 = len(cheats) + len(set(cheats2))