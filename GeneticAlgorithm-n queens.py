import random
n=int(input('Enter no. of queens:'))
b=[]
for p in range(n):
    c=[]
    for l in range(n):
        c.append(0)
    b.append(c)
print('Arranging ',n,' queens without conflicts is possible as follows')
def fitness_score(pos):
    fs=0
    for i in range(n):
        c=pos[i]
        for j in range(n):
            if i==j:
                continue
            if pos[j]==c:
                continue
            if j+pos[j]==i+c:
                continue
            if j-pos[j]==i-c:
                continue
            fs+=1
    return fs/2
def mutation(l):
    t=l+[1]
    t=t[:-1]
    mv=random.randrange(1,n)
    if t==l:
        l[n-mv],l[n-mv-1]=l[n-mv-1],l[n-mv]
    
    return l
def rand():
    l=[]
    while len(l)<n:
        k=random.randrange(1,n+1)
        if k not in l:
            l.append(k)
    return l
def nextGen(p1,p2,mv):
    i=int(mv)
    c1=p1[:i]+p2[i:]
    c2=p2[:i]+p1[i:]
    return (c1,c2)
def print_board(board):
    print('Final board ',board)
    for i in range(1,n+1):
        for ele in board:
            if ele==n-i+1:
                print('Q'+str(board.index(ele)+1),end=' ')
            else:
                print('--',end=' ')
        print()
    
a=rand()
b=rand()
c=rand()
d=rand()
l=[a,b,c,d]
g=0
while True:
    g+=1
    fscore=[]
    mv=n/2
    for i in range(len(l)):
        f=fitness_score(l[i])
        fscore.append(f)
        if f==n-1-i:
            mv=f
    
    p=fscore.index(max(fscore))
    par1=l.pop(p)
    fscore.pop(p)
    p=fscore.index(max(fscore))
    par2=l.pop(p)
    fscore.pop(p)

    g1,g2=nextGen(par1,par2,mv)
    
    child1=mutation(g1)

    child2=mutation(g2)
    
    ffv=(n-1)*n/2
    
    if fitness_score(child1)==ffv:
        print_board(child1)
        print('Reached after ',g,'generations ')
        break
    if fitness_score(child2)==ffv:
        print_board(child1)
        print('Reached after ',g,'generations ')
        break
    l=[child1,child2]
    











