A=open("input.txt").read()
W=25
L=6
N=W*L
final = [["2"]*W for _ in range(L)]

mapping={"1":"0","0":"_"}

for i in range(len(A)):
    r=(i%N)//W
    c=(i%N)%W
    if final[r][c]=="2" and A[i]!="2":
        final[r][c]=mapping[A[i]]

for l in final:
    print("".join(l))