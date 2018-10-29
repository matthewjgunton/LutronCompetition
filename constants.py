"""The constants for handling http requests to the server.
THIS FILE IS PART OF THE SKELETON FRAMEWORK AND SHOULD NOT BE MODIFIED AS PART OF THE PROGRAMMING COMPETITION.
"""


class JsonKey:
    OPPONENT_ID = "OpponentID"
    USER_ID = "UserID"
    ARGS = "args"
    MOVE_INDEX = "MoveIndex"
    SESSION_ID = "SessionID"
    GO_FIRST = "GoFirst"
    GAME_OVER = "GameOver"
    BOARD_STATUS = "BoardStatus"
    MY_CUPS = "MyCups"
    MY_MANCALA = "MyMancala"
    OPPONENT_CUPS = "OpponentCups"
    OPPONENT_MANCALA = "OpponentMancala"


class UrlPath:
    GAME_TYPE = "mancala"
    BEGIN_GAME = "begin_game"
    MAKE_MOVE = "make_move"


server_ip = "https://lutron-code-competition.herokuapp.com:443"
