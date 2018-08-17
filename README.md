# TwitterGame

Guess who tweeted what!  Read a tweet and choose which one of your friends tweeted it.  See how well you know you know your friends and your feed.

This is a command line program with plans to expand to have a UI.

## Organization

The game can be run by running the commad `python manager.py`.

#### manager.py
This module determines what is currently happening in the program.  Currently, it only asks for your name and starts the game, but it is here where settings pages stats could be displayed.

#### game.py
This module is what contains all of the game logic.  This module contains the Game class and is where the game loop resides and keeps the current state of the game.

#### twitterGame.py
This module is what allows the game to interact with a user's Twitter.  This module contains the TwitterGame class which can get question and answers by sending requests to the Twitter api.

#### consoleView.py
This module contains the View class, which is the view in the MVC paradigm.  This View class is what displays the question and allows the user to interact with the program.

