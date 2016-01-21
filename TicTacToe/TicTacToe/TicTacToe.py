
global player1
global player2

def print_board():
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

# Allows Player 1 to choose 'X's or 'O's
def player_selection():
    '''
    Allows Player 1 to choose Xs or Os.
    '''
    def prompt():
        # Will continue to prompt user until a valid entry is made.
        response = raw_input ('Player 1:  Please choose [X]s or [O]s: ')
        response = response.upper()
        if str(response) != 'X' and str(response) != 'O':
            print 'Invalid entry!  Please try again...'
            return False
        player1 = str(response)
        # Sets the global variables to establish player 1 and player 2
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        return True
    
    # Loops until valid selection is made.
    if not prompt():
        prompt()


board = [1,2,3,4,5,6,7,8,9]

print 'Welcome to Tic Tac Toe!'
player_selection()
print_board()
