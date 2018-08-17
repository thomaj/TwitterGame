
# This contains all of the view logic. This uses the command line to show and accept user input
class View:

    # Shows a question
    # question: A question object to show.  Expects a dictionary with ('question': String) and 
    #           ('answers': String[]).
    # returns a Number which is the index of the answer
    def showQuestion(self, question):
        print 'Who said this tweet?\n {!r}\n\n'.format(question['question'])
        for index, answer in enumerate(question['answers']):
            print '{}) {!r}'.format(index, answer)
        
        userAnswer = raw_input('Which number is correct? ')
        return int(userAnswer)

    # Informs the user they are correct
    def showCorrect(self):
        print 'Correct!\n\n'

    # Informs the user they are wrong
    def showWrong(self):
        print 'Wrong!\n\n'
    
    # Shows the current score of the game
    # scoreDict should by a dictionary with ('numRight': Int) and ('numWrong': int)
    def showScore(self, scoreDict):
        print 'Score -- Correct: {}, Incorrect: {}\n\n'.format(scoreDict['numRight'], scoreDict['numWrong'])
