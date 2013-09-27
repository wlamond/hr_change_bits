'''
    Created on Sep 25, 2013

    This program solves the Hacker Rank Changing Bits challenge. 
    Please see the README for more details.

    Copyright (C) 2013 Will Lamond

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses.

'''

import fileinput, sys


class Runtime:
    
    """ The Runtime class maintains the state of the three binary strings
    in the problem. It exploits the arbitrary precision integer type of 
    Python to make this problem really straight-forward. """

    def __init__(self, a_val, b_val, c_val):
        self.a_val = a_val
        self.b_val = b_val
        self.c_val = c_val
        self.getReady = False # to avoid recomputing c_val
        
    def get(self, i):
        """ performs the get operation, as defined on the challenge page. """
        if(not self.getReady):
            self.c_val = self.a_val + self.b_val
        self.getReady = True        
        return (self.c_val >> i) & 1 
        
    def set_a(self, i, val):
        """ performs the set operation on the a_val, as defined on the 
        challenge page."""
        self.getReady = False
        if(val == 1):
            self.a_val |= (1 << i)
        else:
            self.a_val &= ~(1 << i)
        
    def set_b(self, i, val):
        """ This performs the set operation on the b_val, as definied 
        on the challenge page."""
        self.getReady = False
        if(val == 1):
            self.b_val |= (1 << i)
        else:
            self.b_val &= ~(1 << i)
    

def get(cmd, rt):
    """ a wrapper function for calling the Runtime's get method. """
    bit_val = rt.get(int(cmd[1]))
    sys.stdout.write(str(bit_val))
    

    
def set(cmd, rt):
    """ a wrapper function for calling the Runtime's set_(a|b) method. """
    pos = int(cmd[1])
    val = int(cmd[2])
    if(cmd[0] == "set_a"):
        rt.set_a(pos, val)
    else:
        rt.set_b(pos, val)
    


def process_command(cmd, rt):
    """ The wrapper for deciding whether a command is a get or a set, which 
    then calls the respective wrapper function. """
    command = cmd.split(' ')
    operation = command[0]
    opcode = operation.split("_")
    
    if opcode[0] == "set":
        set(command, rt)
    elif opcode[0] == "get":
        get(command, rt)



def main():
    """ This reads the first line (doesn't really need to use it, just needs 
    to get it out of the way), then gets the pair of binary strings, initializes
    them as ints, and then processes the commands one by one. The state of the 
    two ints is maintained by the Runtime class. """

    firstline = raw_input()    
    a_val = int(raw_input(), base=2)
    b_val = int(raw_input(), base=2)
    c_val = 0
    rt = Runtime(a_val, b_val, c_val)
    for line in fileinput.input():
        process_command(line.rstrip('\n'), rt)





if __name__ == "__main__":
    main()

