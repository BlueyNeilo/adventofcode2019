#BlueyNeilo 2019
#AoC Q.2a
#Refactored

from intcode import Intcode, parse_file

ic = Intcode(parse_file("input.txt"))
ic.execute()

print(ic.program[0])