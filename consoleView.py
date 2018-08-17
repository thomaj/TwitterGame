class View:

    def showQuestion(self, question):
        print 'Who said this tweet?\n {!r}\n\n'.format(question['question'])
        for index, answer in enumerate(question['answers']):
            print '{}) {!r}'.format(index, answer)
        
        userAnswer = raw_input('Which number is correct? ')
        return int(userAnswer)

    def showCorrect(self):
        print 'Correct!\n\n'


    def showWrong(self):
        print 'Wrong!\n\n'
    

    def showScore(self, scoreDict):
        print 'Score -- Correct: {}, Incorrect: {}\n\n'.format(scoreDict['numRight'], scoreDict['numWrong'])
