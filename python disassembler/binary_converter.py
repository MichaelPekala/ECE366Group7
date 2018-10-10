print("ECE366 Fall 2018 mini ISA assembler, supporting: lw, sw, init, shiftL, shiftR, bgtR1, bltR1, sub, add, j, increment, decrement")
print("--------")

input_file = open("ISA_asm.txt", "r")
output_file = open("ISA_machine_code.txt","w")

for line in input_file:
    if (line == "\n"):              # empty lines ignored
        continue

    line = line.replace("\n","")    # remove 'endline' character
    print("Instr: ", line)          # show the asm instruction to screen
    line = line.replace(" ","")     # remove spaces anywhere in line
   

   #lw $1($2), $1($4)
   #lw rt, rs
    if(line[0:2] == 'lw'):                # addi: 
        line = line.replace("$","")         # remove $'s anywhere
        line = line.replace("lw","")      # "addi $23, $25, 100" will be split 
        line = line.split(',')              # into three strings: "23" "25" "100"

        op = "00001"
        if(line[0] == '1'):           #rt = $1
            rt = format(0, "01b")
        elif(line[1] == '2'):
            rt = format(1, "01b")  #rt = $2
        else:
            print("Error at lw")
            continue;

        if(line[1] == '1'):           #rs = $1
            rs = format(0, "01b")
        elif(line[1] == '4'):
            rs = format(1, "01b")  #rs = $2
        else:
            print("Error at lw")
            continue;
        print(op + " " + rt + " " + rs + "\n")     
        output_file.write(op + rt + rs + "\n")

        #sw $1($2), imm (0- 7)
        #     rt,   imm
    elif(line[0:2] == 'sw'):                # addi: 
        line = line.replace("$","")         # remove $'s anywhere
        line = line.replace("sw","")      # "addi $23, $25, 100" will be split 
        line = line.split(',')              # into three strings: "23" "25" "100"

        op = "001"
        if(line[0] == '1'):           #rt = $1
            rt = format(0, "01b")
        elif(line[1] == '2'):
            rt = format(1, "01b")  #rt = $2
        else:
            print("Error at sw");
            continue;
            
        if(int(line[1]) >= 0 and int(line[1]) < 8):   #imm[0-8]
            imm = format(int(line[1]), "03b")
        else:
            print("Error at sw")
            continue;
        print(op + " " + rt + " " + imm + "\n")
        output_file.write(op + rt + imm + "\n")
        
       #init rt imm
       #init $1($3)  imm:[0-3]
       #???
    elif(line[0:4] == 'init'):
        op = "011"                  

        line = line.replace("$","")         # remove $'s anywhere
        line = line.replace("init","")       
        line = line.split(',')              
        
        if(line[0] > '0' and line[0] < '5'):
            rt = format(int(line[0])-1, "02b")
        else:
            print("Error at init")
            continue;
        if(int(line[1]) >= 0 and int(line[1]) < 4):   #imm[0-8]
            imm = format(int(line[1]), "02b")
        else:
            print("Error at init")
            continue;
        print(op + " " + rt + " " + imm + "\n")
        output_file.write(op + rt + imm + "\n")

    #?? shorter name and make the registers from 0-3
    #shiftL $1-$4
    elif(line[0:6] == 'shiftL'):		    
        op = "01010"
        line = line.replace("$","")        
        line = line.replace("shiftL","")           
                                            
        if(line[0] > '0' and line[0] < '5'):
            rt = format(int(line)-1, "02b")
        else:
            print("Error at shiftL")
            continue;
        print(op + " " + rt + " " + "\n")
        output_file.write(op + rt + "\n")

   #?? shorter name and make the registers from 0-3
    #shiftR $1-$4
    elif(line[0:6] == 'shiftR'):		    
        op = "01010"
        line = line.replace("$","")        
        line = line.replace("shiftR","")           
                                            
        if(line[0] > '0' and line[0] < '5'):
            rt = format(int(line)-1, "02b")
        else:
            print("Error at shiftR")
            continue;
        print(op + " " + rt + " " + "\n")
        output_file.write(op + rt + "\n")
        
    #bgtR1 $2($4) imm[1-4]
    elif(line[0:5] == 'bgtR1'):		    
        op = "0001"
        line = line.replace("$","")        
        line = line.replace("bgtR1","")           
        line = line.split(',')
        
        if(line[0] == '2'):           #rt = $2
            rt = format(0, "01b")
        elif(line[1] == '4'):
            rt = format(1, "01b")  #rt = $4
        else:
            print("Error at bgtR1");
            continue;
            
        if(line[1] > '0' and line[1] < '5'):
            imm = format(int(line[1])-1, "02b")
        else:
            print("Error at bgtR1")
            continue;
        print(op + " " + rt + " " + imm + " " + "\n")
        output_file.write(op + rt + imm + "\n")
        
        #bltR1 $2($4) imm[1-4]
    elif(line[0:5] == 'bltR1'):		    
        op = "1001"
        line = line.replace("$","")        
        line = line.replace("bltR1","")           
        line = line.split(',')
        
        if(line[0] == '2'):           #rt = $2
            rt = format(0, "01b")
        elif(line[0] == '4'):
            rt = format(1, "01b")  #rt = $4
        else:
            print("Error at bltR1");
            continue;
            
        if(line[1] > '0' and line[1] < '5'):
            imm = format(int(line[1])-1, "02b")
        else:
            print("Error at bltR1")
            continue;
        print(op + " " + rt + " " + imm + " " + "\n")
        output_file.write(op + rt + imm + "\n")
        
        #sub $1-$4 $1($3)
    elif(line[0:3] == 'sub'):		    
        op = "0100"
        line = line.replace("$","")        
        line = line.replace("sub","")         
        line = line.split(',')
                                            
        if(line[0] > '0' and line[0] < '5'):
            rt = format(int(line[0])-1, "02b")
        else:
            print("Error at sub")
            continue;
            
        if(line[1] == '1'):
            rs = format(0, "01b")
        elif (line[1] == '3'):
            rs = format(1, "01b")
        else:
            print("Error at sub")
            continue;
        print(op + " " + rt + " "+ rs + " " + "\n")
        output_file.write(op + rt + rs + "\n")

    #add $1-$4 $1($3)
    elif(line[0:3] == 'add'):		    
        op = "1000"
        line = line.replace("$","")        
        line = line.replace("add","")         
        line = line.split(',')
                                            
        if(line[0] > '0' and line[0] < '5'):
            rt = format(int(line[0])-1, "02b")
        else:
            print("Error at add")
            continue;
            
        if(line[1] == '1'):
            rs = format(0, "01b")
        elif (line[1] == '3'):
            rs = format(1, "01b")
        else:
            print("Error at add")
            continue;
        print(op + " " + rt + " "+ rs + " " + "\n")
        output_file.write(op + rt + rs + "\n")
        
    elif(line[0:1] == 'j'):
        op = "11"  
        line = line.replace("j","")
        
        if (line >= '0' and line <= '31'):
            imm = format(int(line), "05b")
        else:
            print("Error at j")
            continue;
        print(op + " " + imm + "\n")
        output_file.write(op + imm + "\n")    
        
        #increment takes $3, $4
    elif(line[0:9] == 'increment'):
        line = line.replace('$', "")
        line = line.replace("increment", "")
        op = "000001"

        if (line == '3'):
            rt = format(0, "01b")
        elif (line == '4'):
            rt = format(1, "01b")
        else:
            print("Error at increment")
            continue;
        print(op + " " + rt + "\n")
        output_file.write(op + rt + "\n")          

        
            #decrement takes nothing
    elif(line[0:9] == 'decrement'):
        line = line.replace('$', "")
        line = line.replace("decrement", "")
        op = "0000000"

        print(op + "\n")
        output_file.write(op + "\n") 
        
    else:
        print("Unknown instruction:"+ line)

input_file.close()
output_file.close()
