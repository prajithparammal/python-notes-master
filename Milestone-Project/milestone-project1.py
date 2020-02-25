
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


##test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    marker =''
    while marker != 'X' and marker !='O':
        marker = input('Player 1: Choose X or O:').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#player1_marker, player2_marker = player_input()

#print("Player 1 marker is", player1_marker)
#print("Player 2 marker is", player2_marker)

def place_marker(board, marker, position):
    board[position] = marker

#place_marker(test_board, '$', 9)
#display_board(test_board)

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

##win_check(test_board,'x')

import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

##############################################
def space_check(board, position):
    return board[position] == ' '

###############################################
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

##############################################
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
    return position

###############################################

def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'
###############################################

# While loop to keep running th game
print('Welcome to TIc Tac Toe')
while True:
    # play the game
    # set everything up (board, who is first, choose Marker x,o)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n?')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    #game play
    while game_on:
        if turn == 'Player 1':
            #show the board
            display_board(the_board)
            #chose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            #chose a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    break
                else:
                    turn = 'Player 1'
    #player 2 turn
    if not replay():
        break






#Break out the while loop on replay()


