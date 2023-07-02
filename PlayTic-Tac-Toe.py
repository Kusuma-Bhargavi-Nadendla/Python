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

 
def play_game(mode):
    global player_x
    print_board()
    if check_winner()!=None:
        return 'END'
   
    if player_x:
        m=int(input("Player X's move(choose move 1-9)"))-1
        if(m>=0 and m<=8):
            if board[m]!='':
                print('Choose an empty cell')
            else:
                board[m]=player_max
                player_x=False
        else:
            print('Choose move between 1-9')
    else:
        if mode==1:
            
            m,_=minimax(False)
            board[m]=player_min
            player_x=True
        elif mode==2:
            m=int(input("Player O's move(choose move 1-9)"))-1
            if(m>=0 and m<=8):
                if board[m]!='':
                    print('Choose an empty cell')
                else:
                    board[m]=player_min
                    player_x=True
            else:
                print('Choose move between 1-9')
                
while True:
    
    print('Let"s play.....\n1.Player vs AI\n2.Player vs Player\nChoose your mode of play:',end=' ')
    mode=int(input())
   
    res=play_game(mode)
    while(res!='END'):
        res=play_game(mode)

    res=check_winner()
    if(res==player_max):
        print('Player X won the game!!!')
    elif(res==player_min):
        print('Player O won the game!!!')
    elif(res=='draw'):
        print('Oops!!! Game Draw....')
    
    con=input('\nDo you wish to play again??\ny-yes\nn-no\n')
    if con=='n':
        break 
    board=['','','','','','','','','']
    player_x=True

    




