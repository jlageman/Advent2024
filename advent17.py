dat = open('input17.txt').read().splitlines()
program = [int(x) for x in dat[4].split(': ')[1].split(',')]

def do_operation(instruction_pointer, opcode, operand, register):
    combos = '0123ABC'
    if opcode in [0,6,7]:
        regs = 'A.....BC'
        numerator = register['A']
        if operand <= 3:
            denominator = 2**operand
        else:
            denominator = 2**register[combos[operand]]
        result = int(numerator/denominator)
        register[regs[opcode]] = result
        return instruction_pointer+2, register, ''
    
    elif opcode in [1, 4]:
        register['B'] = register['B'] ^ (operand if opcode==1 else register['C'])
        return instruction_pointer+2, register, ''
    
    elif opcode == 2:
        if operand > 3:
            operand = register[combos[operand]]
        register['B'] = operand % 8
        return instruction_pointer+2, register, ''
    
    elif opcode == 3:
        if register['A']==0:
            return instruction_pointer+2, register, ''
        else:
            return operand, register, ''
    
    elif opcode == 5:
        if operand > 3:
            operand = register[combos[operand]]
        output = str(operand % 8) + ','
        return instruction_pointer+2, register, output
    
def run_program(A, program):
    register = {'A': A, 'B': 0, 'C': 0}
    instruction_pointer = 0
    output = ''
    while instruction_pointer < len(program)-1:
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        instruction_pointer, register, o = do_operation(instruction_pointer, opcode, operand, register)
        output = output + o
    return output[:-1]

# part 1
ans = run_program(int(dat[0].split(': ')[1]), program)
    
# part 2
initA = [0]
for o in program[::-1]:
    prevA = []
    for regA in initA:
        for i in range(8):
            a = 8 * regA + i
            for b in range(8):
                if a % 8 == b:
                    # program outputs (regB ^ regC) % 8
                    # define regB and regC as function of initial a & b value
                    if (((b ^ 1) ^ 4) ^ int(a / 2**(b ^ 1))) % 8 == o:
                        prevA.append(a)
    initA = [a for a in prevA if a > 0]
ans2 = min(initA)