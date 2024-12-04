dat = open('input4.txt').read().splitlines()

# part 1
ans = 0
def find_xmas(targets, direction, x, y, dat):
    nx,ny = direction
    if x+nx<0 or x+nx==len(dat[y]) or y+ny<0 or y+ny==len(dat):
        return 0
    target = targets.pop(0)
    if dat[y+ny][x+nx]==target:
        if target=='S':
            return 1
        else:
            return find_xmas(targets, direction, x+nx, y+ny, dat)
    else:
        return 0

neighbors = [(1,1), (0,1), (1,0), (-1,-1), (0,-1), (-1,0), (-1,1), (1,-1)]
for y,line in enumerate(dat):
    for x, letter in enumerate(line):
        if letter=='X':
            for direction in neighbors:
                targets = ['M', 'A', 'S']
                ans += find_xmas(targets, direction, x, y, dat)

# part 2
ans2 = 0
diags = [(-1,-1,1,1), (1,-1,-1,1)]
for y,line in enumerate(dat):
    for x, letter in enumerate(line):
        if letter=='A':
            good = False
            for diag in diags:
                nx1,ny1,nx2,ny2 = diag
                if x+nx1<0 or x+nx1==len(dat[y]) or y+ny1<0 or y+ny1==len(dat) or x+nx2<0 or x+nx2==len(dat[y]) or y+ny2<0 or y+ny2==len(dat):
                    good = False
                    break
                elif (dat[y+ny1][x+nx1]=='M' and dat[y+ny2][x+nx2]=='S') or (dat[y+ny1][x+nx1]=='S' and dat[y+ny2][x+nx2]=='M'):
                    good = True
                else:
                    good = False
                    break
            if good:
                ans2 += 1
    