#BlueyNeilo 2019
#AoC Q.2b
#Refactored

from intcode import Intcode, parse_file

target_output=19690720

ic = Intcode(parse_file("input.txt"))

exit=False
for i in range(100):
    for j in range(100):
        ic.reset()
        ic.program[1]=i
        ic.program[2]=j
        ic.execute()
        output=ic.program[0]
        
        if output==target_output:
            print(100*i+j)
            exit=True 
            break
    if exit:
        break           