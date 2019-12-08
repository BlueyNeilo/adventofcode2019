total = 0
A=list(map(int,open("input.txt").read().split(',')))
#print(A)

def f(A):
    A=A[:]
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
    return A[0]

target_output=19690720

outer_exit=False
for i in range(100):
    for j in range(100):
        A[1]=i
        A[2]=j
        output=f(A)
        #print(i,j,output)
        if output==target_output:
            print(str(i)+str(j))
            outer_exit=True 
            break
    if outer_exit:
        break