def display_board(board):
    
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+ ' | '+board[9])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+ ' | '+board[6])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+ ' | '+board[3])
    print('   |   |')

def check_win_speler1(board):
    # horizontaal
    if board[7] == 'X' and board[8] =='X' and board [9]=='X':
        return True
    elif board[4] == 'X' and board[5] =='X' and board [6]=='X':
        return True
    elif board[1] == 'X' and board[2] =='X' and board [3]=='X':
        return True

    # verticaal
    elif board[7] == 'X' and board[4] =='X' and board [1]=='X':
        return True
    elif board[8] == 'X' and board[5] =='X' and board [2]=='X':
        return True
    elif board[9] == 'X' and board[6] =='X' and board [3]=='X':
        return True

    # diagonaal
    elif board[7] == 'X' and board[5] =='X' and board [3]=='X':
        return True
    elif board[1] == 'X' and board[5] =='X' and board [9]=='X':
        return True
 
def check_win_speler2(board):
    # horizontaal
    if board[7] == 'O' and board[8] =='O' and board [9]=='O':
        return True
    elif board[4] == 'O' and board[5] =='O' and board [6]=='O':
        return True
    elif board[1] == 'O' and board[2] =='O' and board [3]=='O':
        return True

    # verticaal
    elif board[7] == 'O' and board[4] =='O' and board [1]=='O':
        return True
    elif board[8] == 'O' and board[5] =='O' and board [2]=='O':
        return True
    elif board[9] == 'O' and board[6] =='O' and board [3]=='O':
        return True

    # diagonaal
    elif board[7] == 'O' and board[5] =='O' and board [3]=='O':
        return True
    elif board[1] == 'O' and board[5] =='O' and board [9]=='O':
        return True

def reset_board():
    new_board=['#','1','2','3','4','5','6','7','8','9']  
    return new_board