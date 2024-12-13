dat = open('input13.txt').read().splitlines()
dat = [line for line in dat if len(line)>0]

prev_i = 0
ans = 0
ans2 = 0
# loop over all machines
for i in range(3, len(dat)+1, 3):
    # define machine settings
    for line in dat[prev_i:i]:
        if 'Button A' in line:
            ax = int(line.split(': ')[1].split(', ')[0].split('+')[1])
            ay = int(line.split(': ')[1].split(', ')[1].split('+')[1])
        elif 'Button B' in line:
            bx = int(line.split(': ')[1].split(', ')[0].split('+')[1])
            by = int(line.split(': ')[1].split(', ')[1].split('+')[1])
        elif 'Prize' in line:
            Px = int(line.split(': ')[1].split(', ')[0].split('=')[1])
            Py = int(line.split(': ')[1].split(', ')[1].split('=')[1])
    # part 1
    A = (Px*by - Py*bx) / (ax*by - ay*bx)
    B = (ax*Py - ay*Px) / (ax*by - ay*bx)
    if A==int(A) and B==int(B):
        ans += int(3*A + B)
    # part 2
    Px += 10000000000000
    Py += 10000000000000
    A = (Px*by - Py*bx) / (ax*by - ay*bx)
    B = (ax*Py - ay*Px) / (ax*by - ay*bx)
    if A==int(A) and B==int(B):
        ans2 += int(3*A + B)
    # next
    prev_i = i