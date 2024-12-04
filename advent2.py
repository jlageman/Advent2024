dat = open('input2.txt').read().splitlines()

# part 1
ans = 0
safelines = []
for n, line in enumerate(dat):
    line = [int(x) for x in line.split(' ')]
    if len(set(line))!=len(line):
        continue
    safe = True
    incr = 1 if line[0]<line[1] else -1
    for i in range(len(line)-1):
        if (line[i+1]-line[i])*incr < 1 or (line[i+1]-line[i])*incr > 3:
            safe = False
            break
    if safe:
        ans += 1
        safelines.append(n)

# part 2
ans2 = ans
for n, line in enumerate(dat):
    if n in safelines:
        continue
    line = [int(x) for x in line.split(' ')]
    for ni in range(len(line)):
        newline = [x for i,x in enumerate(line) if i!=ni]
        if len(set(newline))!=len(newline):
            continue
        safe = True
        incr = 1 if newline[0]<newline[1] else -1
        for i in range(len(newline)-1):
            if (newline[i+1]-newline[i])*incr < 1 or (newline[i+1]-newline[i])*incr > 3:
                safe = False
                break
        if safe:
            ans2 += 1
            break

        
    
    
                
    
        
    