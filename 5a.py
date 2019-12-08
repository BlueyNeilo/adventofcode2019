#input '1' manually

total = 0
A=list(map(int,open("input.txt").read().split(',')))
#print(A)

#mode 0 = position, mode 1 = immediate
def imp(A,loc,mode):
    if mode:
        return loc
    return A[loc]

def f(A):
    i=0
    op=str(A[i])
    op='0'*(5-len(op))+op
    
    m1=int(op[2])
    m2=int(op[1])
    m3=int(op[0])
    op=int(op[3:])
    while op!=99:
        if op==1:
            #print("adding")
            A[imp(A,i+3,m3)] = A[imp(A,i+1,m1)]+A[imp(A,i+2,m2)]
            i+=4
        elif op==2:
            #print("multiplying")
            A[imp(A,i+3,m3)] = A[imp(A,i+1,m1)]*A[imp(A,i+2,m2)]
            i+=4
        elif op==3:
            A[imp(A,i+1,m1)] = int(input())
            i+=2
        elif op==4:
            print(A[imp(A,i+1,m1)])
            i+=2

        op=str(A[i])
        op='0'*(5-len(op))+op
        m1=int(op[2])
        m2=int(op[1])
        m3=int(op[0])
        op=int(op[3:])
    return A

f(A)