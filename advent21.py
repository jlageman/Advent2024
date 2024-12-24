import functools
dat = open('input21.txt').read().splitlines()
numeric_keypad = {'7': (0,0), '8': (1,0), '9': (2,0), '4': (0,1), '5': (1,1), '6': (2,1), '1': (0,2), '2': (1,2), '3': (2,2), '0': (1,3), 'A': (2,3), 'empty': (0,3)}
robot_keypad = {'^': (1,0), 'A': (2,0), '<': (0,1), 'v': (1,1), '>': (2,1), 'empty': (0,0)}
keypads = [numeric_keypad, robot_keypad]

@functools.lru_cache(maxsize=None)
def type_code(code, keypad):
    output = ''
    keypad = keypads[keypad]
    x, y = keypad['A']
    for c in code:
        tx, ty  = keypad[c]
        # if move left: move horizontal then vertical (if possible)
        if x > tx:
            if not (x+(tx-x),y) == keypad['empty']:
                while x != tx:
                    x -= 1
                    output += '<'   
        while y != ty:
            if y < ty:
                y += 1
                output += 'v'
            elif y > ty:
                y -= 1
                output += '^'
        # if move right: move vertical then horizontal (if possible)
        if x < tx:
            while x != tx:
                x += 1
                output += '>'
        elif x > tx:
            while x != tx:
                if (x-1, y) != keypad['empty']:
                    x -= 1
                    output += '<'
        output += 'A'      
    return output

@functools.lru_cache(maxsize=None)
def multiple_robots(code, N_robots):
    new_code = type_code(code, 1)
    # if final robot
    if N_robots==1:
        return len(new_code)
    # if not final robot
    output = 0
    while new_code:
        cur_code, new_code = new_code[:new_code.index('A')+1], new_code[new_code.index('A')+1:]
        output += multiple_robots(cur_code, N_robots-1)
    return output

# part 1
ans = 0
for code in dat:
    new_code = type_code(code, 0)
    for _ in range(2):
        new_code = type_code(new_code, 1)
    ans += (int(code[:3])*len(new_code))
    
# part 2
ans2 = 0
for code in dat:
    lencode = 0
    new_code = type_code(code, 0)
    while new_code:
        cur_code, new_code = new_code[:new_code.index('A')+1], new_code[new_code.index('A')+1:]
        lencode += multiple_robots(cur_code, 25)
    ans2 += (int(code[:3])*lencode)