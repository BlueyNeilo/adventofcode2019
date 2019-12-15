#BlueyNeilo 2019
#AoC Q.7b
#Refactored

from intcode import Intcode, parse_file
from itertools import permutations

AMPS = 5

program = parse_file("input.txt")
ics = [Intcode(program[:]) for _ in range(AMPS)]
perms = list(permutations(range(AMPS, 2*AMPS)))
max_out = 0                                 

for p in perms:
    last_out = 0
    last_iter = -1

    for ic in ics: ic.reset()
    
    while last_out > last_iter:
        last_iter = last_out

        for i in range(AMPS):
            if last_iter == 0:
                ics[i].sim_input([p[i]])
            
            ics[i].sim_input([last_out])
            unwrap = ics[i].execute_yield()
            
            if unwrap:
                last_out = unwrap.pop()
            else:
                break
    max_out = max(max_out, last_iter)

print(max_out)
