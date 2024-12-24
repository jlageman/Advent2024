dat = open('input24.txt').read().splitlines()
wires = {}
for i, line in enumerate(dat):
    if len(line)<1:
        break
    gate, val = line.split(': ')
    wires[gate] = int(val)
operations = {}
op_order = []
for line in dat[i+1:]:
    op, gate = line.split(' -> ')
    op_order.append(gate)
    operations[gate]=op.split()

# part 1
i = -1
b = ''
while op_order:
    i += 1
    op = op_order[i]
    g1, operator, g2 = operations[op]
    if g1 in wires.keys() and g2 in wires.keys():
        op_order.pop(i)
        i = -1
    else:
        continue
    if operator=='AND':
        if wires[g1] and wires[g2]:
            val = 1
        else:
            val = 0
    elif operator=='OR':
        if wires[g1] or wires[g2]:
            val = 1
        else:
            val = 0
    elif operator=='XOR':
        if wires[g1] != wires[g2]:
            val = 1
        else:
            val = 0
    wires[op] = val

b = ''
for gate in sorted(wires.keys()):
    if gate[0]=='z':
        b += str(wires[gate])
b = b[::-1]
ans = int(b, 2)

# part 2
