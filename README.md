My submission for the Hacker Rank Changing Bits competition.

Please see https://www.hackerrank.com/challenges/changing-bits for more details.

The program works by exploiting Python's arbitrary precision integer type. Because of
this arbitrary precision, it can grow its bit strings to any length. An integer of this 
type can be instantiated from a binary string by using the int(binstr, base) function. 
This function, as far as I can tell, always returns a positive integer. This makes sense
since given the integer type's arbitrary precision, it would be hard to deduce where the 
negative bit is in a two's compliement representation. 


