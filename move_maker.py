"""This class is the main class that should be modified to make moves in order to play the game.
"""


class MoveMaker:

    def __init__(self):
        """This class is initialized when the program first runs.
        All variables stored in this class will persist across moves.
        Do any initialization of data you need to do before the game begins here.
        """
        print("Matthew J Gunton and Brian Snyder")

    def make_move(self, mancala_board):

        # {
        #     "MyCups": [4, 3, 2, 1, 5, 3],
        #     "MyMancala": 0,
        #     "OpponentCups": [3, 6, 2, 0, 1, 2],
        #     "OpponentMancala": 3
        # }

        #strategy:
        # 1) take all free moves as they happen
        # 2) can it land on an empty space & steal
        # 3) if all else fails, whichever is closest, you move



        NUMOFCUPS = 6

        #1
        for i in range(NUMOFCUPS-1,-1,-1):
            #we don't account for if you can go around and get this
            if mancala_board["MyCups"][i] == NUMOFCUPS - i:
                return i

        #2
            if mancala_board["MyCups"][i] == 0 and mancala_board["OpponentCups"][5-i] != 0:
                for curIndex, stone_count in enumerate(mancala_board["MyCups"]):
                    if i > curIndex:
                        if i == stone_count - 13 + curIndex and stone_count != 0:
                            print("we found a way to steal")
                            return curIndex

                    else:

                        if stone_count == i - curIndex and stone_count != 0:
                            print("we found a way to steal\n our index:"+str(i)+"\n current index: "+str(curIndex)+"\n stone count"+str(stone_count))
                            return curIndex

        print("nothing better")
        #3

        for i in range(NUMOFCUPS - 1, -1, -1):
            if (mancala_board["MyCups"][i] != 0):
                return i




        return 0
