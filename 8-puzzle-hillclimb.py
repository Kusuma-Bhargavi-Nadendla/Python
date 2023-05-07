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
        return [0]
  

def heuristic(node,goal):
    c=0
    for i in range(len(node)):
      if node[i]!=goal[i]:
        c+=1
    return c
def hillclimb(problem):
    node=problem['initial']
    goal=problem['goal']
    if node==goal:
        return node 
    current=heuristic(node,goal)
    frontier=[node]
    explored=[]
    while(current!=0):
        if len(frontier)==0:
            return 'failure'
        node=frontier[0]
        frontier=frontier[1:]
        explored.append(node)
        min_node=[]
        child_nodes=[]
        for ac in range(len(problem['actions'])): 
            child=child_node(node,ac+1)
            if child==node or child in explored or child in frontier or child==[0]:
              continue
            
            if child==goal:
              return child
            child_nodes.append(child)
            if heuristic(child,goal)<=current:
              min_node=child
              current=heuristic(child,goal)
        if min_node!=[]:
            frontier.append(min_node)
            print(min_node)
        else:
            m=100
            l=[]
            for c in child_nodes:
               if heuristic(c,goal)<=m:
                 m=heuristic(c,goal)
                 l=c 
            frontier.append(l)
            print(l)
            #return node
        
        
print('Enter initial state:')
in_sta=[int(x) for x in input().split()]

print('Enter goal state of puzzle')
goal_sta=[int(x) for x in input().split()]
actions={1:'left',2:'right',3:'up',4:'down'}
problem={'initial':in_sta,'goal':goal_sta,'actions':[1,2,3,4]}

res=hillclimb(problem)
if res==goal_sta:
    print('Goal state reached:',res)
else:
    print('Goal state not reached from node ',res)

