	# ECE366Group7
	ISA Functions:

	lw	      00001 x y			Loads from memory to $1 or $4
	sw        	001 x iii  		Stores $1 or $2 into memory at M[0:7]
	init  	        011 xx ii		Initializes $xx to be an unsigned imm [0:3]	
	shiftL	      01010 xx			$xx << 1
	shiftR	      01011 xx			$xx >> 1
	bgtR1	       0001 x ii    		Branches if $2 or $4 is greater than $1 by unsigned imm [1:4]
	bltR1	       1001 x ii		Branches if $2 or $4 is less than $1 by unsigned imm [1:4]
	sub	       0100 xx y 		$xx = $xx - $y		x:[1:4] y:[1 or 3]
	add	       1000 xx y		$xx = $xx + $y		x:[1:4] y:[1 or 3]
	j		 11 iiiii		jumps to PC = imm[0:31]
	increment    000001 x 			Increments either $3 or $4 by 1
	decrement   0000000			Increments $4 by -1

	Psudo code for project 1:

	Load M[0] into $1
	Load M[1] into $2
	As long as $1 > $2: $1 = $1 - $2
	When it isnt $1 = $1 * 6
	Then repeat $1 = $1 - $2
	Store final value into M[2]
		
	Psudo code for project 2:
	
	Load M[3] into $1	
	Load M[3+n] into $2
	xor of $1 and $2 into $3
	
	
				init $4, 3				$4 = 3
				lw $1, $4				$1 = M[$4] = M[3]
				shiftL $4, 1				$4 = 6
				shiftL $4, 1				$4 = 12
				increment $4			$4 = 13
				shiftL $4, 1				$4 = 26
				increment $4			$4 = 27
				shiftL $4, 1				$4 = 54
				shiftL $4, 1				$4 = 108
newWord:		decrement				$4 = $4 - 1
				lw $2, $4				$2 = M[$4]
				bltR1 $2 notEqual		If $2 > $1, it doesn't equal $1
				bgtR1 $2 notEqual		If $2 < $1, it doesn't equal $1
				increment $3			If $2 isnt > or < than $1, it equals $1, increment best matching count
notEqual:		init $1 2				$1 = 2
				shift $1 1				$1 = 4
				shift $1 1				$1 = 8
				bltR1 $4 noMoreWords	If $4 < 8, all words have been checked
				j newWord				If all words have not been checked, jumps to next word
noMoreWords:	init $1, 0				Sets $1 to 0
				add $2, $3				$1 = $3 (Best_matching_count)
				bgtR1 $2, exactFound	If $2 > 0, a best match was found
				sw $1, 5				
				sw $1, 4				Incase a best isnt found, stores 0 into M[4] and M[5]
				j done					
exactFound:		sw $2, 5				M[5] = best_matching_count
				init $1, 2				$1 = 2
				shiftL $1				$1 = 4
				shiftL $1				$1 = 8
				shiftL $1				$1 = 16
				sw $1, 4
done
