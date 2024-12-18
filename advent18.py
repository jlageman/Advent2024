byte_list = []
for line in open('input18.txt').read().splitlines():
    byte_list.append((int(line.split(',')[0]), int(line.split(',')[1])))
grid_size = (70,70)
N_fallen_bytes = 1024
fallen_bytes = byte_list[:N_fallen_bytes]

def get_steps(grid_size, current, fallen_bytes):
    steps = []
    x, y = current
    if x-1 >= 0 and (x-1,y) not in fallen_bytes:
        steps.append((x-1,y))
    if x+1 <= grid_size[0] and (x+1,y) not in fallen_bytes:
        steps.append((x+1,y))
    if y-1 >= 0 and (x,y-1) not in fallen_bytes:
        steps.append((x,y-1))
    if y+1 <= grid_size[1] and (x,y+1) not in fallen_bytes:
        steps.append((x,y+1))
    return steps

def find_shortest_path(grid_size, fallen_bytes):
    start = (0,0)
    finish = grid_size
    dist = {}
    d = {}
    for x in range(grid_size[0]+1):
        for y in range(grid_size[1]+1):
            dist[(x, y)] = 999999
    visited = []
    dist[start] = 0
    current = start
    while current != finish:
        steps = get_steps(grid_size, current, fallen_bytes)
        if len(steps)<1:
            return fallen_bytes[-1], False
        for s in steps:
            if s in visited:
                continue
            if 1 + dist[current] < dist[s]:
                dist[s] = 1 + dist[current]
        visited.append(current)
        d[current] = dist[current]
        del dist[current]
        current = min(dist, key = dist.get)
    ans = dist[finish]
    return ans, True

# part 1
ans, _ = find_shortest_path(grid_size, fallen_bytes)

# part 2
def binary_search(grid_size, N_fallen_bytes, byte_list):
    split_index = len(byte_list[N_fallen_bytes:]) // 2
    if split_index == 0:
        return byte_list[-1]
    fallen_bytes = byte_list[:N_fallen_bytes+split_index]
    last_byte, found_path = find_shortest_path(grid_size, fallen_bytes)
    if found_path:
        return binary_search(grid_size, N_fallen_bytes+split_index, byte_list)
    else:
        return binary_search(grid_size, N_fallen_bytes, byte_list[:N_fallen_bytes+split_index])

ans2 = binary_search(grid_size, N_fallen_bytes, byte_list)