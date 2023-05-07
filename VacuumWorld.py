loc=input('Enter location of vacuum(A/B):')
a_sta=input('Enter status of A room:')
b_sta=input('Enter status of B room:')
print('Initial state:(A,',a_sta,'),(B,',b_sta,')')
print('Goal state:(A,0),(B,0)')
print('Actions possible are')
print('1.Clean the room\n2.Move to A\n3.Move to B')
while(a_sta!=0 or b_sta!=0):
  ac=int(input('Choose action to be performed:'))
  if(ac==1):
    if(loc=='A' and a_sta!=0):
      a_sta=0
      print('Room A cleaned')
    elif(loc=='B' and b_sta!=0):
      b_sta=0
      print('Room B cleaned')
    else:
      print('Room is clean')
  elif(ac==2):
    if(loc=='B'):
      loc='A'
    else:
      print('Vacuum is in room A')
  elif(ac==3):
    if(loc=='A'):
      loc='B'
    else:
      print('Vacuum is in room B')
  else:
    print('Invalid action command')
  print('Current state:(A,',a_sta,'),(B,',b_sta,')')
  print('Location of Vacuum:',loc)
print('Goal state reached')
