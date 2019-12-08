lines = open("input.txt").readlines()
lines = list(map(lambda line: line.split(","),lines))

points=[None]*2
for i in range(2):
    points[i]=[[0,0,False,0]]
    for j in range(len(lines[i])):
        pcode=lines[i][j][0]
        pnum=int(lines[i][j][1:])
        if pcode=="U":
            points[i].append([points[i][-1][0],points[i][-1][1]+pnum,True,points[i][-1][3]+pnum])
        elif pcode=="D":
            points[i].append([points[i][-1][0],points[i][-1][1]-pnum,True,points[i][-1][3]+pnum])
        elif pcode=="R":
            points[i].append([points[i][-1][0]+pnum,points[i][-1][1],False,points[i][-1][3]+pnum])
        else:
            points[i].append([points[i][-1][0]-pnum,points[i][-1][1],False,points[i][-1][3]+pnum])

def within_r(mi,ma,x):
    return (mi<x and ma>x) or (mi>x and ma<x)

intersections=[]
for i in range(1,len(points[0])):
    for j in range(1,len(points[1])):
        #Horizontal meets Vertical
        if points[0][i][2]!=points[1][j][2]:
            v=[points[0][i-1],points[0][i]]
            h=[points[1][j-1],points[1][j]]

            if points[1][j][2]:
                v,h=h,v
            x=v[0][0]
            y=h[0][1]

            if within_r(v[0][1],v[1][1],y) and within_r(h[0][0],h[1][0],x):
                #print(x,y,h[0],abs(h[0][0]-x),v[0],abs(v[0][1]-y))
                intersections.append(h[0][3]+abs(h[0][0]-x)+v[0][3]+abs(v[0][1]-y))

#print(intersections)
print(min(intersections))