dat = open('input7.txt').read().splitlines()
testvals = [int(line.split(': ')[0]) for line in dat]
nums = [[int(x) for x in line.split(': ')[1].split()] for line in dat]

# part 1
def possible_solutions(left_nums, right_nums):
    if len(left_nums)<1:
        left_nums = [right_nums.pop(0)]
    next_num = right_nums.pop(0)
    new_left_nums = []
    for n in left_nums:
        new_left_nums.append(n+next_num)
        new_left_nums.append(n*next_num)
    if len(right_nums)>0:
        return possible_solutions(new_left_nums, right_nums)
    return new_left_nums

ans = 0
for testval, num in zip(testvals, nums):
    right_nums = [x for x in num]
    pos = possible_solutions([], right_nums)
    if testval in pos:
        ans += testval

# part 2
def possible_solutions2(left_nums, right_nums):
    if len(left_nums)<1:
        left_nums = [right_nums.pop(0)]
    next_num = right_nums.pop(0)
    new_left_nums = []
    for n in left_nums:
        new_left_nums.append(n+next_num)
        new_left_nums.append(n*next_num)
        new_left_nums.append(int(str(n)+str(next_num)))
    if len(right_nums)>0:
        return possible_solutions2(new_left_nums, right_nums)
    return new_left_nums

ans2 = 0
for testval, num in zip(testvals, nums):
    right_nums = [x for x in num]
    pos = possible_solutions2([], right_nums)
    if testval in pos:
        ans2 += testval


