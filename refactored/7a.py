#BlueyNeilo 2019
#AoC Q.7a
#Refactored

from intcode import Intcode, parse_file
from itertools import permutations

AMPS = 5

ic = Intcode(parse_file("input.txt"))
perms = list(permutations(range(AMPS)))     #Permutations of [0..AMPS-1]
max_out = 0                                 #Maximum output signal

for p in perms:
    last_out = 0
    for i in range(AMPS):
        ic.reset()
        ic.sim_input([p[i], last_out])
        last_out = ic.execute_yield().pop()

    max_out = max(max_out, last_out)

print(max_out)
