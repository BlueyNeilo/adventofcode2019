import os
total = 0
A=list(map(int,open("input.txt").read().split(',')))+[0]*1000
#print(A)

#mode 0 = position, mode 1 = immediate
def imp(A,loc,mode,rel):
    if mode==1:
        return loc
    elif mode==2:
        return A[loc]+rel
    return A[loc]

def f(A,i,inp,rel):
    out_buf=[]
    outi=0
    op=str(A[i])
    op='0'*(5-len(op))+op
    
    m1=int(op[2])
    m2=int(op[1])
    m3=int(op[0])
    op=int(op[3:])

    addr1=imp(A,i+1,m1,rel)
    addr2=imp(A,i+2,m2,rel)
    addr3=imp(A,i+3,m3,rel)
    while op!=99:
        if op==1:
            #print("adding")
            A[addr3] = A[addr1]+A[addr2]
            i+=4
        elif op==2:
            #print("multiplying")
            A[addr3] = A[addr1]*A[addr2]
            i+=4
        elif op==3:
            A[addr1]=inp
            i+=2
        elif op==4:
            #print(A[addr1])
            out_buf.append(A[addr1])
            i+=2
            if len(out_buf)>=2:
                #print(out_buf,i)
                return A, i, out_buf, rel
            
        elif op==5:
            if A[addr1]:
                i=A[addr2]
            else:
                i+=3
        elif op==6:
            if not A[addr1]:
                i=A[addr2]
            else:
                i+=3
        elif op==7:
            A[addr3] = A[addr1]<A[addr2]
            i+=4
        elif op == 8:
            A[addr3] = A[addr1]==A[addr2]
            i+=4
        elif op == 9:
            rel+=A[addr1]
            i+=2
        
        op=str(A[i])
        op='0'*(5-len(op))+op
        m1=int(op[2])
        m2=int(op[1])
        m3=int(op[0])
        op=int(op[3:])

        addr1=imp(A,i+1,m1,rel)
        addr2=imp(A,i+2,m2,rel)
        addr3=imp(A,i+3,m3,rel)
        #print(i)
    return A, -1, -1, -1
panels=dict()

dir=[(0,-1),(1,0),(0,1),(-1,0)]
d=['^','>','v','<']
c=['.','#']
turn=[-1,1]

current_col=0
current_dir=0
current_loc=(0,0)
i=0
rel=0
trig=False
local=50
def drawpanels():
    os.system('cls')
    minx=min(panels.keys(),key=lambda x: x[0])[0]
    miny=min(panels.keys(),key=lambda x: x[1])[1]
    maxx=max(panels.keys(),key=lambda x: x[0])[0]
    maxy=max(panels.keys(),key=lambda x: x[1])[1]
    lines=""
    for j in range(current_loc[1]-local,current_loc[1]+local+1): #range(miny,maxy+1):
        for i in range(current_loc[0]-local,current_loc[0]+local+1): #range(minx,maxx+1):
            if (i,j)==current_loc:
                lines+=d[current_dir]
            else:
                if (i,j) in panels:
                    lines+=c[panels[i,j]]
                else:
                    lines+=c[0]
        lines+="\n"
    print(lines)

while True:
    A,i,col_turn,rel=f(A,i,current_col,rel)
    if i==-1:
        break

    panels[current_loc]=col_turn[0]
    current_dir=(current_dir+turn[col_turn[1]])%4
    current_loc=(current_loc[0]+dir[current_dir][0],current_loc[1]+dir[current_dir][1])
    if current_loc in panels:
        current_col=panels[current_loc]
    else:
        current_col=0
    #drawpanels()
    if len(panels)%100==0:
        if not trig:
            drawpanels()
            #print(col_turn,current_dir)
            #print(current_loc)
            print(len(panels))
            trig=True
    else:
        trig=False
    
print(len(panels))