import copy
max_best_alpha=-1000 #-infinity
min_best_beta=1000 #infinity 
board=['','','','','','','','','']
player_max='X'
player_min='O'

def print_board(board):
    print('............')
    for ele in range(len(board)):
        print(board[ele],end=' | ')
        if(ele==2 or ele==5):
            print()
    print('\n...........')

def check_winner():
    #horizontal win
    for i in range(0,9,3):
        if (board[i]==board[i+1]==board[i+2]!=''):
            return board[i]
    #vertical win
    for i in range(3):
        if (board[i]==board[i+3]==board[i+6]!=''):
            return board[i]
    #diagonal win 
    if (board[0]==board[4]==board[8]!='') or (board[2]==board[4]==board[6]!=''):
        return board[4]
    if '' not in board:
        return 0
    return None 
def generate_moves():
    moves=[]
    for i in range(9):
        if board[i]=='':
            moves.append(i)
    return moves 
def game_over():
    res=check_winner()
    if res!=None:
        return True
    return False
def alpha_beta_prunning(alpha,beta,is_player_max):
    best_move=-1
    if game_over():
        res=check_winner()
        if res=='X':
            return None,1 
        elif res=='O':
            return None,-1
        elif res=='draw':
            return None,0
    if is_player_max:
        best=-1000
        for move in generate_moves():
            board[move]=player_max
            _, score = alpha_beta_prunning(alpha,beta,False)
            board[move] = ''
            if score > best:
                best= score
                best_move = move
            alpha=max(alpha,best)
            if alpha>=beta:
                return best_move,best 
    else:
        best=1000
        for move in generate_moves():
            board[move]=player_min
            _, score = alpha_beta_prunning(alpha,beta,True)
            board[move] = ''
            if score < best:
                best= score
                best_move = move
            beta=min(beta,best)
            if alpha>=beta:
                return best_move,best 
    
    return best_move,best
def get_best_move(initial_state,is_max):
    global board
    print('Initial state')
    print_board(initial_state)
    board=initial_state
    move,score=alpha_beta_prunning(max_best_alpha,min_best_beta,is_max)
    if move==None:
        print('Game draw..')
    elif is_max:
        board[move]='X'
    else:
        board[move]='O'
    print('Best move for maximiser')
    print_board(board)
    print('Best possible score is ',score)
def game_start():
    
    is_max=True
    while(check_winner()==None):
        print_board(board)
        if is_max:
            move,score=alpha_beta_prunning(max_best_alpha,min_best_beta,True)
            is_max=False
        else:
            move,score=alpha_beta_prunning(max_best_alpha,min_best_beta,False)
            is_max=True
        if move==None:
            print('Game draw..')
        elif is_max:
            board[move]='X'
        else:
            board[move]='O'
game_start()
print_board(board)
res=check_winner()
if(res==player_max):
    print('Player X won')
elif(res==player_min):
    print('Player O won')
elif(res=='draw'):
    print('Oops!!! Game Draw....')

