# Star Balls
# CSE 210 Tic Tac Toe Game

X = "X"
O = "O"
BLANK = " "
def new_board():
    '''Create a list of nine empty spaces to play tic-tac-toe.'''
    blank_board = [BLANK, BLANK, BLANK, 
                   BLANK, BLANK, BLANK,
                   BLANK, BLANK, BLANK ]
    return blank_board

def is_x_turn(board):
    '''Determine whose turn it is in the game.'''
    count_x = 0
    count_y = 0
    count_blank = 0

    for space in board:
        # Count the number of X's and O's on the board. 
        if space == "X":
            count_x += 1
        elif space == "Y":
            count_y += 1
        else:
            count_blank += 1

        # Compare X's and O's to determine whose turn it is to go. 
        if count_x <= count_y and count_blank != 0:
            return True
        else:
            return False
        
def quit_game(user_input):
    '''Check if the user inputs a "Q" or "q" to end the game.'''
    if user_input == "Q" or user_input == "q":
        return True
    else:
        return False
    
def check_user_input(user_input):
    '''Check if user input is a letter or number. If a letter display error
       message, if not change to an integer and check if the integer is 
       a valid number between one and nine.'''
    try:
        user_input = int(user_input)
        if user_input < 1 or user_input > 9:
            print("Please enter a number between one and nine.")
            return
    except:
        ValueError
        print("Please enter a number one and nine.")
        return
    return user_input
    

def mark_square(user_input, symbol, board):
    if board[user_input - 1] == BLANK:
        board[user_input - 1] == symbol
    else:
        print("Square is already taken.\n"
               "Please enter a number for an empty square.")
    return


print("This is a the game of tic-tac-toe. Take turns putting X's and ",
      "O's on the board. Use the numbers 1 through 9 to identify",
      " where you would like to go.\n")
for number in range(1,10):
    if number % 3 != 0:
        print(" ", number, " |")


    

