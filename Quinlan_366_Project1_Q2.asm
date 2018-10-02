.data
T: .word -5
best_matching_score: .word -1 # best score = ? within [0, 32]
best_matching_count: .word -1 # how many patterns achieve the best score?
Pattern_Array: 1, -2, 3, -4, 5, -6, 7, -8, 9, -10, -5, 5,
-5, 5, -5, 1, -2, 3, -4, 5 
.text
		lw $s0, 0x2000($0)	#Loads target word into $s7
		addi $s1, $0, 0x200c	#Initializes $s0 to the first word in the list at memory 0x0000200c
newWord:	lw $s2, 0($s1)		#Loads the next word into $s2
		addi $t0, $0, 32	#Initializes match count to 32
		addi $t1, $0, 32	#Initializes remaining bits to 32
		xor $s3, $s2, $s0	#Sets all bits the two numbers dont have in common to 1
loop:		andi $s4, $s3, 1	#Sets $s4 to 1 if $s3 is 1
		srl $s3, $s3, 1		#Scrolls $s3's data left 1 bit
		sub $t0, $t0, $s4	#Subtracts 1 from word score if $s4 was set to 1
		subi $t1, $t1, 1	#Subtracts 1 from remaining bits to check
		bne $t1, $0, loop	#Branches to the next bit until all bits are checked
		lw $t2, 0x2004($0)	#Loads current highest score acheived
		beq $t2, $t0, sameAsMax	#Branches to increment best_matching_count
		slt $t3, $t2, $t0	#Sets $t3 to 1 if theres more matches in the current word than any previous word
		beq $t3, $0, done	#Branches out if the current word is not the new best word
		sw $t0, 0x2004($0)	#Stores the score in 0x2004 if its better than all previous words
		addi $t4 $0 1		#Sets $t4 to 1 so that 1 can be set into best_matching_count, as a new best has been found
		sw $t4 0x2008($0)	#Resets best matching count to 1
		j done			#jumps to the end of the loop
sameAsMax:	addi $t4, $t4, 1	#Increments best_matching_count
		sw $t4, 0x2008($0)	#Stores the incremented best_matching_count
done:		addi $s1, $s1, 0x4	#Increments $s1 so the next word can be loaded
		slti $t5, $s1, 0x205C	#Sets $t5 to 1 until $s1 scrolls through all word addresses
		bne $t5, $0, newWord	#Branches back up the analyze the next word until $s1 = 0x205C (all words have been checked)
