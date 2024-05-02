with open('assembler_sample.txt') as t:
    data = []
    for line in t.readlines():
        data.append(line.split())
#print(data)

symbols = []
value = 0
def contains(string):
    string = list(string)
    for i in string:
        if i == "F":
            return 4
        elif i =="D":
            return 8
    return 1

def contains_literal(string):
    string = list(string)
    if "=" in string:
        return True

for j, i in enumerate(data):
    
    if len(i) == 2 and i[0].lower() == "using":
        value = 0
        continue

    if len(i) == 2:
        value += 4
    if j == 1:
        value = 0
        continue

    if len(i) == 3:
        length = contains(i[2])
        if i[1].lower() == "eqv":
            symbols.append([i[0], int(i[2]), length, 'A'])
            base = int(i[2])
        else:
            symbols.append([i[0], value, length, "R"])
            if(length != 4):
              value += length
            else:
              value += 4

print("OUTPUT of Pass 1\n\nSymbol Table (ST)")
print("Symbol\tValue\t\tLength\tRelocation")
for i in symbols:
    print(i[0],"\t",hex(i[1])[2:],'(',i[1],')',"\t",i[2],"\t",i[3])

literals = []
lvalue = value

for j, i in enumerate(data):
  if len(i) == 2:
    if contains_literal(i[1]):
      a = list((i[1].split('='))[1] )
      length = contains(a[0])
      literals.append([(i[1].split(','))[1], lvalue, length, "R"])
      if(length != 4):
        lvalue += length
      else:
        lvalue += 4
      #print(a)
print("\nLiteral Table (LT)")
print("Literal\tValue\t\tLength\tRelocation")
for i in literals:
    print(i[0],"\t",hex(i[1])[2:],'(',i[1],')',"\t",i[2],"\t",i[3])

main = symbols + literals
mot = [['L',int('58', 16)],['ST',int('50', 16)],['A',int('5A', 16)]]

# Define pseudo opcode table
pseudo_opcodes = {
    'START': '00',
    'END': '01',
    'USING': '02',
    'DC':'03',
    'EQU':'04'
}

# Function to get opcode from pseudo opcode table
def get_pseudo_opcode(op):
    return pseudo_opcodes.get(op, None)

def getOpHex(op):
    opcode_hex = get_pseudo_opcode(op)
    if opcode_hex is None:
        for i in mot:
            if i[0] == op:
                return i[1]
    return 

def getOpOperand(op):
    for i in main:
        if i[0] == op:
            return i[1]
    return 
print("------------------------------------------------------------------")
print("\nOUTPUT of Pass 2\n\nMachine Code")
print("Instruction\tMachine Code")

one = 100   
for i, j in enumerate(data[2:], 1):
    if len(j) == 2: 
        final = getOpHex(j[0]) + getOpOperand(j[1].split(',')[1]) + one + base
        print(j[0], '\t\t',hex(final)[2:],'(',final,')')

# Print pseudo opcode table
print("\nPseudo Opcode Table")
print("Opcode\tHex")
for mnemonic, opcode in pseudo_opcodes.items():
    print(mnemonic, "\t", opcode)

bases = []
for i in range(0,16):
  if(i == base):
    bases.append(['Y',000000])
  else:
    bases.append(['N',None])
print("\nBase Table (BT)")
print("Base Availability Indicator Contents")
for j,i in enumerate(bases):
    if(i[1] == 0):
      print(j,"\t",i[0],"\t\t",str(i[1]) * 6)
    else:
      print(j,"\t",i[0])
      
