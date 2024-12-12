dat = open('input6.txt').read().splitlines()
for y, line in enumerate(dat):
    for x, s in enumerate(line):
        if s=='^':
            pos = (x,y)
            direction = (0,-1)
next_direction = {(0,-1): (1,0), (1,0): (0,1), (0,1): (-1,0), (-1,0): (0,-1)}
            
# part 1
def step(dat, pos, direction):
    x,y = pos
    dx,dy = direction
    if x+dx<0 or x+dx>len(dat[0])-1 or y+dy<0 or y+dy>len(dat)-1:
        return 0,0
    if dat[y+dy][x+dx]=='#':
        return pos, next_direction[direction]
    elif dat[y+dy][x+dx] in '.^':
        pos = (x+dx, y+dy) 
        return pos, direction

visited = []
prev_directions = []
while True:
    visited.append(pos)
    prev_directions.append(direction)
    pos, direction = step(dat, pos, direction)  
    if pos==0:
        break
ans = len(set(visited))

# part 2
obstacles = []
for i, pos in enumerate(visited):
    if pos in visited[:i]:
        if next_direction[prev_directions[i]]==prev_directions[visited.index(pos)]:
            x,y = pos
            dx,dy = prev_directions[i]
            obstacles.append((x+dx, y+dy))
    else:
        new_dir = next_direction[prev_directions[i]]
        new_pos = pos
        while True:
            new_pos, new_dir = step(dat, new_pos, new_dir)
            if new_pos==pos and new_dir==direction:
                x,y = pos
                dx,dy = direction
                obstacles.append((x+dx, y+dy))
                break
            elif new_pos==0:
                break
ans2 = 0
for obs in set(obstacles):
    x,y = obs
    if dat[y][x] not in '^#':
        ans2 += 1
