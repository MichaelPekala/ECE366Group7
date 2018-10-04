# ECE366Group7
ISA Functions:

lw        0001 x y i  Either loads into $1 or $2 from the address at $0 or $1 shifted by 0x2 or 0x4
bne       00001 ii    Branches if $2 is not equal to $3 by unsigned imm [1:4]    
shiftR1   100 iiii    Shifts $1 by a signed imm [-8:7]
end       0000000     Freezes the CPU
sw        001 x y ii  Stores $1 or $3 into memory at $0 or $2 shifted by 0x0 0x2 0x4 or 0x6
init      01 x iiii   Initializes $1 or $2 to be an unsigned imm [1:16]
sub1R2    0000001     Subtracts 1 from $2
andi      1000000     Performs an andi operation into $3 of $2 and 1
