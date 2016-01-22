import os

# Global Variables
board = [1,2,3,4,5,6,7,8,9] # List to hold board positions
draw_board = None
player1 = None # String value: either 'X' or 'O'
player2 = None # String value:  either 'X' or 'O'
player1_first = None # Boolean value:  True is Player 1 plays first, False if otherwise.
player_next = None # String value:  next player to move
move_num = None # Integer value:  tracks total number of moves in game.
MAX_MOVES = 9 # Constant:  total moves allowed in single game.
game_won = None # A boolean:  a flag to determine if the game has been won. 

############################################
# Draws the board
############################################
def draw_board():
    '''
    Draws the Tic Tac Toe Board
    '''
    global drawing_board

    drawing_board = []
    i = 0
    
    for square in board:
        if str(board[i]).isdigit():
            drawing_board.append(' ')
        else:
            drawing_board.append(str(board[i]))
        i += 1

    print '\n'
    print '       ' + '|' + '       ' + '|' + '       ' 
    print '   ' + drawing_board[0] + '   ' + '|' + '   ' + drawing_board[1] + '   ' + '|' + '   ' + drawing_board[2] + '   '
    print '-------|-------|-------'
    print '       ' + '|' + '       ' + '|' + '       ' 
    print '   ' + drawing_board[3] + '   ' + '|' + '   ' + drawing_board[4] + '   ' + '|' + '   ' + drawing_board[5] + '   '
    print '-------|-------|-------'
    print '       ' + '|' + '       ' + '|' + '       ' 
    print '   ' + drawing_board[6] + '   ' + '|' + '   ' + drawing_board[7] + '   ' + '|' + '   ' + drawing_board[8] + '   '
    print '\n'

############################################
# Allows Player 1 to choose 'X's or 'O's
############################################
def player_selection():
    '''
    Prompts Player 1 to choose Xs or Os.
    '''
    global player1 
    global player2
    global player1_first

    # Will continue to prompt user until a valid entry is made.
    print '\n'
    response = raw_input ('Player 1:  Please choose [X]s or [O]s: ')
    #response = response.upper()
    if str(response.upper()) != 'X' and str(response.upper()) != 'O':
        print 'Invalid entry!  Please try again...'
        return False
            
    # Sets the global variables to establish player 1 and player 2
    # Player who chooses 'X's will always play first
    player1 = str(response.upper())
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
# Prompts a player to make valid move
############################################
def player_move ():
    '''
    Prompts the appropriate player to make a move.
    '''
    global move_num
    global player_next
    valid_move = False


    player_next = next_to_play()

    # Loop until the next player makes a valid move.
    while not valid_move:
        response = raw_input ("Player %s's turn.  Choose an empty square: " %(player_next))
        # Must be a numeric value
        if not response.isdigit():
            print 'Please enter a numeric value between 1 and 9!!'
        # Must be between 1 and 9 (inclusive)
        elif not (1 <= int(response) <= 9):
            print 'Please enter a square number between 1 and 9!!'
        # Must be an empty square
        elif board[int(response)-1] == 'X' or board[int(response)-1] == 'O':
            print 'Square has already been taken.  Try again.'
        else:  
            # Valid remove, so record it
            if player_next == 1:
                board[int(response)-1 ] = player1
            else:
                board[int(response)-1] = player2

            # iterate move number and set to valid move
            move_num +=1
            valid_move = True

            # Redraw board
            os.system('cls')
            draw_board()

############################################
# Determines who is next to play
############################################
def next_to_play():
    '''
    Determines who is next to play.
    '''
    if move_num == 0:
        if player1_first:
            return 1
        else:
            return 2            
    else:
        if player1_first:
            if move_num % 2 == 0:
                return 1
            else:
                return 2
        else:
            if move_num % 2 == 0:
                return 2
            else:
                return 1

############################################
# TODO: Fix to win when move made on the final move
############################################
def game_is_won():
    '''
    Determine if a player had won the game.
    '''
    global game_won
    # If minimum number of moves for a win
    # hasn't been reached, game is not won
    if move_num < 5:
        return False

    # Row 1 Victory
    if (board[0] == board [1] == board[2]):
        game_won = True
        return game_won
    # Row 2 Victory
    elif board[3] == board[4] == board[5]:
        game_won = True
        return game_won
    # Row 3 Victory
    elif board[6] == board[7] == board[8]:
        game_won = True
        return game_won
    # Column 1 Victory
    elif board[0] == board[3] == board[6]:
        game_won = True
        return game_won
    # Column 2 Victory
    elif board[1] == board[4] == board [7]:
        game_won = True
        return game_won
    # Column 3 Victory
    elif board[2] == board[5] == board[8]:
         game_won = True
         return game_won
    # Diagonal 1 Victory
    elif board[0] == board[4] == board[8]:
        game_won = True
        return game_won
    #Diagonal 2 Victory
    elif board[2] == board[4] == board[6]:
        game_won = True
        return game_won
    else:
        return False

############################################
# Play TIC TAC TOE!
############################################
def play_game():
    global move_num
    global board
    global drawing_board
    global player1
    global player2
    global player_next
    global game_won

    playing = True

    # Welcome message
    print 'Welcome to Tic Tac Toe!\n'

    while playing:
        # Game setup
        move_num = 0
        player_selection()
        os.system('cls')
        draw_board()

        # Game is played until game is won or board is filled.
        while not game_is_won() and move_num < MAX_MOVES:
            player_move()

        # Finishes game
        print '\n'
        if game_won:
            print 'GAME WON BY PLAYER %s!!\n' %(player_next)
        else:
            print 'GAME IS A DRAW!!\n'

        # Play again?
        again = raw_input('Would you like to play again, [Y]es OR [N]o?')
        again = again.upper()
        if again != 'Y':
            print '\n'
            print 'Exiting game...\n'
            playing = False

        drawing_board = None
        board = [1,2,3,4,5,6,7,8,9]
        player1 = None
        player2 = None
        player_next = None
        game_won = False


play_game()