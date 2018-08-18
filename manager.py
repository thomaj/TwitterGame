from twitterGame import TwitterGame
from consoleView import View

def main():
    view = View()
    view.showSplash()

    game = TwitterGame()
    game.start(view)

if __name__ == '__main__':
    main()