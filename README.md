	# ECE366Group7
	ISA Functions:

	lw        00001 x y	Either loads into $1 or $2 from the address at $0 or $1
	bneR1     0001 x ii    	Branches if $0 or $2 is not equal to $1 forward by imm [1:4]
	shiftR1   100 iiii    	Shifts $1 by a signed imm [-8:7]
	end       0000000     	Freezes the CPU
	sw        001 x y ii  	Stores $1 or $3 into memory at $0 or $2 shifted by 0x0 0x2 0x4 or 0x6
	init      01 iiiii   	Initializes $1 to be an unsigned imm [1:32]
	sub1R2    0000001     	Subtracts 1 from $2
	andi      1000000     	Performs an andi operation into $3 of $2 and 1
	add	  101 xx yy	$xx = $xx + $yy
	xor	  0000010	Performs xor operation on $1 and $2 outputting into $3
	sub	  110 xx yy 	$xx = $xx - $yy
	sInit	  111 x iii 	$x = [-4,3] ($x is either $2 or $3)

	Machine code for Project 1:

	Assumes data starts at 0x0000, $0 always equal to 0

			Code				Machine Code		Comments

			lw $1, $0			(1)000 0100		($1's value is the value from M[0])
			shiftR1 6			(1)100 0110		($1 shifted left half way across the halfword of data)
			shiftR1 6			(1)100 0110		($1 shifted left the rest of the way so that the least significant byte is now the most)
			shiftR1 -6			(1)100 1010		($1 shifted half way back)
			shiftR1 -6			(1)100 1010		($1 shifted all the way back leaving only the east significant byte)
			bneR1 $0, notZero		(1)000 1011
			init $1, 1			(0)010 0001	
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notZero		init $1, 1			(1)010 0000		($1 is set to 1)
			bneR1 $2 notOne			(0)000 1111		(Branches to notOne if $1 is not equal to 1)
			init $1, 6			(1)010 0101		(If $1 is equal to 1, sets $1 equal to 6)	
			sw $1 0x2($0)			(0)001 0001		(And then stores that into memory at 0x2)
			end				(0)000 0000		(Ends the program)
				
	notOne		init $1, 2			(0)010 0001		(All code blocks work this way, so they are not all commented)
			bneR1 $2 notTwo			(0)000 1111		
			init $1, 2			(0)010 0001	
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
					
	notTwo		init $1, 3			(0)010 0010
			bneR1 $2 notThree		(0)000 1111
			init $1, 12			(0)010 1011
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notThree	init $1, 4			(1)010 0011
			bneR1 $2 notFour		(0)000 1111
			init $1, 4			(1)010 0011
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notFour		init $1, 5			(0)010 0100
			bneR1 $2 notFive		(0)000 1111
			init $1, 7			(1)010 0110
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
					
	notFive		init $1, 6			(1)010 0101
			bneR1 $2 notSix			(0)000 1111
			init $1, 8			(0)010 0111
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notSix		init $1, 7			(1)010 0110
			bneR1 $2 notSeven		(0)000 1111
			init $1, 14			(0)010 1101
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notSeven	init $1, 8			(0)010 0111
			bneR1 $2 notEight		(0)000 1111
			init $1, 16			(1)010 1111	
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notEight	init $1, 9			(0)010 1000
			bneR1 $2 notNine		(0)000 1111
			init $1, 11			(1)010 1010
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
						
	notNine		init $1, 10			(1)010 1001
			bneR1 $2 notTen			(0)000 1111
			init $1, 13			(1)010 1100
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
					
	notTen		init $1, 11			(1)010 1010
			bneR1 $2 notElev		(0)000 1111
			init $1, 5			(0)010 0100
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notElev		init $1, 12			(0)010 1011
			bneR1 $2 notTwelv		(0)000 1111
			init $1, 13			(1)010 1100
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notTwelv	init $1, 13			(1)010 1100
			bneR1 $2 notThir		(0)000 1111
			init $1, 10			(1)010 1001
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notThir		init $1, 14			(0)010 1101
			bneR1 $2 notFourt		(0)000 1111
			init $1, 9			(0)010 1000
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000
				
	notFourt	init $1, 3			(0)010 0010
			sw $1 0x2($0)			(0)001 0001
			end				(0)000 0000

			

