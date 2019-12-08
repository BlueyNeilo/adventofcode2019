x=273025
y=767253

total=0
for i in range(x,y):
    c = str(i)
    good=True
    count=[0]*10
    for d in c:
        count[int(d)]+=1
    for j in range(1,6):
        if (c[j-1]>c[j]):
            good=False
            break
    same = len(list(filter(lambda x: x==2, count)))>0

    if good and same:
        total+=1
        
print(total)