E=list(map(lambda line: line.strip().split(')'),open("input.txt").readlines()))
#print(E)
mapping=dict()
bucket=dict()
for e in E:
    mapping[e[0]]=[]
for e in E:
    mapping[e[0]].append(e[1])

def find(current,targ):
    if current in mapping.keys():
        for c in mapping[current]:
            if c==targ:
                return [targ]
            dc=find(c,targ)
            if dc!=-1:
                return [c]+dc
    return -1

x=find("COM","YOU")
y=find("COM","SAN")
common=0
for i in range(len(x)):
    if x[i]!=y[i]:
        common=i-1
        break
x=x[common:]
y=y[common:]
#print(x)
#print(y)
print(len(x)+len(y)-4)
#print(mapping)