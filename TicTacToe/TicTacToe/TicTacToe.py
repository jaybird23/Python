
# Global Variables
player1 = None
player2 = None
player1_first = None
player_next = None
move_num = 0


# TODO:  Force a redraw given the last valid move.
def print_board():
    '''
    Draws the Tic Tac Toe Board
    '''
    print '   ' + '|' + '   ' + '|' + '   '
    print '   ' + '|' + '   ' + '|' + '   '
    print '   ' + '|' + '   ' + '|' + '   '
    print '-----------'
    print '   ' + '|' + '   ' + '|' + '   '
    print '   ' + '|' + '   ' + '|' + '   '
    print '   ' + '|' + '   ' + '|' + '   '
    print '-----------'
    print '   ' + '|' + '   ' + '|' + '   '
    print '   ' + '|' + '   ' + '|' + '   '
    print '   ' + '|' + '   ' + '|' + '   '
    print '\n'

############################################
# Allows Player 1 to choose 'X's or 'O's
############################################
def player_selection():
    '''
    Prompts Player 1 to choose Xs or Os.
    '''
    global player1 # String value: either 'X' or 'O'
    global player2 # String value:  either 'X' or 'O'
    global player1_first  # Boolean value:  True is Player 1 plays first, False if otherwise.

    # Will continue to prompt user until a valid entry is made.
    response = raw_input ('Player 1:  Please choose [X]s or [O]s: ')
    response = response.upper()
    if str(response) != 'X' and str(response) != 'O':
        print 'Invalid entry!  Please try again...'
        return False
            
    # Sets the global variables to establish player 1 and player 2
    # Player who chooses 'X's will always play first
    player1 = str(response)
    if player1 == 'X':
        player2 = 'O'
        player1_first = True
    else:
        player2 = 'X'
        player1_first = False
    return True
    
    # Loops until valid selection is made.
    if not player_selection():
        player_selection()

############################################
# TODO:
############################################
def player_move ():
    '''
    Prompts the appropriate player to make a move.
    '''
    global move_num
    global player_next


    player_next = next_to_play()
    print "Player %s's turn." %(player_next)

    move_num +=1

############################################
# Determines who is next to play
############################################
def next_to_play():
    '''
    Determines who is next to play.
    '''
    if move_num == 0:
        if player1_first:
            return player1
        else:
            return player2            
    else:
        if player1_first:
            if move_num % 2 == 0:
                return player1
            else:
                return player2
        else:
            if move_num % 2 == 0:
                return player2
            else:
                return player1

############################################
# TODO:
############################################
def game_is_won():
    #TODO:  Always returns false for now.
    return False

############################################
# Main application flow section
############################################

# List to hold board positions
board = [1,2,3,4,5,6,7,8,9]

# Welcome message
print 'Welcome to Tic Tac Toe!\n'

# Game setup
player_selection()
print_board()

# Game is played until game is won or board is filled.
while not game_is_won() and move_num < 9:
    player_move()

# Finishes game
print '\n'
if move_num != 9:
    print 'GAME WON BY PLAYER %s!!' %(player_next)
else:
    print 'GAME IS A DRAW!!'

