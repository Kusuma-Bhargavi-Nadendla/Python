def child_node(in_sta,ac):
    child=[]
    for i in range(len(in_sta)):
        if in_sta[i]==0:
            bl_loc=i
            break
    t=bl_loc
    if(ac==1):
        if bl_loc==0 or bl_loc==3 or bl_loc==6:
            f=0
        else:
            f=1
            bl_loc-=1
    elif(ac==2):
        if bl_loc==2 or bl_loc==5 or bl_loc==8:
            f=0
        else:
            f=1
            bl_loc+=1
    elif(ac==3):
        if bl_loc==0 or bl_loc==1 or bl_loc==2:
            f=0
        else:
            f=1
            bl_loc-=3
    elif(ac==4):
        if bl_loc==6 or bl_loc==7 or bl_loc==8:
            f=0
        else:
            f=1
            bl_loc+=3
    if f==1:
        child=[0]+in_sta
        child=child[1:]
        child[bl_loc],child[t]=child[t],child[bl_loc]
        return child
    else:
        return [0]*len(in_sta)
  

def bfs(problem):
    node=problem['initial']
    path_cost=0
    if node==problem['goal']:
        return node 
    frontier=[node]
    explored=[]
    while(node!=problem['goal']):
        if len(frontier)==0:
            return 'failure'
        node=frontier[0]
        frontier=frontier[1:]
        explored.append(node)
        for ac in range(len(problem['actions'])):
            child=child_node(node,ac+1)
            if child==node:
              continue 
            if (child not in frontier) and (child not in explored):
                if child==problem['goal']:
                    return child 
                frontier.append(child)
                print(child)
        
        
print('Enter initial state:')
in_sta=[int(x) for x in input().split()]
print('Enter goal state of puzzle')
goal_sta=[int(x) for x in input().split()]
actions={1:'left',2:'right',3:'up',4:'down'}
problem={'initial':in_sta,'goal':goal_sta,'actions':[1,2,3,4]}

res=bfs(problem)
print('Goal state reached:',res)

