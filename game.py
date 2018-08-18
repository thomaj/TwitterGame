# Holds all of the game logic and state
class Game:

    def __init__(self, playerName = 'player'):
        self.playerName = playerName
        self.numRight = 0
        self.numWrong = 0
        self.numSkipped = 0
        self.currentQuestion = None
        self.lengthOfGame = 5


    # Start the game.  This method return once the game is finished
    def start(self, view):
        self.playerName = view.getName()

        while self.numberOfQuestionsAsked() < self.lengthOfGame:
            self.currentQuestion = self.getQuestionAndAnswers()
            userAnswer = view.showQuestion(self.currentQuestion)
            result = self.checkAnswer(userAnswer)

            if result:
                view.showCorrect()
            else:
                view.showWrong()
            view.showScore(self.score())
        
        info = self.score()
        info['playerName'] = self.playerName
        view.showEnd(info)
    

    # Checks if the answer is correct compared to the current question
    # Updates instance members 'numWrong' and 'numRight' accordingly
    # Returns True or False
    def checkAnswer(self, answerIndex):
        correct = True
        if answerIndex != self.currentQuestion['correctIndex']:
            correct = False
            self.numWrong += 1
        else:
            self.numRight += 1

        return correct


    # Returns the number of questions that have been asked. Does not include the current question
    def numberOfQuestionsAsked(self):
        return self.numRight + self.numWrong + self.numSkipped
    
    # Returns a dictionary with information about the score, etc.
    def score(self):
        return {
            'numRight': self.numRight,
            'numWrong': self.numWrong,
            'numSkipped': self.numSkipped,
            'numAsked': self.numberOfQuestionsAsked()
        }