
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

def player_selection():
    player_type = None
    
    def prompt():
        response = raw_input ('Please choose [X]s or [O]s: ')
        if response.upper <> 'X' or response.upper <> 'O':
            print 'You entered: %s ' %(response.upper)
            print 'Sorry, invalid entry. Try again.'
            prompt()
        player_type = response.upper

    prompt()


board = [1,2,3,4,5,6,7,8,9]

print 'Welcome to Tic Tac Toe!'
player_selection()

#print_board()
