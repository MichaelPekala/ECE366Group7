# ECE366Group7
ISA Functions:

lw        00010 x y		Either loads into $1 or $2 from the address at $0 or $1
bneR1     0001 x ii    	Branches if $0 or $2 is not equal to $1 forward by imm [1:4]
shiftR1   100 iiii    	Shifts $1 by a signed imm [-8:7]
end       0000000     	Freezes the CPU
sw        001 x y ii  	Stores $1 or $3 into memory at $0 or $2 shifted by 0x0 0x2 0x4 or 0x6
init      01 x iiii   	Initializes $1 or $2 to be an unsigned imm [1:16]
sub1R2    0000001     	Subtracts 1 from $2
andi      1000000     	Performs an andi operation into $3 of $2 and 1

Machine code for project 1:

Assumes data starts at 0x0000, $0 always equal to 0

		Code				Machine Code		Comments

			lw $1, $0			0001000			($1's value is the value from M[0])
			shiftR1 6			1000110			($1 shifted left half way across the halfword of data)
			shiftR1 6			1000110			($1 shifted left the rest of the way so that the least significant byte is now the most)
			shiftR1 -6			1001010			($1 shifted half way back)
			shiftR1 -6			1001010			($1 shifted all the way back leaving only the least significant byte)
			bneR1 $0, notZero	0001011
			init $1, 1			0100001	
			sw $1 0x2($0)		0010001
			end					0000000
			
notZero		init $1, 1			0100000			($1 is set to 1)
			bneR1 $2 notOne		0001111			(Branches to notOne if $1 is not equal to 1)
			init $1, 6			0100101			(If $1 is equal to 1, sets $1 equal to 6)	
			sw $1 0x2($0)		0010001			(And then stores that into memory at 0x2)
			end					0000000			(And ends the program)
			
notOne		init $1, 2			0100001
			bneR1 $2 notTwo		0001111			(All code blocks work this way, so they are not all commented.)
			init $1, 2			0100001	
			sw $1 0x2($0)		0010001
			end					0000000
				
notTwo		init $1, 3			0100010
			bneR1 $2 notThree	0001111
			init $1, 12			0101011
			sw $1 0x2($0)		0010001
			end					0000000
			
notThree	init $1, 4			0100011
			bneR1 $2 notFour	0001111
			init $1, 4			0100011
			sw $1 0x2($0)		0010001
			end					0000000
			
notFour		init $1, 5			0100100
			bneR1 $2 notFive	0001111
			init $1, 7			0100110
			sw $1 0x2($0)		0010001
			end					0000000
				
notFive		init $1, 6			0100101
			bneR1 $2 notSix		0001111
			init $1, 8			0100111
			sw $1 0x2($0)		0010001
			end					0000000
			
notSix		init $1, 7			0100110
			bneR1 $2 notSeven	0001111
			init $1, 14			0101101
			sw $1 0x2($0)		0010001
			end					0000000
			
notSeven	init $1, 8			0100111
			bneR1 $2 notEight	0001111
			init $1, 16			0101111	
			sw $1 0x2($0)		0010001
			end					0000000
			
notEight	init $1, 9			0101000
			bneR1 $2 notNine	0001111
			init $1, 11			0101010
			sw $1 0x2($0)		0010001
			end					0000000
				
notNine		init $1, 10			0101001
			bneR1 $2 notTen		0001111
			init $1, 13			0101100
			sw $1 0x2($0)		0010001
			end					0000000
			
notTen		init $1, 11			0101010
			bneR1 $2 notElev	0001111
			init $1, 5			0100100
			sw $1 0x2($0)		0010001
			end					0000000
			
notElev		init $1, 12			0101011
			bneR1 $2 notTwelv	0001111
			init $1, 13			0101100
			sw $1 0x2($0)		0010001
			end
			
notTwelv	init $1, 13			0101100
			bneR1 $2 notThir	0001111
			init $1, 10			0101001
			sw $1 0x2($0)		0010001
			end					0000000
			
notThir		init $1, 14			0101101
			bneR1 $2 notFourt	0001111
			init $1, 9			0101000
			sw $1 0x2($0)		0010001
			end
			
notFourt	init $1, 3			0100010
			sw $1 0x2($0)		0010001
			end					0000000

		

