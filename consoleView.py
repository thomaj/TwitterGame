import os

# Gets input from the user and casts it to be the type of typeOfResponse
# Repeatedy prompts the user until it is a vaild response
def getValidInput(prompt, typeOfResponse):
    while True:
        try:
            response = typeOfResponse(raw_input(str(prompt) + ' '))
        except ValueError:
            print 'Come on, that wasn\'t valid!'
        else:
            break

    return response

        

# This contains all of the view logic. This uses the command line to show and accept user input
class View:

    # Shows a question
    # question: A question object to show.  Expects a dictionary with ('question': String) and 
    #           ('answers': String[]).
    # returns a Number which is the index of the answer
    def showQuestion(self, question):
        print 'Who said this tweet?\n'
        print question['question'] + '\n'
        for index, answer in enumerate(question['answers']):
            print str(index + 1) + ') ' + answer
        
        userAnswer = getValidInput('Which number is correct?', int)

        return userAnswer - 1

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

    
    def clear():
        os.system('clear')
