

def clean(input):
    input = input.split("\n")
    input = [i.strip() for i in input]
    return input
    

def phase_one(input):
    for line in range(len(input)):
        # print(i)
        i = input[line]
        temp = i.split(' ')
        # print(temp)
        if len(temp) > 2 and temp[1].lower() == 'macro':
            # print(i)
            index = len(MDT)
            MNT.append([index, temp[0]])
            line += 1
            while line < len(input):
                curr = input[line]
                MDT.append(curr)
                curr_split = curr.split(' ')
                if curr_split[0].lower() == 'endm':
                    break
                line += 1

    print_mdt()
    print_mnt()

def check_for_macro(line):
    if len(line) < 2:
        return -1
    
    for name in MNT:
        if line[0] in name and line[1].lower() != 'macro':
            return name[0]

    return -1

def phase_two():
    res = []
    for i in range(len(input)):
        line = input[i]
        temp = line.split(' ')
        index = check_for_macro(temp)
        if index != -1:
            ALA.append(temp[1])
            while (MDT[index].lower() != "endm"):
                temp_line = MDT[index]
                if 'XX' in temp_line:
                    temp_line = temp_line.replace("XX", temp[1])
                res.append(temp_line)
                index += 1
        else:
            res.append(line)
    print_ala()
    return res

def print_mdt():
    print("Macro Defination Table : ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Index \tMacro Definition")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(MDT)):
        print(f" {i}\t{MDT[i]}")
    print("\n\n")

def print_mnt():
    print("Macro Name Table : ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Index on MDT\tMacro Name")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for name in MNT:
        print(f" {name[0]}\t\t{name[1]}")
    print("\n\n")

def print_ala():
    print("Argumrnt List Array : ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("index\tArgument Name")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(len(ALA)):
        print(f" {i}\t{ALA[i]}")
    print("\n\n")

# MDT : Macro Definition Table
MDT = []
# MNT : Macro Name Table
MNT = []
# ALA : Argument List Array
ALA = []

input = ""
with open('macro_processor_sample.asm','r') as f:
    input = f.read()

input = clean(input)
# print(input)
phase_one(input)
res = phase_two()

print('\n--------------OUTPUT--------------------')
for i in res:
    print(i)

# --------------------------------
# .model
# .stack
# .data
# MSG1 DB 10,13,Welcome$
# MSG2 DB 10,13,TCET$

# .code
# DISP MACRO XX
# MOV AH,09
# LEA DX,XX
# INT 21H
# ENDM

# .startup
# DISP MSG1
# DISP MSG2

# .exit
# end