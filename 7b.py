total = 0
A=list(map(int,open("input.txt").read().split(',')))
#print(A)

def imp(A,loc,mode):
    if mode:
        return loc
    return A[loc]

def f(A,i,inputs):
    inpi=0
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
            return A, i+2, A[imp(A,i+1,m1)]
            #i+=2
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
    return A, -1, -1

import itertools

L=list(itertools.permutations([5,6,7,8,9]))
maxL=0

for l in L:
    last_out=0
    last_iter=0
    As=[A[:] for _ in range(5)]
    Is=[0]*5

    for i in range(5):
        As[i],Is[i],last_out=f(As[i],Is[i],[l[i],last_out])

    while last_out>last_iter:
        last_iter=last_out
        for i in range(5):
            As[i],Is[i],last_out=f(As[i],Is[i],[last_out])
            if last_out==-1:
                break

    if last_iter>maxL:
        maxL=last_iter

print(maxL)