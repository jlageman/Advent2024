dat = open('input11.txt').read().splitlines()[0].split()
import functools

# define functions
@functools.lru_cache(maxsize=None)
def single_blink_count(stone):
    if stone=='0':
        return '1', None
    elif len(stone)%2==0:
        s1 = stone[:len(stone)//2]
        s2 = stone[len(stone)//2:]
        while len(s2)>1 and s2[0]=='0':
            s2 = s2[1:]
        return s1, s2
    else:
        return str(2024*int(stone)), None

@functools.lru_cache(maxsize=None)
def multiple_blink_count(stone, blinks):
    s1, s2 = single_blink_count(stone)
    # if final blink
    if blinks==1:
        if s2==None:
            return 1
        else:
            return 2
    # if not final blink
    count = multiple_blink_count(s1, blinks-1)
    if not s2==None:
        count += multiple_blink_count(s2, blinks-1)
    return count

# part 1
stones = [x for x in dat]
ans = 0
for stone in stones:
    ans += multiple_blink_count(stone, 25)

# part 2
stones = [x for x in dat]
ans2 = 0
for stone in stones:
    ans2 += multiple_blink_count(stone, 75)