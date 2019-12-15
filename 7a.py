total = 0
A=list(map(int,open("input.txt").read().split(',')))
#print(A)

def imp(A,loc,mode):
    if mode:
        return loc
    return A[loc]

def f(A,inputs):
    inpi=0
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
            A[imp(A,i+3,m3)]=A[imp(A,i+1,m1)]+A[imp(A,i+2,m2)]
            i+=4
        elif op==2:
            #print("multiplying")
            A[imp(A,i+3,m3)]=A[imp(A,i+1,m1)]*A[imp(A,i+2,m2)]
            i+=4
        elif op==3:
            A[imp(A,i+1,m1)]=int(inputs[inpi])
            inpi+=1
            i+=2
        elif op==4:
            return A[imp(A,i+1,m1)]
            i+=2
        elif op==5:
            if A[imp(A,i+1,m1)]:
                i=A[imp(A,i+2,m2)]
            else:
                i+=3
        elif op==6:
            if not A[imp(A,i+1,m1)]:
                i=A[imp(A,i+2,m2)]
            else:
                i+=3
        elif op==7:
            A[imp(A,i+3,m3)]=int(A[imp(A,i+1,m1)]<A[imp(A,i+2,m2)])
            i+=4
        elif op == 8:
            A[imp(A, i+3, m3)] = int( A[imp(A, i+1, m1)] == A[imp(A, i+2, m2)] )
            i+=4
        op=str(A[i])
        op='0'*(5-len(op))+op
        m1=int(op[2])
        m2=int(op[1])
        m3=int(op[0])
        op=int(op[3:])

    return A
last_out=0

import itertools
L=list(itertools.permutations([0,1,2,3,4]))
maxL=0
for l in L:
    for i in range(5):
        last_out=f(A,[l[i],last_out])
        #print(last_out)
    if last_out>maxL:
        maxL=last_out

    last_out=0
print(maxL)