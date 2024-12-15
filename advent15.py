dat = open('input15.txt').read().splitlines()
grid = {}
for y, line in enumerate(dat):
    if len(line)<1:
        break
    for x, pos in enumerate(line):
        grid[(x,y)] = pos
instructions = ''
for line in dat[y+1:]:
    instructions = instructions + line
robot = [x for x in grid.keys() if grid[x]=='@']
directions = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0,-1)}

# part 1
def move_item(grid, to_move, direction):
    x,y = to_move[-1]
    dx, dy = direction
    if grid[(x+dx,y+dy)]=='#':
        return grid
    elif grid[(x+dx,y+dy)]=='.':
        for pos in reversed(to_move):
            px,py = pos
            grid[(px+dx,py+dy)] = grid[pos]
            grid[pos]='.'
        return grid
    elif grid[(x+dx,y+dy)]=='O':
        to_move.append((x+dx,y+dy))
        return move_item(grid, to_move, direction)

# loop over instructions
for ins in instructions:
    grid = move_item(grid, robot, directions[ins])
    robot = [x for x in grid.keys() if grid[x]=='@']
ans = 0
for key, val in grid.items():
    if val=='O':
        ans += (100*key[1]+key[0])
        
# part 2
wide_grid = {}
for y, line in enumerate(dat):
    if len(line)<1:
        break
    for x, pos in enumerate(line):
        if pos in '#.':
            wide_grid[(2*x,y)] = pos
            wide_grid[(2*x+1,y)] = pos
        elif pos=='O':
            wide_grid[(2*x,y)] = '['
            wide_grid[(2*x+1,y)] = ']'
        elif pos=='@':
            wide_grid[(2*x,y)] = '@'
            wide_grid[(2*x+1,y)] = '.'
robot = [x for x in wide_grid.keys() if wide_grid[x]=='@']

def move_wide_item(wide_grid, to_move, direction):
    dx, dy = direction
    # if anything hits stone: don't move
    if any([wide_grid[(px+dx,py+dy)]=='#' for px,py in to_move]):
        return wide_grid
    # if there is only open space/known boxes before us: move
    elif all([(wide_grid[(px+dx,py+dy)]=='.' or (px+dx,py+dy) in to_move) for px,py in to_move]):
        for pos in reversed(to_move):
            px,py = pos
            wide_grid[(px+dx,py+dy)] = wide_grid[pos]
            wide_grid[pos]='.'
        return wide_grid
    # check for unknown boxes, add them to move list
    if any([wide_grid[(px+dx,py+dy)]=='[' for px,py in to_move]):
        for px,py in to_move:
            if wide_grid[(px+dx,py+dy)]=='[' and (px+dx,py+dy) not in to_move:
                to_move.append((px+dx,py+dy))
                to_move.append((px+dx+1,py+dy))
    if any([wide_grid[(px+dx,py+dy)]==']' for px,py in to_move]):
        for px,py in to_move:
            if wide_grid[(px+dx,py+dy)]==']' and (px+dx,py+dy) not in to_move:
                to_move.append((px+dx,py+dy))
                to_move.append((px+dx-1,py+dy))
    return move_wide_item(wide_grid, to_move, direction)

# loop over instructions
for ins in instructions:
    wide_grid = move_wide_item(wide_grid, robot, directions[ins])
    robot = [x for x in wide_grid.keys() if wide_grid[x]=='@']
ans2 = 0
for key, val in wide_grid.items():
    if val=='[':
        ans2 += (100*key[1]+key[0])