x=8
y=0
z=0
l=8
m=5
n=3
print('Initial state:(8,0,0)')
print('Goal state:(4,4,0)')
print('Rules for filling jugs')
print('1. Pour from 8-g to 5-g until 5-g full\n2. Pour from 8-g to 3-g until 3-g full\n3. Pour from 5-g to 3-g until 3-g full')
print('4. pour from 3-g to 5-g completely\n5. pour from 3-g to 8-g completely\n6. pour from 5-g to 8-g completely')
print('7. pour from 5-g to 3-g completely\n8. pour from 8-g to 5-g completely\n9. pour from 8-g to 3-g completely')
while(x!=4 or y!=4):
    r=int(input('Enter rule number:'))
    (p,q,s)=(x,y,z)
    if(r==1):
        if(x+y>=m and y<m and x>0):
            x=x-(m-y)
            y=m
    elif(r==2):
        if(x+y>=n and y>0 and z<n):
            x=x-(m-z)
            z=n
    elif(r==3):
        if(y+z>=3 and y>0 and z<3):
            y=y-(n-z)
            z=n
    elif(r==4):
        if(y+z<=5 and z>0):
            y+=z
            z=0
    elif(r==5):
        if(z>0 and x+z<=8):
            x+=z
            z=0
    elif(r==6):
        if(y>0 and x+y<=8):
            x+=y
            y=0
    elif(r==7):
        if(y+z<=3 and y>0):
            z+=y
            y=0
    elif(r==8):
        if(x+y<=5 and x>0):
            y+=x
            x=0
    elif(r==9):
        if(x+z<=3 and x>0):
            z+=x
            x=0
    else:
        print('Invalid entry for rule number')
    if( (p,q,s)==(x,y,z)):
        print('Rule is not applicable to current state.\nTry again!!!')
    else:
        print('Rule applied :(',x,',',y,',',z,')')
print('Goal state reached')   
            
    


