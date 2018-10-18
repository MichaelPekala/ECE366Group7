print("ECE366 Fall 2018 mini ISA assembler, supporting: lw, sw, init, shiftL, shiftR, ")
print("bgtR0, bltR0, sub, add, j")
print("--------")

input_file = open("ISA_asm.txt", "r")
output_file = open("ISA_machine_code.txt","w")
jmpList = []
jmpNum = []
count = 0
for line in input_file:
    line = line.replace("\t", "")
    line = line.replace(" ","")     # remove spaces anywhere in line
    if (line == "\n"):              # empty lines ignored
        continue
    line = line.replace("\n","")
    for i in range(0,len(line)):
        if(line[i] == ':'):
            jmpList.append(line[0:i])
            jmpNum.append(count)
            break;
    count = count + 1

input_file.close()
input_file = open("ISA_asm.txt", "r")
count = 0

def parity(m_code):
    print("(" + str(m_code.count('1')%2) + ")", end='')
    return str(m_code.count('1')%2)

for line in input_file:
    line = line.replace("\t", "")
    line = line.replace(" ","")     # remove spaces anywhere in line
    if (line == "\n"):              # empty lines ignored
        continue
    
    line = line.replace("\n","")    # remove 'endline' character

   #lw $0($1), $0($3)
   #lw rt, rs
    for i in range(0, len(jmpNum)):
        if count == jmpNum[i]:
            x=len(jmpList[i])
            line = line.replace(line[0:x], '', 1) 
            line = line.replace(":", "")
    print("Instr: ", line)          # show the asm instruction to screen
    
    if(line[0:2] == 'lw'):                # addi:
        line = line.replace("$","")         # remove $'s anywhere
        line = line.replace("lw","")      # "addi $13, $15, 100" will be split
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.split(',')              # into three strings: "23" "25" "100"
        count = count + 1
        op = "00001"
        if(line[0] == '0'):           #rt = $0
            rt = format(0, "01b")
        elif(line[0] == '1'):
            rt = format(1, "01b")  #rt = $1
        else:
            print("Error at lw: register destination")
            output_file.write("Error lw Reg dest \n")
            continue;

        if(line[1] == '0'):           #rs = $0
            rs = format(0, "01b")
        elif(line[1] == '2'):
            rs = format(1, "01b")  #rs = $1
        else:
            print("Error at lw: register source")
            output_file.write("Error lw Reg source\n")
            continue;
        p = parity(op+rt+rs)
        print(op + " " + rt + " " + rs + "\n")
        output_file.write(p + op + rt + rs + "\n")

        #sw $0($1), imm (0- 7)
        #     rt,   imm
    elif(line[0:2] == 'sw'):                # addi:
        line = line.replace("$","")         # remove $'s anywhere
        line = line.replace("sw","")      # "addi $13, $15, 100" will be split
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.split(',')              # into three strings: "23" "25" "100"
        count = count + 1
        op = "001"
        if(line[0] == '0'):           #rt = $0
            rt = format(0, "01b")
        elif(line[0] == '1'):
            rt = format(1, "01b")  #rt = $1
        else:
            print("Error sw destination");
            output_file.write("Error sw Reg dest\n")
            continue;

        if(int(line[1]) >= 0 and int(line[1]) < 8):   #imm[0-8]
            imm = format(int(line[1]), "03b")
        else:
            print("Error at sw")
            output_file.write("Error sw imm\n")
            continue;
        p = parity(op+rt+imm)
        print(op + " " + rt + " " + imm + "\n")
        output_file.write(p+op + rt + imm + "\n")

       #init rt imm
       #init $0($2)  imm:[0-3]
       #???
    elif(line[0:4] == 'init'):
        op = "011"
        count = count + 1
        line = line.replace("$","")         # remove $'s anywhere
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("init","")
        line = line.split(',')

        if(line[0] >= '0' and line[0] < '4'):
            rt = format(int(line[0]), "02b")
        else:
            print("Error at init")
            output_file.write("Error init Reg dest\n")
            continue;
        if(int(line[1]) >= 0 and int(line[1]) < 4):   #imm[0-8]
            imm = format(int(line[1]), "02b")
        else:
            print("Error at init")
            output_file.write("Error init imm\n")
            continue;
        p = parity(op+rt+imm)
        print(op + " " + rt + " " + imm + "\n")
        output_file.write(p + op + rt + imm + "\n")

    #?? shorter name and make the registers from 0-3
    #shiftL $0-$3
    elif(line[0:6] == 'shiftL'):
        op = "01010"
        count = count + 1
        line = line.replace("$","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("shiftL","")
        line = line.split(',')

        if(line[0] >= '0' and line[0] < '4'):
            rt = format(int(line[0]), "02b")
        else:
            print("Error at shiftL")
            output_file.write("Error shiftL reg\n")
            continue;
        p = parity(op+rt)
        print(op + " " + rt + " " + "\n")
        output_file.write(p + op + rt + "\n")

   #?? shorter name and make the registers from 0-3
    #shiftR $0-$3
    elif(line[0:6] == 'shiftR'):
        op = "01011"
        line = line.replace("$","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("shiftR","")
        line = line.split(',')
        count = count + 1
        if(line[0] >= '0' and line[0] < '4'):
            rt = format(int(line[0]), "02b")
        else:
            print("Error at shiftR")
            output_file.write("Error shiftR reg\n")
            continue;
        p = parity(op+rt)
        print(op + " " + rt + " " + "\n")
        output_file.write(p + op + rt + "\n")


        #sub $0-$3 $0($2)
    elif(line[0:3] == 'sub'):
        op = "0100"
        line = line.replace("$","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("sub","")
        line = line.split(',')
        count = count + 1
        if(line[0] >= '0' and line[0] < '4'):
            rt = format(int(line[0]), "02b")
        else:
            print("Error at sub")
            output_file.write("Error sub dest reg\n")
            continue;

        if(line[1] == '0'):
            rs = format(0, "01b")
        elif (line[1] == '2'):
            rs = format(1, "01b")
        else:
            print("Error at sub")
            output_file.write("Error sub source Reg\n")
            continue;
        p = parity(op+rt+rs)
        print(op + " " + rt + " "+ rs + " " + "\n")
        output_file.write(p + op + rt + rs + "\n")

    #addi $0-$3, imm[-2to1]
    elif(line[0:4] == 'addi'):
        op = "101"
        line = line.replace("$","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("addi","")
        line = line.split(',')
        count = count + 1
        if(line[0] >= '0' and line[0] < '4'):
            rt = format(int(line[0]), "02b")
        else:
            print("Error at addi: unknown register")
            output_file.write("Error addi source Reg\n")

        if(line[1] == '-2'):
            imm = '10'
        elif(line[1] == '-1'):
            imm = '11'
        elif(line[1] == '0'):
            imm = '00'
        elif(line[1] == '1'):
            imm = '01'
        else:
            print("Error at addi: invalid imm")
            output_file.write("Error addi imm\n")
            
        p = parity(op+rt+imm)
        print(op + " " + rt + " "+ imm + " " + "\n")
        output_file.write(p + op + rt + imm + "\n")
        
    #add $0-$3 $0($2)
    elif(line[0:3] == 'add'):
        op = "1000"
        line = line.replace("$","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("add","")
        line = line.split(',')
        count = count + 1
        
        if(line[0] >= '0' and line[0] < '4'):
            rt = format(int(line[0]), "02b")
        else:
            print("Error at add")
            output_file.write("Error add Reg dest\n")
            continue;
            
        if(line[1] == '0'):
            rs = format(0, "01b")
        elif (line[1] == '2'):
            rs = format(1, "01b")
        else:
            print("Error at add")
            output_file.write("Error add Reg source\n")
            continue;
        
        p = parity(op+rt+rs)
        print(op + " " + rt + " "+ rs + " " + "\n")
        output_file.write(p + op + rt + rs + "\n")

        #jump
    elif(line[0:1] == 'j'):
        op = "11"
        line = line.replace("j","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.split(',')
        count = count + 1
        imm = -1
        for m in range(0, len(jmpList)):
            if(line[0] == jmpList[m]):
                imm = format(int(jmpNum[m]), "05b")
                p = parity(op+imm)
                print(op + " " + imm + "\n")
                output_file.write(p + op + imm + "\n")
                continue;
        if (imm == -1):
            print("Error at j")
            output_file.write("Error jump cant be found\n")

    elif(line[0:5] == 'bgtR0'):
        op = "0001"
        line = line.replace("$","")
        line = line.replace("bgtR0","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.split(',')

        if(line[0] == '1'):           #rt = $1
            rt = format(0, "01b")
        elif(line[0] == '2'):
            rt = format(1, "01b")     #rt = $3
        else:
            print("Error at bgtR0 Register");
            output_file.write("Error bgtR0 Reg\n")
            continue;
        imm = -1
        for m in range(0, len(jmpList)):
            if(line[1] == jmpList[m]):
                x=int(jmpNum[m]-count)
                count = count + 1
                if (x > 0 and x < 5):
                    imm = format(x-1,"02b")
                    p = parity(op+rt+imm)
                    print(op + " " + rt + " " + imm + " " + "\n")
                    output_file.write(p + op + rt + imm + "\n")
                else:
                    print("Error at bgtR0 you can only jump forward by imm of 4")
                    output_file.write("Error bgtR0 jump only 4\n")
                continue
        if (imm == -1):
            print("Error at bgtR0: incorrect branch coordinate")
            output_file.write("Error bgtR0 unexpected\n")
            count = count + 1

    #bltR1 $1($3) imm[1-4]
    elif(line[0:5] == 'bltR0'):
        op = "1001"
        line = line.replace("$","")
        line = line.replace("(", ",")
        line = line.replace("#", ",")
        line = line.replace("bltR0","")
        line = line.split(',')

        if(line[0] == '1'):           #rt = $1
            rt = format(0, "01b")
        elif(line[0] == '2'):
            rt = format(1, "01b")  #rt = $3
        else:
            print("Error at bltR0: incorrect register");
            output_file.write("Error bltR0 Reg\n")
            continue;
        imm = -1
        for m in range(0, len(jmpList)):
             if(line[1] == jmpList[m]):
                 x=int(jmpNum[m]-count)
                 count = count + 1
                 if (x > 0 and x < 5):
                     imm = format(x-1,"02b")
                     p = parity(op+rt+imm)
                     print(op + " " + rt + " " + imm + " " + "\n")
                     output_file.write(p + op + rt + imm + "\n")
                 else:
                     print("Error at bltR0 you can only jump forward by imm of 4")
                     output_file.write("Error bltR0 can't go backward\n")
                 continue

        if (imm == -1):
            print("Error at bgtR0: incorrect branch coordinate")
            output_file.write("Error bgtR0 unexpected\n")
            count = count + 1

        
    else:
        print("Unknown instruction:"+ line)
        count = count + 1


input_file.close()
output_file.close()
