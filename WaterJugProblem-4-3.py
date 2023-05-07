#WATER JUG PROBLEM TO FILL 2 LITRES OF WATER USING 4 AND 3 GALLONS CAPACITY JUGS
x=0
y=0
m=4
n=3
print('Initial state:(0,0)')
print('Goal state:(2,x)')
print('Rules for filling jugs')
print('1. Fill 4 gallon jug\n2.Fill 3 gallon jug\n3.pour from 3-g jug to 4-g completely')
print('4.pour from 4-g to 3-g completely\n5.Pour to 4-g jug until it is full\n6.Pour to 3-g jug until it is full')
print('7.Empty 4-g jug\n8.Empty 3-g jug')
c=0
while(x!=2):
    r=int(input('Enter rule number:'))
    (p,q)=(x,y)
    if(r==1):
        if(x<4):
            x=m
    elif(r==2):
        if(y<3):
            y=n
    elif(r==3):
        if(y>0 and x+y<=m):
            x+=y
            y=0
    elif(r==4):
        if(x>0 and x+y<=n):
            y+=x
            x=0
    elif(r==5):
        if(y>0 and x<m and x+y>=m):
            y=y-(m-x)
            x=m
    elif(r==6):
        if(x>0 and y<n and x+y>=n):
            x=x-(n-y)
            y=n
    elif(r==7):
        if(x>0):
            x=0
    elif(r==8):
        if(y>0):
            y=0
    if( (p,q)==(x,y)):
        print('Rule is not applicable for current state \nTry again!!!')
    else:
        c+=1
        print('Rule applied :(',x,',',y,')')
print('Goal state reached in ',c,' steps')   
