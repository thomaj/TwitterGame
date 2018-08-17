# Holds all of the game logic and state
class Game:

    def __init__(self, playerName):
        self.playerName = playerName
        self.numRight = 0
        self.numWrong = 0
        self.numSkipped = 0
        self.currentQuestion = None


    # Start the game.  This method return once the game is finished
    def start(self, view):
        while self.numberOfQuestionsAsked() < 3:
            self.currentQuestion = self.getQuestionAndAnswers()
            userAnswer = view.showQuestion(self.currentQuestion)
            result = self.checkAnswer(userAnswer)

            if result:
                view.showCorrect()
            else:
                view.showWrong()
            view.showScore(self.score())
    

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


    def numberOfQuestionsAsked(self):
        return self.numRight + self.numWrong + self.numSkipped
    

    def score(self):
        return {
            'numRight': self.numRight,
            'numWrong': self.numWrong,
            'numSkipped': self.numSkipped,
            'numAsked': self.numberOfQuestionsAsked()
        }