	# ECE366Group7
	ISA Functions:

	lw        00001 x y	Either loads into $1 or $2 from the address at $0 or $1
	sw        001 x iii  	Stores $1 or $2 into memory at M[0:7]
	init      011 x iii	Initializes $1 to be an unsigned imm [-4:3]		reg [1:4]
	shift 	  100 xx ii    	Shifts $1 by a signed imm [-2:1]
	bneR1     0001 x ii    	Branches if $0 or $2 is not equal to $1 forward by imm [1:4]
	sub	  010 xx yy 	$xx = $xx - $yy		[1:4]
	add	  101 xx yy	$xx = $xx + $yy		[1:4]
	lsbXor	  0000001     	Performs an andi operation into $1 of $2 and $3
	j	  11  iiiii	[0:31]														incr	  000001 x	Increments eitehr $1 or $2 by 1
	


	Machine code for project 1:

	Load M[0] into $1
	Load M[1] into $2
	As long as $1 > $2: $1 = $1 - $2
	When it isnt $1 = $1 * 6
	Then repeat $1 = $1 - $2
