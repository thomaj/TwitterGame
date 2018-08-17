from twitterGame import TwitterGame
from consoleView import View

def main():
    game = None
    name = 'player'
    
    # Get the user's name
    print 'Are you ready to guess who tweeted what?'
    name = raw_input('Please enter your name to get started: ')
    game = TwitterGame('player')
    game.start(View())

if __name__ == '__main__':
    main()