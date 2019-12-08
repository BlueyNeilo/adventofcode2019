def getfuel(x):
    newx=x//3 - 2
    if newx<=0:
        return 0
    return newx + getfuel(newx)

total = 0
for line in open("input.txt"):
    x = int(line)
    total+=getfuel(x)
print(total)