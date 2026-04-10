def display_board(board):
    print (f'''
     1    2    3
1  {board[0][0]}  | {board[0][1]}  | {board[0][2]}             
   ---|---|---
2  {board[1][0]}  | {board[1][1]}  | {board[1][2]}
   ---|---|---
3  {board[2][0]}  | {board[2][1]}  | {board[2][2]}
           ''')

def get_player_move(board, player):
    while True:
        while True:
            if player == 'x':
                row = input ("You are player X, what row do you want? ")
            else:
                row = input ("You are player O, what row do you want? ")
            if row == '1' or row == '2' or row =='3':
                pass
            else:
                print ("Row does not exist, pick 1,2, or 3")
                continue
            column = input ("What column do you want ")
            if column == '1' or column == '2' or column =='3':
                break
            else:
                print ("Column does not exist, pick 1,2, or 3")
                continue
        if board [int(row)-1][int(column)-1]=='':
            board [int(row)-1][int(column)-1]= player
            break
        else:
            print ("Space Taken")

def check_winner(board):
    if board [0][0] == 'x' and board [0][1] == 'x' and board [0][2] == 'x':
        return 'x'
    elif board [0][0] == 'o' and board [0][1] == 'o' and board [0][2] == 'o':
        return 'o'
    elif board [1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
        return 'x'
    elif board [1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
        return 'o'
    elif board [2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
        return 'x'
    elif board [2][0] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
        return 'o'
    elif board [0][0] == 'x' and board [1][0] == 'x' and board [2][0] == 'x':
        return 'x'
    elif board [0][0] == 'o' and board [1][0] == 'o' and board [2][0] == 'o':
        return 'o'
    elif board [0][1] == 'x' and board [1][1] == 'x' and board [2][1] == 'x':
        return 'x'
    elif board [0][1] == 'o' and board [1][1] == 'o' and board [2][1] == 'o':
        return 'o'
    elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
        return 'x'
    elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'o':
        return 'o'
    elif board [0][0] == 'x' and board [1][1] == 'x' and board [2][2] == 'x':
        return 'x'
    elif board [0][0] == 'o' and board [1][1] == 'o' and board [2][2] == 'o':
        return 'o'
    elif board [2][0] == 'x' and board [1][1] == 'x' and board [0][2] == 'x':
        return 'x'
    elif board [2][0] == 'o' and board [1][1] == 'o' and board [0][2] == 'o':
        return 'o'
    return None

def is_draw(board):
    if board[0][0] != '' and board[0][1] != '' and board[0][2] != '' and board[1][0] != '' and board[1][1] != '' and board[1][2] != '' and board[2][0] != '' and board[2][1] != '' and board[2][2] != '':
        return True
    return False

def main():
    while True:
        player = 'x'
        board = [
        ["","",""],                 
        ["","",""],
        ["","",""]
        ]

        while True:
            display_board(board)
            get_player_move(board, player)

            winner = check_winner(board)
            if winner:
                display_board(board)
                print (f"{winner.upper()} wins!")
                break

            if is_draw(board):
                display_board(board)
                print ("Draw :|")
                break

            if player == 'x':
                player = 'o'
            else:
                player = 'x'

        play_again = input("Play again? (y/n) ")
        if play_again != 'y':
            break

main()