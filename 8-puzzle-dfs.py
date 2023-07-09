def child_node(in_sta,ac):
    #actions={1:'left',2:'right',3:'up',4:'down'}
    child=[]
    bl_loc=in_sta.index(0)
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
        child=[]+in_sta
        child[bl_loc],child[t]=child[t],child[bl_loc]
        return child
    else:
        return [0]
  
frontier=[]
explored=[]
def dfs(problem):
    node=problem['initial']
    
    if node==problem['goal']:
        return node 
    frontier.append(node)
    while(node!=problem['goal']):
        
        if len(frontier)==0:
            return 'failure'
        
        node=frontier.pop()
        if node in explored:
            return 'failure'
        explored.append(node)
        print(node)
        for ac in problem['actions']:
            child=child_node(node,ac)
            if child==[0] or child==node:
              continue 
            if (child not in frontier) and (child not in explored):
                if child==problem['goal']:
                    return child 
                frontier.append(node)
                problem={'initial':child,'goal':goal_sta,'actions':[1,2,3,4]}
                res=dfs(problem)
                if res!='failure':
                    return res 
                else:
                    continue

#in_sta=[2, 8, 3, 1, 6, 4, 7, 0, 5]
#goal_sta=[1,2,3,4,8,0,7,5,6]
#There is no guarantee of obtaining a  solution using DFS 
print('Enter initial state:')
in_sta=[int(x) for x in input().split()]
print('Enter goal state of puzzle')
goal_sta=[int(x) for x in input().split()]
problem={'initial':in_sta,'goal':goal_sta,'actions':[1,2,3,4]}
res=dfs(problem)
print('Goal state reached:',res)

