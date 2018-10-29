# Lutron Programming Competition - Python
This repository contains the technical documentation and details of the Programming Competition used by Lutron - specifically for Python.

# Game
### [Mancala](https://en.wikipedia.org/wiki/Mancala)
#### [Mancala Rules](https://www.thesprucecrafts.com/how-to-play-mancala-409424)

#Before Running
Please update your user id in config.py to be your full name.

#How To Run:
Have python 3.4 or greater installed

You can check your python versions using python --version or python3 --version

Run the following command to install dependencies (this may require running with sudo(mac or linux) or powershell prompt as administrator(windows) depending on how you have setup python)
    pip3 install -r requirements.txt //if pip --version shows "... python 2.x"
    pip install -r requirements.txt //if pip --version shows "... python 3.x"

You must now choose a unique name for yourself, and set it as the user_id inside the config.py file
Once you set this you cannot change it!

To run the program just run
    python3 main.py <difficulty> //if python --version shows "... python 2.x.xx"
    python main.py <difficulty>  //if python --version shows "... python 3.x.xx"
    
replacing <difficulty> with either easy, medium, or hard



#For programming:
All your code changes should be in move_maker.py
Whenever it is your turn move_maker.make_move is called with the current state of the board.
Your code should return an integer of the cup you want to select to make.
The mancala_board variable is a dictionary that looks like:

{
	"MyCups": [4, 3, 2, 1, 5, 3],
	"MyMancala": 0,
	"OpponentCups": [3, 6, 2, 0, 1, 2],
	"OpponentMancala": 3
}

This data structure would map to an actual mancala board like this (notice that the opponent side is flipped):

     ---------------
    |  2|1|0|2|6|3  |
    |3             0|
    |  4|3|2|1|5|3  |
     ---------------
 CUP:  0 1 2 3 4 5

So returning the number 1 would select the cup with 3 pieces in it.

You can interact with the board using standard python dictionary commands.
eg:

mancala_board["MyCups"][0]   would return 4
mancala_board["OpponentCups"][5]   would return 2
mancala_board["MyMancala"]  would return 0

