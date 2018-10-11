	# ECE366Group7
	ISA Functions:

	lw	       00001 x  y		Either loads into $1 or $2 from the address at $1 or $3
	sw        	 001 x  iii  		Stores $1 or $2 into memory at M[0:7]
	init  	         011 xx ii		Initializes $1 or $3 to be an unsigned imm [0:3]		reg [1:4]
	shiftL	       01010 xx			$xx << 1
	shiftR	       01011 xx			$xx >> 1
	bgtR1	        0001 x  ii    	 	Branches if $2 or $3 is greater than $1 by unsigned imm [1:4]
	bltR1	        1001 x  ii		Branches if $2 or $3 is less than $1 by unsigned imm [1:4]
	sub             0100 xx y 		$xx = $xx - $y		x:[1:4] y:[1 or 3]
	add		1000 xx y		$x = $x + $yy		x:[1:2] y:[1:4]
	j		  11 iiiii		Jumps to PC = imm[0:31]
	addi		 101 xx ii		$xx = $xx + ii x:[1:4] imm [-2,1]
