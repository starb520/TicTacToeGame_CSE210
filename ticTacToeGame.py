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
    count_o = 0
    count_blank = 0

    for space in range(len(board)):
        # Count the number of X's and O's on the board. 
        if board[space] == X:
            count_x += 1
        elif board[space] == O:
            count_o += 1
        else:
            count_blank += 1

        # Compare X's and O's to determine whose turn it is to go. 
    if count_x <= count_o and count_blank != 0:
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
    except ValueError:
        print("Please enter a number between one and nine.")
        return
    return user_input
    

def mark_square(user_input, symbol, board):
    if board[user_input - 1] == BLANK:
        board[user_input - 1] = symbol
    else:
        print("Square is already taken.\n"
               "Please enter a number for an empty square.")
    return

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))  

def game_done(board, message=False):
    for space in range(len(board)):
        pass 


def play_game(board):
    '''Continue to prompt for X and O until the game is ended. The game ends 
    by one player getting three in a row horizontally, vertically, or 
    diagonally, or neither player wins (a tie), or the game is quit.'''
    end = False

    while end == False:
        is_x_turn(board)
        if is_x_turn(board) == True:
            symbol = X
        else:
            symbol = O

        user_input = input(symbol + "> ")

        # Check if the user wants to end the game by enters q.
        if quit_game(user_input) == True:
            end = True
            return 

        # Check the user input for validity. Is it a number 1 through 9?
        # No letters or invalid numbers.
        else:
            user_input = check_user_input(user_input)

        # Put an X or O on the board and save to the game list of moves.
        mark_square(user_input, symbol, board)
        display_board(board)

    
print()
print("This is a the game of tic-tac-toe.")
print("Take turns putting X's or O's in the spaces ")
print("1 through 9 to play the game or press 'Q' to quit.")
print("\t  1 | 2 | 3 ")
print("\t ---+---+---")
print("\t  4 | 5 | 6 ")
print("\t ---+---+---")
print("\t  7 | 8 | 9 ")

# Create a blank board for tic-tac-toe game.
board = new_board()
play_game(board)




    

