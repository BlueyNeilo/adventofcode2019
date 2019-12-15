#BlueyNeilo 2019
#AoC Q.2a
#Refactored Intcode (backwards-compatible for all AoC 2019)

def parse_file(file):
    return list(map(int,open(file).read().split(',')))

class Intcode:
    #(parameters, function that takes in intcode object)
    opcodes={
        1:  (3, lambda ic: ic.setarg(3, ic.arg(1) + ic.arg(2))),
        2:  (3, lambda ic: ic.setarg(3, ic.arg(1) * ic.arg(2))),
        3:  (1, lambda ic: ic.setarg(1, ic.input())),
        4:  (1, lambda ic: ic.output(ic.arg(1))),
        5:  (2, lambda ic: ic.setpc(ic.arg(2)-3) if ic.arg(1) else None),
        6:  (2, lambda ic: ic.setpc(ic.arg(2)-3) if not ic.arg(1) else None),
        7:  (3, lambda ic: ic.setarg(3, ic.arg(1) < ic.arg(2))),
        8:  (3, lambda ic: ic.setarg(3, ic.arg(1) == ic.arg(2))),
        9:  (1, lambda ic: ic.updateoffset(ic.arg(1))),
        99: (0, lambda ic: ic.halt())
    }
    
    #Helper functions for lambda
    def setpc(self,pc):             self.pc=pc
    def updateoffset(self,off):     self.rel_offset+=off
    def halt(self):                 self.halted=True

    #Addressing with different modes
    addr_modes={
        0: (lambda ic, addr: ic.program[addr]),
        1: (lambda _,  addr: addr),
        2: (lambda ic, addr: ic.program[addr] + ic.rel_offset)
    }

    def __init__(self,
                program=[99],
                pc=0,
                rel_offset=0,
                halted=False):
        self.original=program       #Original source code to reset to
        self.program=None           #Expects array of ints for program
        self.reset(pc,rel_offset,halted)

    def reset(self,pc=0,rel_offset=0,halted=False):
        self.program=self.original[:]
        self.pc=pc                  #Program counter (index of program)
        self.rel_offset=rel_offset  #Relative offset for addressing (mode 2)
        self.halted=halted          #Halted or not
        self.input_buf=[]           #Buffer for passing in simulated input
        self.output_buf=[]          #Buffer for simulated output
        self.sim_outputs=0          #How many times left to simulate to output_buf

    def address(self,addr,mode):
        if mode in Intcode.addr_modes:
            final_addr=Intcode.addr_modes[mode](self,addr)
            
            #Extend the tape if needed
            if final_addr>=len(self.program):
                self.program+=[0]*(final_addr-len(self.program)+2)
            return final_addr
        else:
            raise "Bad mode" + str(self.len)

    def getmode(self,a):
        modes=self.program[self.pc]//100
        return (modes%(10**(a)))//(10**(a-1))

    def arg(self,a):
        return self.program[self.address(self.pc+a,self.getmode(a))]

    def setarg(self,a,v):
        self.program[self.address(self.pc+a,self.getmode(a))]=v

    def input(self):
        if self.input_buf:
            return self.input_buf.pop()
        return int(input())

    #FIFO, reading from end of list
    def sim_input(self,buf):
        self.input_buf=buf[::-1]+self.input_buf

    def output(self,v):
        if self.sim_outputs>0:
            self.output_buf.append(v)
            self.sim_outputs-=1
        else:
            print(v)
    
    def execute(self):
        while not self.halted:
            self.tick()
    
    #Yield back control after a number of outputs
    def execute_yield(self,outputs=1):
        self.sim_outputs=outputs
        self.output_buf=[]
        while (not self.halted) and (self.sim_outputs>0):
            self.tick()
        return self.output_buf

    def tick(self):
        if not self.halted:
            op=self.program[self.pc]%100
            Intcode.opcodes[op][1](self)
            self.pc += Intcode.opcodes[op][0] + 1
