dat = open('input12.txt').read().splitlines()
m = {}
to_visit = []
for y, line in enumerate(dat):
    for x, crop in enumerate(line):
        m[(x,y)] = crop
        to_visit.append((x,y))

# part 1 + 2
def fence_crop(m, position, this_area):
    perimeter = 0
    sides = 0
    crop = m[position]
    this_area.append(position)
    x, y = position
    corners = [0,0,0,0]
    # check all neighbors if not already in this area
    # left
    if x-1<0 or m[(x-1, y)]!= crop:
        perimeter += 1
        corners[0]=1
    elif m[(x-1,y)]==crop:
        if not (x-1, y) in this_area:
            p, this_area, s = fence_crop(m, (x-1, y), this_area)
            perimeter += p
            sides += s
    # up
    if y-1<0 or m[(x,y-1)]!= crop:
        perimeter += 1
        corners[1]=1
    elif m[(x,y-1)]==crop:
        if not (x,y-1) in this_area:
            p, this_area, s = fence_crop(m, (x, y-1), this_area)
            perimeter += p
            sides += s
    # right
    if x+1>max(m.keys())[0] or m[(x+1, y)]!= crop:
        perimeter += 1
        corners[2]=1
    elif m[(x+1,y)]==crop:
        if not (x+1,y) in this_area:
            p, this_area, s = fence_crop(m, (x+1, y), this_area)
            perimeter += p
            sides += s
    # down
    if y+1>max(m.keys())[1] or m[(x, y+1)]!= crop:
        perimeter += 1
        corners[3]=1
    elif m[(x,y+1)]==crop:
        if not (x,y+1) in this_area:
            p, this_area, s = fence_crop(m, (x,y+1), this_area)
            perimeter += p
            sides += s
    
    # count corners
    if sum(corners)==4:
        sides += 4
    elif sum(corners)==3:
        sides += 2
    elif sum(corners)==2:
        if corners[0]!=corners[2]:
            if corners[1]!=corners[3]:
                sides += 1
    # check diagonals
    if not sum(corners)==4:
        for diag in [(x-1,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1)]:
            if diag in m.keys():
                if m[diag[0],y]==crop:
                    if m[x,diag[1]]==crop:
                        if m[diag]!=crop:
                            sides += 1
    
    return perimeter, this_area, sides

ans = 0
ans2 = 0
while to_visit:
    position = to_visit.pop(0)
    perimeter, this_area, sides = fence_crop(m, position, [])
    ans += (perimeter*len(this_area))
    ans2 += (sides*len(this_area))
    to_visit = [x for x in to_visit if not x in this_area]