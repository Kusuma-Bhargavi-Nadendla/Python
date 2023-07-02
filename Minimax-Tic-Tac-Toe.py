board=['','','','','','','','','']
player_max='X'
player_min='O'

def print_board():
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
        return 'draw'
    return None 
def generate_moves():
    moves=[]
    for i in range(9):
        if board[i]=='':
            moves.append(i)
    return moves 
def minimax(is_player_max):
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
            _, score = minimax(False)
            board[move] = ''
            if score > best:
                best= score
                best_move = move
    else:
        best=1000
        for move in generate_moves():
            board[move]=player_min
            _, score = minimax(True)
            board[move] = ''
            if score < best:
                best= score
                best_move = move
    return best_move,best
player_x=True
while(check_winner()==None):
    print_board()
    if player_x:
        m,_=minimax(True)
        board[m]=player_max
        player_x=False
    else:
        m,_=minimax(False)
        board[m]=player_min
        player_x=True
print_board()
res=check_winner()
if(res==player_max):
    print('Player X won the game!!!')
elif(res==player_min):
    print('Player O won the game!!!')
elif(res=='draw'):
    print('Oops!!! Game Draw....')

