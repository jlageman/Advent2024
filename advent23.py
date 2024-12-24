dat = open('input23.txt').read().splitlines()
connections = {}
for line in dat:
    com1, com2 = line.split('-')
    for A, B in zip([com1, com2], [com2, com1]):
        if A not in connections.keys():
            connections[A] = [B]
        else:
            connections[A].append(B)

# part 1
ans = 0
sets = []
for com, connection in connections.items():
    for c in connection:
        common = [x for x in connections[c] if x in connection]
        for i in range(len(common)):
            sets.append(tuple(sorted((com, c, common[i]))))
sets = list(set(sets))
for s in sets:
    if any([x[0]=='t' for x in s]):
        ans += 1
        
# part 2
largest_party = []
for s in sets:
    party = list(s)
    for com in connections[s[0]]:
        if len(set(connections[com]).intersection(party))>=len(party):
            party.append(com)
    if len(party)>len(largest_party):
        largest_party = sorted(party)
ans2 = ','.join(largest_party)
