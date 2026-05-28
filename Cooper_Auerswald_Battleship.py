'''
Author: Cooper Auerswald
Date: 5/28/2026
Description: 
    Battleship game where the player has 10 turns to find 3 hidden ships on a 5x5 grid.
Bugs: 
    Fixed infinite loop in rand_dots, fixed game not ending, fixed crash on
    invalid input, fixed board resetting each loop iteration.
Sources: Charlie Gordon helped me with the basic setup of the rand_dots function
Version: 1.1
'''

import random

def rand_dots(hidden_board): #function to randomly place ships on the hidden board
    while True: #loop to ensure we place a ship in an empty spot
        random_column = random.randint(0, 4) #generate random column index
        random_row = random.randint(0, 4) #generate random row index
        if hidden_board[random_row][random_column] == "X": #check if the spot is empty
            hidden_board[random_row][random_column] = "H" #place a ship
            break

def print_board(player_board): #function to print the player's board
    print() 
    for row in player_board: #loop through each row in the player's board and print it
        print(row)
    print()

def turn(player_board, hidden_board, hits): #function to handle a player's turn, takes in the player's board, the hidden board, and the current number of hits
    while True: #loop to ensure valid input and that the player doesn't guess the same spot twice
        shot_row = input("Select a row (1-5): ") #prompt the player to select a row
        if not shot_row.isdigit() or not (1 <= int(shot_row) <= 5): #check if the input is a valid number between 1 and 5   
            print("Invalid input. Please enter a number between 1 and 5.") #if the input is invalid, print an error message and prompt again
            continue

        shot_column = input("Select a column (1-5): ") #prompt the player to select a column
        if not shot_column.isdigit() or not (1 <= int(shot_column) <= 5): #check if the input is a valid number between 1 and 5
            print("Invalid input. Please enter a number between 1 and 5.") # if the input is invalid, print an error message and prompt again
            continue

        row = int(shot_row) - 1 #convert the input to an index by subtracting 1
        col = int(shot_column) - 1 #convert the input to an index by subtracting 1

        if player_board[row][col] == "🔥" or player_board[row][col] == "❌": #check if the spot has already been guessed
            print("You already guessed that spot. Try again.") #if the spot has already been guessed, print an error message and prompt again
            continue

        if hidden_board[row][col] == "H": #check if the shot is a hit
            print("Hit!") #if the shot is a hit, print a message and update the player's board with a fire emoji
            player_board[row][col] = "🔥" 
            hits += 1 #increment the number of hits
        else:
            print("Miss!")
            player_board[row][col] = "❌" #if the shot is a miss, print a message and update the player's board with a cross emoji

        print_board(player_board)
        return hits

def main(): #main function to run the game
    turns = 10 #number of turns the player has to find the ships
    hits = 0 #number of hits the player has made
    total_ships = 3 #total number of ships hidden on the board

    player_board = [ #initialize the player's board with "X" to represent unknown spots
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"]
    ]
    hidden_board = [ #the hidden board where the ships will be placed, initialized with "X" to represent empty spots
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X"]
    ]

    rand_dots(hidden_board)
    rand_dots(hidden_board)
    rand_dots(hidden_board)

    print_board(player_board)

    while turns > 0 and hits < total_ships: #loop to allow the player to take turns until they run out of turns or find all the ships
        print(f"{turns} turns remaining") #display the number of turns remaining
        hits = turn(player_board, hidden_board, hits) #call the turn function to handle the player's turn and update the number of hits
        turns -= 1 #decrement the number of turns after each turn

    if hits == total_ships: #if the player found all the ships, print a victory message
        print("You found all the ships! You win!") 
    else:
        print("Out of turns! Game over.")

main()