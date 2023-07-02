'''Choose location of gold(1-16):6
Choose location of monster(1-16):5
Choose location of first pit(1-16):3
Choose location of second pit(1-16) or -1 to avoid:15

[['SNEEZE'], ['BREEZE'], ['PIT'], ['BREEZE']]
[['WUMP'], ['GOLD', 'SNEEZE'], ['BREEZE'], '']
[['SNEEZE'], '', ['BREEZE'], '']
['AGENT', ['BREEZE'], ['PIT'], ['BREEZE']]
Best path: 3,0-->3,1-->2,1-->1,1-->With score  987
'''


board=[['','','',''],['','','',''],['','','',''],['','','','']]
visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
is_pit=[]
is_wump=[]

#print the board
def print_board():
    print()
    for i in board:
        print(i)
    print()
print_board()


def set(x,y,s):
    if x<0 or y<0 or x>=4 or y>=4:
        return
    if board[x][y]=='':
        board[x][y]=[s]
    else:
        board[x][y]=board[x][y]+[s]

        
def set_position(loc,dan,state):
    x,y=divmod(loc,4)
    if y==0:
        x=x-1
        y=4
    set(x,y-1,dan)
    if dan=='GOLD':
        return
    set(x-1,y-1,state)
    set(x+1,y-1,state)
    set(x,y-2,state)
    set(x,y,state)

#find possible moves
def generate_moves(x,y):
    l=[]
    if x-1>=0 and x-1<=3 and y>=0 and y<=3:
        l.append((x-1,y))
    if x+1>=0 and  x+1<=3 and y>=0 and y<=3:
        l.append((x+1,y))
    if x>=0 and y-1<=3 and x<=3 and y-1>=0:
        l.append((x,y-1))
    if x>=0 and y+1<=3 and x<=3 and y+1>=0:
        l.append((x,y+1))
    return l


#move the agent
def make_move(ax,ay,x,y):
    
    if isinstance(board[ax][ay],str):
        board[ax][ay]=''
    else:
        board[ax][ay]=board[ax][ay][1:]
    if isinstance(board[x][y],str):
        board[x][y]=['AGENT']+[board[x][y]]
    else:
        board[x][y]=['AGENT']+board[x][y]

#move back the agent
def undo_move(a,b,p,q):
    make_move(a,b,p,q)

#evaluate the state   
def evaluate(x,y):
    if 'PIT' in board[x][y] or 'WUMP' in board[x][y]:
        return -1000
    if 'GOLD' in board[x][y]:
        return 1000
    s=1
    if board[x][y] in is_pit or board[x][y] in is_wump:
        s+=(-10)
    if 'SNEEZE' in board[x][y]:
        s+=(-25)
    if 'BREEZE' in board[x][y]:
        s+=(-15)
    return s

#check adjacent states
def resolve(x,y):
    if 'SNEEZE' in board[x][y]:
        for a,b in generate_moves(x,y):
            is_wump.append((a,b))
    if 'BREEZE' in board[x][y]:
        for a,b in generate_moves(x,y):
            is_pit.append((a,b))
    if 'SNEEZE' not in board[x][y]:
        for a,b in generate_moves(x,y):
            if (a,b) in is_wump:
                is_wump.remove((a,b))
    if 'BREEZE' not in board[x][y]:
        for a,b in generate_moves(x,y):
            if (a,b) in is_pit:
                is_pit.remove((a,b))

#choose locations
def initialise_game():
    gold_loc=int(input("Choose location of gold(1-16):"))
    set_position(gold_loc,'GOLD','SHINE')
    
    wump_loc=int(input("Choose location of monster(1-16):"))
    set_position(wump_loc,'WUMP','SNEEZE')
    
    pit_loc1=int(input("Choose location of first pit(1-16):"))
    set_position(pit_loc1,'PIT','BREEZE')
    
    pit_loc2=int(input("Choose location of second pit(1-16) or -1 to avoid:"))
    if pit_loc2!=-1:
        set_position(pit_loc2,'PIT','BREEZE')
        
    board[3][0]='AGENT'
    visited[3][0]=1
    
#start finding the path
def start_game():
    initialise_game()
    cax,cay=3,0
    print_board()
    final_score=0
    path=[(cax,cay)]
    
    while True:
        if 'GOLD' in board[cax][cay]:
            break
        best=-1000
        for movex,movey in generate_moves(cax,cay):
            
            if visited[movex][movey]==1:
                continue
            resolve(movex,movey)
            score=evaluate(movex,movey)
            if score>best:
                best=score
                best_move=movex,movey

        
        if best_move==(cax,cay) :
                undo_move(cax,cay,path[-2][0],path[-2][1])
                cax,cay=path[-2][0],path[-2][1]
                path=path[:-2]
                continue
        if best!=-1000:
            final_score+=best
            
        path.append(best_move)
        make_move(cax,cay,best_move[0],best_move[1])
        cax,cay=best_move[0],best_move[1]
        visited[cax][cay]=1
        print('Move:',cax,cay,' score:',final_score)
        print_board()
        
    print('Best path:',end=' ')
    for x,y in path:
        print(x,y,end='-->',sep=',')
    print('With score ',final_score)

start_game()
