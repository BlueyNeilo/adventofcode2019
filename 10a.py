import math

I=open("input.txt").readlines()

Y=len(I)
X=len(I[0])-1
A=dict()

for r in range(Y):
    for c in range(X):
        A[r,c] = int(I[r][c]=="#")

#Bruteforce
for r1 in range(Y):
    for c1 in range(X):
        if A[r1,c1]:
            bad=[]
            for r2 in range(r1,Y):
                for c2 in range(X):
                    if r2>r1 or c2>c1:
                        if A[r2,c2] and ((r2,c2) not in bad):
                            A[r1,c1]+=1
                            A[r2,c2]+=1

                            #Project out
                            dr,dc=(r2-r1),(c2-c1)
                            g=math.gcd(dr,dc)
                            dr,dc=dr//g,dc//g
                            cr,cc=r2+dr,c2+dc
                            while 0<=cr and cr<Y and 0<=cc and cc<X:
                                if A[cr,cc]:
                                    bad.append((cr,cc))
                                cr,cc=cr+dr,cc+dc

for r in range(Y):
    for c in range(X):
        if A[r,c]:
            A[r,c]-=1

FA=list(A.items())
#print(A)
print(max(FA,key=lambda x:x[1]))
