n=int(input('Enter no. of queens:'))
b=[]
for p in range(n):
    c=[]
    for l in range(n):
        c.append(0)
    b.append(c)
print('Arranging ',n,' queens without conflicts is possible as follows')
def conflicts(i,j):
    c=0
    for k in range(n):
        if b[i][k]!=0:
            c+=1
        if b[k][j]!=0:
            c+=1
        if (i+k)<n and (j+k)<n and b[i+k][j+k]!=0:
            c+=1
        if (i-k)<n and (i-k)>=0 and (j-k)<n  and (j-k)>=0 and b[i-k][j-k]!=0:
            c+=1
        if (i-k)<n and (i-k)>=0 and (j+k)<n and (j+k)>=0 and b[i-k][j+k]!=0:
            c+=1
        if (i+k)<n and (i+k)>=0 and (j-k)<n and (j-k)>=0 and b[i+k][j-k]!=0:
            c+=1
    return c
i=j=0
stack=[]
k=1
while k<=n:
    while i<n:
        f=0
        while j<n:
            if conflicts(i,j)==0:
                b[i][j]='Q'+str(k)
                #print(b)
                stack.append((i,j,k))
                f=1
                k+=1
                j=0
                break
            j+=1
        if f==0:
            (i,j,k)=stack.pop()
            b[i][j]=0
            j+=1
        else:
            i+=1
for p in range(n):
    for l in range(n):
        print(b[p][l],end='  ')
    print()
                
