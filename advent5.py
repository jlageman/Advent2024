# prepare data
dat = open('input5.txt').read().splitlines()
rules = [line.split('|') for line in dat if '|' in line]
rdict = {}
for rule in rules:
    if rule[0] not in rdict.keys():
        rdict[rule[0]] = [rule[1]]
    else:
        rdict[rule[0]].append(rule[1])
updates = [line.split(',') for line in dat if ',' in line]

# part 1
ans = 0
incorrect_updates = []
for update in updates:
    correct = True
    for i,num in enumerate(update):
        if num not in rdict.keys():
            continue
        if len(set(update[:i]).intersection(rdict[num]))>0:
            correct = False
            break
    if correct:
        ans += int(update[len(update)//2])
    else:
        incorrect_updates.append(update)

# part 2
ans2 = 0
def check_update(update, rdict):
    new_update = [x for x in update]
    for i,num in enumerate(update):
        if num not in rdict.keys():
            continue
        mistakes = set(new_update[:i]).intersection(rdict[num])
        if len(mistakes)>0:
            for m in mistakes:
                new_update.insert(new_update.index(m), new_update.pop(new_update.index(num)))
                return check_update(new_update, rdict)
    return new_update

for update in incorrect_updates:
    new_update = check_update(update, rdict)
    ans2 += int(new_update[len(new_update)//2])