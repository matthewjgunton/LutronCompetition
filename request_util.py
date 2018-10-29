"""The class for making network requests to the game server.
THIS FILE IS PART OF THE SKELETON FRAMEWORK AND SHOULD NOT BE MODIFIED AS PART OF THE PROGRAMMING COMPETITION.
"""

import requests
from constants import JsonKey, UrlPath, server_ip


def send_new_game_request(opponent_id, user_id):
    """This method sends a request to start a new game

    Parameters:
    string opponent_id: the opponent id
    string user_id: the user id

    Returns:
    http response: The response of the server
    """
    request_json = {
        JsonKey.ARGS: {
            JsonKey.OPPONENT_ID: opponent_id,
            JsonKey.GO_FIRST: user_id
        }
    }
    headers = {
        JsonKey.USER_ID: user_id
    }
    return requests.post("/".join([server_ip, UrlPath.GAME_TYPE, UrlPath.BEGIN_GAME]), json=request_json,
                         headers=headers)


def make_move(session_id, user_id, move_index):
    """This method sends a request to make a move in an on going game

    Parameters:
    string session_id: the session id returned when making a start game request
    string user_id: the user id
    int move_index: the cup number you want to pick for your next move

    Returns:
    http response: The response of the server
    """

    request_json = {
        JsonKey.ARGS: {
            JsonKey.MOVE_INDEX: move_index
        }
    }

    headers = {
        JsonKey.SESSION_ID: session_id,
        JsonKey.USER_ID: user_id
    }

    return requests.put("/".join([server_ip, UrlPath.GAME_TYPE, UrlPath.MAKE_MOVE]), json=request_json, headers=headers)
