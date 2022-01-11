# The solution for the game create player board
def create_player_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board
# Display the game board to the screen
# The display_board hold one parameter pass it into grid
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


# player control condition for two 'x' and 'o' set the input range
#def player_draw(board):

# The play winner of the game
#def player_winner(board):

# The player require input integer value
# def start_tictactoe(player, board):

# The player are two 'x' and 'o'
# Who the current player is 'X goes first'
# def player_control(player):
