A=open("input.txt").read()
L=25*6
N=len(A)//L
#print(N,len(A))
buckets=[[0,0,0] for _ in range(N)]

for i in range(len(A)):
    buckets[i//L][int(A[i])]+=1

m=min(buckets,key=lambda x: x[0])
print(m)
print(m[1]*m[2])