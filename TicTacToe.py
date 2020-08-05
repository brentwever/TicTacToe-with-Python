
from functies_tictactoe import display_board
from functies_tictactoe import check_win_speler1
from functies_tictactoe import check_win_speler2
from functies_tictactoe import reset_board

board=['#','1','2','3','4','5','6','7','8','9']   
display_board(board)
naam1 = input('Speler 1 : Wat is uw naam? : ')
naam2 = input('Speler 2 : Wat is uw naam? : ')
print(naam1+' heeft X, '+naam2+ ' heeft O')
        
doorgaan = True
while doorgaan:
    # voor speler 1
    keuze_speler_1 = input(naam1+' is aan zet, welk cijfer kiest u voor markering? (voor stoppen typ "q") : ')
    if keuze_speler_1=='q':
        doorgaan= False
        break
    for item in board:
        if keuze_speler_1 == item:
            board[int(keuze_speler_1)]='X'
    display_board(board)
    if check_win_speler1(board):
        print('YES '+naam1+' heeft gewonnen!!')
        again = input('Wilt u nog een keer spelen? (y/n) : ')
        if again == 'y':
            board = reset_board()
            display_board(board)
            continue
        else:
            break

    # voor speler 2
    keuze_speler_2 = input(naam2+' is aan zet, welk cijfer kiest u voor markering? (voor stoppen typ "q") : ')
    if keuze_speler_2=='q':
        doorgaan= False
        break
    for item in board:
        if keuze_speler_2 == item:
            board[int(keuze_speler_2)]='O'
    display_board(board)
    if check_win_speler2(board):
        print('YES '+naam2+' heeft gewonnen!!')
        again = input('Wilt u nog een keer spelen? (y/n) : ')
        if again == 'y':
            board = reset_board()
            display_board(board)
            continue
        else:
            break

print('Game over')