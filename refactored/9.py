#BlueyNeilo 2019
#AoC Q.9
#Refactored

from intcode import Intcode, parse_file

ic = Intcode(parse_file("input.txt"))

#ic.sim_input([1])      #9a
#ic.sim_input([2])      #9b
ic.execute()