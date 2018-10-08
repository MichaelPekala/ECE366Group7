	# ECE366Group7
	ISA Functions:

	lw        00001 x y		Either loads into $1 or $2 from the address at $0 or $1
	sw        001 x iii  	Stores $1 or $2 into memory at M[0:7]
	init      011 x iii		Initializes $1 to be an unsigned imm [-4:3]		reg [1:4]
	shiftR1   100 iiii    	Shifts $1 by a signed imm [-8:7]
	bneR1     0001 x ii    	Branches if $0 or $2 is not equal to $1 forward by imm [1:4]
	sub		  010 xx yy 	$xx = $xx - $yy		[1:4]
	add		  101 xx yy		$xx = $xx + $yy		[1:4]
	andi      1000000     	Performs an andi operation into $1 of $2 and $3
	xor		  0000010		Performs xor operation on $1 and $2 outputting into $3
	j		  11  iiiii		[0:31]														*Free an op code by shorting jump to 4 i's instead of 5, op codes 111 and 110 can be used

	Machine code for project 1:

	Load M[0] into $1
	Load M[1] into $2
	As long as $1 > $2: $1 = $1 - $2
	When it isnt $1 = $1 * 6
	Then repeat $1 = $1 - $2