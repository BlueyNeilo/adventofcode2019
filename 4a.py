x=273025
y=767253

total=0
for i in range(x,y):
    c = str(i)
    good=True
    same=False
    for j in range(1,6):
        if (c[j-1]>c[j]):
            good=False
            break
        if c[j-1]==c[j]:
            same=True

    if good and same:
        total+=1
        #print(c)
print(total)