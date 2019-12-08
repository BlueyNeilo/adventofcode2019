def getfuel(x):
    return x//3 - 2

total = 0
for line in open("input.txt"):
    x = int(line)
    total+=getfuel(x)
print(total)