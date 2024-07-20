##Annabelle Crescenzo, Ayushi Gupta
##I pledge my honor that I have abided by the Stevens Honor System
##Assembler
##Turn assmebly language into machine code
##8 bit AA BB CC DD
##AA --> operation (ADD, SUB, LDR)
##BB --> destination
##CC --> operand 1
##DD --> operand 2

##ADD opcode = 00
##SUB opcode = 01
##LDR opcode = 10

##STEP 1
#uploading a text file

##STEP 2
#determine which areas of file are .data and .text segments 

##STEP 3
#compare string with available instructions and registers (ADD, SUB, LDR) (X0, X1, X2, X3)
#return binary code (00, 01, 10) (00, 01, 10, 11)

##STEP 4a
#for each line in the .text of file
#assume all instructions are in format of op dest reg1 reg2
#split line at spaces into 4 strings

##STEP 4b
#for each line in .data of file
#turn all data values in hexadecimals

##STEP 5
#create new text file for instruction memory

##STEP 6
#create new text file for data memory


#######################################################################


##STEP 1
with open('assembly.txt') as f:
    x = [(line.strip()) for line in f.readlines()]


##STEP 2
#determines whether .text or .data segment in assembly file
t = x.index('.text') #0
d = x.index('.data') #10

text = x[t:d]
while("" in text):
    text.remove("")

data = x[d:]
while("" in data):
    data.remove("")


##STEP 3
##determine binary machine code
def binaryCode(op, de, r1, r2 = '00'):
    if op == "LDR":
        bincode = "10"
    elif op == "ADD":
        bincode = "00"
    elif op == "SUB":
        bincode = "01"

    if de == 'X0':
        bincode += '00'
    elif de == 'X1':
        bincode += '01'
    elif de == 'X2':
        bincode += '10'
    elif de == 'X3':
        bincode += '11'

    if r1 == 'X0':
        bincode += '00'
    elif r1 == 'X1':
        bincode += '01'
    elif r1 == 'X2':
        bincode += '10'
    elif r1 == 'X3':
        bincode += '11'

    if r2 == 'X0':
        bincode += '00'
    elif r2 == 'X1':
        bincode += '01'
    elif r2 == 'X2':
        bincode += '10'
    elif r2 == 'X3':
        bincode += '11'
    else:
        bincode += r2
    return bincode


##STEP 4a, 5
##creates a new text file to hold the hex values for INSTRUCTION MEMORY
with open('instructionImage.txt', 'w') as n:

    ##added to be able to directly load into Logisim RAM
    n.write('v3.0 hex words addressed\n')
    n.write('00: ')

    ##STEP 2
    ##splits the instruction by spaces into each field
    for i in text[1:]:
        split = i.split()

        ##LDR with two registers, so 3 fields
        if len(split) == 3:
            oper, dest, reg1 = [split[s] for s in range(3)]
            instruction = binaryCode(oper, dest, reg1)

            instruction = '0b'+instruction
            hexI = format((int(instruction, 2)), '02x')
            n.write(hexI+' ')
            
        ##ADD and SUB instructions, so 4 fields
        else:
            oper, dest, reg1, reg2 = [split[s] for s in range(4)]
            instruction = binaryCode(oper, dest, reg1, reg2)
            
            instruction = '0b'+instruction
            hexI = format((int(instruction, 2)), '02x')
            n.write(hexI+' ')


##STEP 4b, 6
##creates a new text file to hold the hex values for DATA MEMORY
with open('dataImage.txt', 'w') as m:

    ##added to be able to directly load into Logisim RAM
    m.write('v3.0 hex words addressed\n')
    m.write('00: ')

    for i in data[1:]:
        hexD = format((int(i, 10)), '02x')
        m.write(hexD + ' ')
        
    
    


