				
Program for Program 2					Machine Code			Comments
				
				init $3, 3		(0)0111011			$3 = 3
				lw $1, $3		(0)0000101			$1 = M[$4] = M[3]
				shiftL $3, 1		(1)0101010			$3 = 6
				shiftL $3, 1		(1)0101010			$3 = 12
				addi $3, 1		(0)1011001			$3 = 13
				shiftL $3, 1		(1)0101010			$3 = 26
				addi $3, 1		(0)1011001			$3 = 27
				shiftL $3, 1		(1)0101010			$3 = 54
				shiftL $3, 1		(1)0101010			$3 = 108
newWord:			addi $3, -1		(1)1011011			$3 = $3 - 1
				lw $2, $3		(1)0000111			$2 = M[$3]
				bltR1 $2 notEqual	(0)1001010			If $2 > $1, it doesn't equal $1
				bgtR1 $2 notEqual	(1)0001001			If $2 < $1, it doesn't equal $1
				addi $4, 1		(1)1011101			If $2 isnt > or < than $1, it equals $1, increment best matching count ($4)
notEqual:			init $1 2		(1)0110010			$1 = 2
				shiftL $1 1		(1)0101000			$1 = 4
				shiftL $1 1		(1)0101000			$1 = 8
				bltR1 $3 noMoreWords	(1)1001101			If $3 < 8, all words have been checked
				j newWord		(0)1101001			If all words have not been checked, jumps to next word
noMoreWords:			init $1, 0		(0)0110000			Sets $1 to 0
				add $2, $3		(1)1000110			$1 = $4 (Best_matching_count)
				bgtR1 $2, exactFound	(0)0001010			If $2 > 0, a best match was found
				sw $1, 5		(1)0010101
				sw $1, 4		(0)0010100			Incase a best isnt found, stores 0 into M[4] and M[5]
				j done			(1)1111111
exactFound:			sw $2, 5		(0)0011101			M[5] = best_matching_count
				init $1, 2		(1)0110010			$1 = 2
				shiftL $1		(0)0101000			$1 = 4
				shiftL $1		(0)0101000			$1 = 8
				shiftL $1		(0)0101000			$1 = 16
				sw $1, 4		(0)0010100
done				j done			(1)1111111			Pause

