total = 0
A=list(map(int,open("input.txt").read().split(',')))
#print(A)

#mode 0 = position, mode 1 = immediate
def imp(A,loc,mode,rel):
    if mode==1:
        return loc
    elif mode==2:
        return A[loc]+rel
    return A[loc]

def f(A):
    i=0
    rel=0
    op=str(A[i])
    op='0'*(5-len(op))+op
    
    m1=int(op[2])
    m2=int(op[1])
    m3=int(op[0])
    op=int(op[3:])

    addr1=imp(A,i+1,m1,rel)
    addr2=imp(A,i+2,m2,rel)
    addr3=imp(A,i+3,m3,rel)
    while op!=99:
        if op==1:
            #print("adding")
            A[addr3] = A[addr1]+A[addr2]
            i+=4
        elif op==2:
            #print("multiplying")
            A[addr3] = A[addr1]*A[addr2]
            i+=4
        elif op==3:
            A[addr1] = int(input())
            i+=2
        elif op==4:
            print(A[addr1])
            i+=2
        elif op==5:
            if A[addr1]:
                i=A[addr2]
            else:
                i+=3
        elif op==6:
            if not A[addr1]:
                i=A[addr2]
            else:
                i+=3
        elif op==7:
            A[addr3] = A[addr1]<A[addr2]
            i+=4
        elif op == 8:
            A[addr3] = A[addr1]==A[addr2]
            i+=4
        elif op == 9:
            rel+=A[addr1]
            i+=2
        
        op=str(A[i])
        op='0'*(5-len(op))+op
        m1=int(op[2])
        m2=int(op[1])
        m3=int(op[0])
        op=int(op[3:])

        addr1=imp(A,i+1,m1,rel)
        addr2=imp(A,i+2,m2,rel)
        addr3=imp(A,i+3,m3,rel)
    return A

f(A+[0]*10000)