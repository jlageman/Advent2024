dat = open('input3.txt').read()

# part 1 + 2
ans = 0
ans2 = 0
enable = True
ndat = dat.split('mul(')
for item in ndat:
    c = ''.join([x for x in item])
    if item[0] not in '1234567890' or ')' not in item:
        continue
    item = item.split(')')[0]
    if ',' not in item or any([x in ' abcdefghijklmnopqrstuvwxyz!@#$%^&*()-' for x in item]):
        continue
    item = item.split(',')
    if len(item[0])>3 or len(item[1])>3:
        continue
    ans += (int(item[0])*int(item[1]))
    if enable:
        ans2 += (int(item[0])*int(item[1]))
    if "don't()" in c:
        enable = False
    if 'do()' in c:
        enable = True