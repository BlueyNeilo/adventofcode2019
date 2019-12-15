#BlueyNeilo 2019
#AoC Q.5b
#Refactored

from intcode import Intcode, parse_file

ic = Intcode(parse_file("input.txt"))

ic.sim_input([5])   #Comment out for manual input
ic.execute()
