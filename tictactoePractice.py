
def check_user_input_number(user_input):
    '''Check if user input is a letter or number. If a letter display error
       message, if not change to an integer and check if the integer is 
       a valid number between one and nine.'''

    while type(user_input) != int:
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Please enter a number, not a letter: ")

        user_input = input("Enter num> ")
    
    return 

def check_user_input_in_range(user_input):
    user_input = check_user_input_number(user_input)
    while user_input < 1 or user_input > 9:

        print("Please enter a valid number.")
        user_input = input("Enter a number in range: ")
        user_input = check_user_input_number(user_input)
    return user_input


    

print()

user_input = input("Number between 1 and 9: ")
input = check_user_input_in_range(user_input)

