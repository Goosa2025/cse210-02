""" Documentation checker

A command-line tool for checking source code documentation requirements.

Authors:
  - Ogunniyi Owamamwen
  - Sheyla Norton
  -
"""
from tictactoe import player_control, create_player_board, player_winner, player_draw, display_board, start_tictactoe


# The main function call other functions to run
# This mean one entry point


def main():
    print("-------------------------------------------\nThe grid with integer values is an example\nplease choose from number\n-------------------------------------------")
    player = player_control("")
    board = create_player_board()
    while not (player_winner(board) or player_draw(board)):
        display_board(board)
        start_tictactoe(player, board)
        player = player_control(player)
    display_board(board)
    print("Winner of the game with three point")


if __name__ == "__main__":
    main()
