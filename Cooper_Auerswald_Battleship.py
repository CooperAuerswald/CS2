'''
Author: Cooper Auerswald
Date:
Description:
Bugs:
Sources: Charlie Gordon helped me with the basic setup of the rand_dots function
Version: 1.0
'''

import random
def rand_dots(hidden_board):
    random_column= random.randint (0,4)
    random_row = random.randint (0,4)
    while True:
        if hidden_board [random_row] [random_column] == "X":
            hidden_board [random_row] [random_column] = "H"
            break

def turn (player_board, hidden_board,):
    while True:
        #fill
        shot_row = input("Select a row")
        shot_column = input("Select a column")
        if player_board [int (shot_row)-1] [int (shot_column) -1] =="X":
            if hidden_board [int (shot_row)-1] [int (shot_column) -1] =="H":
                print ("Hit!")
                player_board [int (shot_row)-1] [int (shot_column) -1] ="🔥"
                print(f'''
{player_board[0]}
{player_board[1]}
{player_board[2]}
{player_board[3]}
{player_board[4]}
''')
                #fill
                
                #fill
            else: 
                print ("Miss!")
                player_board [int (shot_row)-1] [int (shot_column) -1] ="❌"
                print(f'''
{player_board[0]}
{player_board[1]}
{player_board[2]}
{player_board[3]}
{player_board[4]}
                    ''')
                
                #fill
                return False
        else:
            print ("Invalid move")
        
        


            #turns = 10

            #(after each turn)
            #turns -=1



            # end after all four found or if no turns remaining





def main():
    turns = 10
    while True:
        print (f"{turns} turns remaining")
        player_board = [
                ["X","X","X","X","X"],                 
                ["X","X","X","X","X"], 
                ["X","X","X","X","X"],
                ["X","X","X","X","X"],
                ["X","X","X","X","X"]
                ]
        hidden_board = [
            ["X","X","X","X","X"],                 
            ["X","X","X","X","X"], 
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"]
            ]
        rand_dots (hidden_board)
        rand_dots (hidden_board)
        rand_dots (hidden_board)
        # rand_dots (hidden_board)]
        print(f'''
{player_board[0]}
{player_board[1]}
{player_board[2]}
{player_board[3]}
{player_board[4]}
        ''')
        while turns > 0:
            print (f"{turns} turns remaining")
            turn(player_board, hidden_board)
            turns -= 1

main()

    