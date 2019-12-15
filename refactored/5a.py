#BlueyNeilo 2019
#AoC Q.5a
#Refactored

from intcode import Intcode, parse_file

ic = Intcode(parse_file("input.txt"))

ic.sim_input([1])   #Comment out for manual input
ic.execute()
