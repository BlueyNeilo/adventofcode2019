#BlueyNeilo 2019
#AoC Q.11
#Refactored

from intcode import Intcode, parse_file

panels = {}                             #Painted panels (tuple space)
dir = [(0,-1), (1,0), (0,1), (-1,0)]    #(UP,RIGHT,DOWN,LEFT)
turn = [-1,1]                           #offset the index for dir to rotate 90 degrees

ic = Intcode(parse_file("input.txt"))
current_col = 0     #11a - 0, 11b - 1
current_dir = 0
current_loc = (0,0)


#Drawing
from os import system

#local_render - How far in each direction to render
def draw_panels(panels,current_loc,current_dir,local_render = 50):
    d = ['^', '>', 'v', '<']    #Direction render
    c = ['.', '#']              #Paint render

    system('cls')
    lines=""
    for j in range(current_loc[1]-local_render,current_loc[1]+local_render+1): #range(miny,maxy+1):
        for i in range(current_loc[0]-local_render,current_loc[0]+local_render+1): #range(minx,maxx+1):
            if (i,j)==current_loc:
                lines+=d[current_dir]
            else:
                if (i,j) in panels:
                    lines+=c[panels[i,j]]
                else:
                    lines+=c[0]
        lines+="\n"
    print(lines)


#Main logic
while not ic.halted:
    ic.sim_input([current_col])
    unwrap = ic.execute_yield(outputs=2)
    if unwrap:
        [paint_col,new_turn] = unwrap

        panels[current_loc] = paint_col
        current_dir = (current_dir + turn[new_turn]) % 4
        current_loc = tuple([sum(x) for x in zip(current_loc, dir[current_dir])])
        
        current_col = 0
        if current_loc in panels:
            current_col = panels[current_loc]

draw_panels(panels,current_loc,current_dir)
print(len(panels))