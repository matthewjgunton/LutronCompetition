"""The main function to run the manacala game.
THIS FILE IS PART OF THE SKELETON FRAMEWORK AND SHOULD NOT BE MODIFIED AS PART OF THE PROGRAMMING COMPETITION.
"""
from sys import argv
import request_util
from move_maker import MoveMaker
from constants import JsonKey
from config import user_id


def print_board(board):
    """This method will pretty print a mancala board to the console.

    Parameters:
    mancala_board (python dict): python dictionary of the game board.
    """
    num_spaces = ((len(board[JsonKey.MY_CUPS]) * 2) + 3)
    num_spaces -= len(str(board[JsonKey.OPPONENT_MANCALA]))
    num_spaces -= len(str(board[JsonKey.MY_MANCALA]))
    num_dashes = (4 + (len(board[JsonKey.MY_CUPS]) * 2) - 1)
    print(" {0}".format("-" * num_dashes))
    print("|  " + "|".join(str(x) for x in board[JsonKey.OPPONENT_CUPS][::-1]) + "  |")
    print("|" + str(board[JsonKey.OPPONENT_MANCALA]) + (" " * num_spaces) + str(board[JsonKey.MY_MANCALA]) + "|")
    print("|  " + "|".join(str(x) for x in board[JsonKey.MY_CUPS]) + "  |")
    print(" {0}".format("-" * num_dashes))

def print_instructions(): 
    print("\nChoose the difficulty to play against from easy, medium, and hard\n\nEx: python main.py easy\n")
def get_difficulty():
    diffs = {"easy":"1", "medium":"2", "hard":"3"}
    if len(argv) != 2 or argv[1] not in diffs:
        print_instructions()
        quit()
    return diffs[argv[1]]


def main():
    """This is the main starting point of the application.
    Calling main will start a new game and run until the game ends.
    """
    opponent_id = get_difficulty()
    response = request_util.send_new_game_request(opponent_id, user_id)
    session_id = response.headers[JsonKey.SESSION_ID]
    current_board = response.json()[JsonKey.ARGS][JsonKey.BOARD_STATUS]
    print("Initial Board")
    print_board(current_board)
    game_over = False

    user_move_maker = MoveMaker()
    while not game_over:
        next_move_index = user_move_maker.make_move(current_board)
        print("Picking cup #{}\n\n".format(next_move_index))
        response_json = request_util.make_move(session_id, user_id, next_move_index).json()
        current_board = response_json[JsonKey.ARGS][JsonKey.BOARD_STATUS]
        print_board(current_board)
        game_over = response_json[JsonKey.ARGS][JsonKey.GAME_OVER]

    print("\n\nGame over!")


if __name__ == "__main__":
    main()
