print('Enter initial state of puzzle')
in_sta=[int(x) for x in input().split()]
print('Enter goal state of puzzle')
goal_sta=[int(x) for x in input().split()]
for i in range(len(in_sta)):
  if in_sta[i]==0:
    bl_loc=i
    break
while(in_sta != goal_sta):
  print('Move blank to\n1.Left\n2.Right\n3.Up\n4.Down\n')
  ac=int(input('Choose action:'))
  f=0
  t=bl_loc
  if(ac==1):
    if bl_loc==0 or bl_loc==3 or bl_loc==6:
      print('Cannot move to left')
    else:
      f=1
      bl_loc-=1
  elif(ac==2):
    if bl_loc==2 or bl_loc==5 or bl_loc==8:
      print('Cannot move to right')
    else:
      f=1
      bl_loc+=1
  elif(ac==3):
    if bl_loc==0 or bl_loc==1 or bl_loc==2:
      print('Cannot move to up')
    else:
      f=1
      bl_loc-=3
  elif(ac==4):
    if bl_loc==6 or bl_loc==7 or bl_loc==8:
      print('Cannot move to down')
    else:
      f=1
      bl_loc+=3
  if f==1:
    in_sta[bl_loc],in_sta[t]=in_sta[t],in_sta[bl_loc]
  print('Location of blank-',bl_loc)
  print('Current state:',in_sta)
print('Goal state reached')
