dat = open('input14.txt').read().splitlines()
width, height = 101, 103

# part 1
robots = []
velocities = []
q1,q2,q3,q4 = 0,0,0,0
for line in dat:
    rx, ry = [int(x) for x in line.split()[0].split('=')[1].split(',')]
    dx, dy = [int(x) for x in line.split()[1].split('=')[1].split(',')]
    velocities.append((dx,dy))
    for _ in range(100):
        # new x
        if (rx+dx)<0:
            rx = width + (rx+dx)
        elif (rx+dx)>=width:
            rx = (rx+dx) - width
        else:
            rx = rx+dx
        # new y
        if (ry+dy)<0:
            ry = height + (ry+dy)
        elif (ry+dy)>= height:
            ry = (ry+dy) - height
        else:
            ry = ry+dy
    # where is the robot?
    robots.append((rx,ry))
    if rx < (width//2):
        if ry < (height // 2):
            q1 += 1
        elif ry > (height // 2):
            q3 += 1
    elif rx > (width//2):
        if ry < (height // 2):
            q2 += 1
        elif ry > (height // 2):
            q4 += 1

ans = q1*q2*q3*q4

# part 2
iteration_number = 100
while True:
    iteration_number += 1
    grid = robots
    robots = []
    for robot, velocity in zip(grid, velocities):
        rx, ry = robot
        dx, dy = velocity
        # new x
        if (rx+dx)<0:
            rx = width + (rx+dx)
        elif (rx+dx)>=width:
            rx = (rx+dx) - width
        else:
            rx = rx+dx
        # new y
        if (ry+dy)<0:
            ry = height + (ry+dy)
        elif (ry+dy)>= height:
            ry = (ry+dy) - height
        else:
            ry = ry+dy
        robots.append((rx,ry))
    if len(set(robots))==len(robots):
        ans2 = iteration_number
        break

# print christmas tree
for y in range(height):
    for x in range(width):
        if (x,y) in robots:
            print('#', end="")
        else:
            print('.', end="")
    print('\n')