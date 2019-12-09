E=list(map(lambda line: line.strip().split(')'),open("input.txt").readlines()))
#print(E)
mapping=dict()
bucket=dict()
bucket["COM"]=0
for e in E:
    mapping[e[0]]=[]
    bucket[e[1]]=0
for e in E:
    mapping[e[0]].append(e[1])

def dive(current,depth=0):
    if current in mapping.keys():
        for c in mapping[current]:
            bucket[c]=bucket[current]+1
            dive(c,depth+1)

dive("COM")
print(sum(bucket.values()))
#print(mapping)