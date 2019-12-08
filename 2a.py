total = 0
A=list(map(int,open("input.txt").read().split(',')))
#print(A)

i=0
while A[i]!=99:
    if A[i]==1:
        #print("adding")
        A[A[i+3]]=A[A[i+1]]+A[A[i+2]]
    else:
        #print("multiplying")
        A[A[i+3]]=A[A[i+1]]*A[A[i+2]]
    #print(A[i+1],A[i+2],A[i+3])
    #print(i,len(A))
    i+=4

print(A[0])