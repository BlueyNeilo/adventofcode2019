lines = open("input.txt").readlines()
lines = list(map(lambda line: line.split(","),lines))

points=[None]*2
for i in range(2):
    points[i]=[[0,0,False]]
    for j in range(len(lines[i])):
        pcode=lines[i][j][0]
        pnum=int(lines[i][j][1:])
        if pcode=="U":
            points[i].append([points[i][-1][0],points[i][-1][1]+pnum,True])
        elif pcode=="D":
            points[i].append([points[i][-1][0],points[i][-1][1]-pnum,True])
        elif pcode=="R":
            points[i].append([points[i][-1][0]+pnum,points[i][-1][1],False])
        else:
            points[i].append([points[i][-1][0]-pnum,points[i][-1][1],False])

def within_r(mi,ma,x):
    return (mi<x and ma>x) or (mi>x and ma<x)

intersections=[]
for i in range(1,len(points[0])):
    for j in range(1,len(points[1])):
        #Horizontal meets Vertical
        if points[0][i][2]!=points[1][j][2]:
            v=[points[0][i],points[0][i-1]]
            h=[points[1][j],points[1][j-1]]

            if points[1][j][2]:
                v,h=h,v
            x=v[0][0]
            y=h[0][1]
            
            if within_r(v[0][1],v[1][1],y) and within_r(h[0][0],h[1][0],x):
                intersections.append([x,y])

#print(intersections)
dists=list(map(lambda p: abs(p[0])+abs(p[1]),intersections))
print(min(dists))
