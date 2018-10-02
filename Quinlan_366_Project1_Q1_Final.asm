.data
P: .word 1005	# 8	201	1005
R: .word -1

.text
		lw $s0, 0x2000($0)		#	Loads the word from M[0x2000] into $s0
		sll $s0, $s0, 28		#	The only byte we care about is the 8th byte of the word, as can be demonstrated by our algorithm
		slt $s1, $s0, $0		#	Checks if the byte is greater than 7 or less than 8 by utilizing the fact 0x8 or above is negative while 0x7 or below is positive
		srl $s0, $s0, 28		#	Scrolls $s0 back to its original position, except now the front 7 bytes are 0's
		bne $s1 $0, gTSeven		#	Sends the code to the negative branch if the left-shifted P input produced a negative number ( (P mod 16) > 8)
		
		addi $t0, $0, 0x00000000			
		bne $t0, $s0, notZero		#	When $t0 = $s0, our algorithm tells us what (6 ^ P) mod 17 will give us
		addi $s1, $0, 6
		j done
		
notZero:	addi $t0, $0, 0x00000001		
		bne $t0, $s0, notOne		#	X(P) is defined as X = (P mod 16), Y(P) is defined as Y = ((6 ^ P) mod 17 )
		addi $s0, $0, 2
		j done
						#	(Shift left 28 then shift right 28 perfectly produces a result X(P) bounded between 0 and 15.)				
notOne:		addi $t0, $0, 0x00000002				
		bne $t0, $s0, notTwo		#	My algorithm gives these (X, Y) pairs:
		addi $s1, $0, 12		#		(0, 6) (1, 2) (2, 12) (3, 4) (4, 7) (5, 8)
		j done				#	(X,Y):	(6, 14) (7, 16) (8, 11) (9, 15) (10, 5)
						#		(11, 13) (12, 10) (13, 9) (14, 3) (15, 1)
notTwo:		addi $t0, $0, 0x00000003
		bne $t0, $s0, notThree
		addi $s1, $0, 4
		j done
						#	Code is set up such that when P is inputted into $s0, it is converted into X and from X into Y.
notThree:	addi $t0, $0, 0x00000004	#	With Y being the value to store into memory
		bne $t0, $s0, notFour		#	This method avoids all loops and has been designed to minimize redundant computation
		addi $s1, $0, 7
		j done
						#	Example code block explained: (all code blocks work this way, just with different values)
notFour:	addi $t0, $0, 0x00000005	#	Start by setting $t0 to the next value that is checked
		bne $t0, $s0, notFive		#	Check if $t0 = $s0, if so we're done testing values and can move on
		addi $s1, $0, 8			#	Set $s1 to the Y value corresponding to the X value that was found
		j done				#	Jumps to done (Which stores the new s1 value to memory)
		
notFive:	addi $t0, $0, 0x00000006
		bne $t0, $s0, notSix
		addi $s1, $0, 14
		j done
		
notSix:		addi $t0, $0, 16		#	This is valid because the code can only get to this point if $s0 is between 0 and 7
		j done				#	If we know its not 0-6, we can know it is 7 without verifying
		
gTSeven:	addi $t0, $0, 0x00000008
		bne $t0, $s0, notEight
		addi $s1, $0, 11
		j done
			
notEight:	addi $t0, $0, 0x00000009
		bne $t0, $s0, notNine
		addi $s1, $0, 15
		j done
		
notNine:	addi $t0, $0, 0x0000000a	
		bne $t0, $s0, notTen	
		addi $s1, $0, 5			
		j done
					
notTen:		addi $t0, $0, 0x0000000b
		bne $t0, $s0, notEleven
		addi $s1, $0, 13
		j done
						
notEleven:	addi $t0, $0, 0x0000000c
		bne $t0, $s0, notTwelve
		addi $s1, $0, 10
		j done
				
notTwelve:	addi $t0, $0, 0x0000000d
		bne $t0, $s0, notThirteen
		addi $s1, $0, 9
		j done
		
notThirteen:	addi $t0, $0, 0x0000000e
		bne $t0, $s0, notFourteen
		addi $s1, $0, 3
		j done
		
notFourteen:	addi $s1, $0, 1			#	This again is possible because we know $s0 is between 8 and 15 in this branch, and it has to be greater than 14.
						
done:		sw $s1, 0x2004($0)		#	Stores (6 ^ P) mod 17 into M[0x2004]
