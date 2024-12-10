# prepare data
dat = open('input10.txt').read().splitlines()
m = {}
trailheads = []
summits = []
for y, line in enumerate(dat):
    for x, height in enumerate(line):
        m[(x,y)] = int(height)
        if height=='0':
            trailheads.append((x,y))
        elif height=='9':
            summits.append((x,y))

# part 1
def get_steps(m, pos, visited):
    steps = []
    height = m[pos]
    x, y = pos
    # left
    if x-1 >= 0:
        if m[(x-1,y)]==height+1 and (x-1, y) not in visited:
            steps.append((x-1,y))
    # right
    if x+1 <= max(m.keys())[0]:
        if m[(x+1,y)]==height+1 and (x+1, y) not in visited:
            steps.append((x+1,y))
    # up
    if y-1 >= 0:
        if m[(x,y-1)]==height+1 and (x, y-1) not in visited:
            steps.append((x,y-1))
    # down
    if y+1 <= max(m.keys())[1]:
        if m[(x,y+1)]==height+1 and (x, y+1) not in visited:
            steps.append((x,y+1))
    return steps

N_reachable_summits = []
reachable_summits = {}
for th in trailheads:
    visited = []
    to_visit = [th]
    while to_visit:
        pos = to_visit.pop(0)
        visited.append(pos)
        to_visit.extend(get_steps(m, pos, visited))
    N_reachable_summits.append(len(set(visited).intersection(summits)))
    reachable_summits[th] = list(set(visited).intersection(summits))
ans = sum(N_reachable_summits)

# part 2
def count_trails(m, pos, summit):
    visited = []
    # if you reached the summit
    if pos==summit:
        return 1
    steps = get_steps(m, pos, visited)
    # if dead end
    if len(steps)<1:
        return 0
    # else: count trails from next step
    total = 0
    for step in steps:
        visited.append(step)
        total += count_trails(m, step, summit)
    return total
            
scores = []    
for th in trailheads:
    th_score = 0
    for s in reachable_summits[th]:
        th_score += count_trails(m, th, s)
    scores.append(th_score)
ans2 = sum(scores)