import os
import time

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

    # shows the splash screen
    def showSplash(self):
        self.clear()
        print '---------------------------------------'
        print '-------------- Welcome! ---------------'
        print '---------------------------------------'


    # Asks the user for their name and returns it
    def getName(self):
        self.clear()
        name = 'player'
        # Get the user's name
        print 'Are you ready to guess who tweeted what?'
        name = getValidInput('Please enter your name to get started: ', str)
        return name

    # Shows a question
    # question: A question object to show.  Expects a dictionary with ('question': String) and 
    #           ('answers': String[]).
    # returns a Number which is the index of the answer
    def showQuestion(self, question):
        self.clear()
        print 'Who said this tweet?\n'
        print question['question'] + '\n'
        for index, answer in enumerate(question['answers']):
            print str(index + 1) + ') ' + answer

        print question['correctIndex']
        
        userAnswer = getValidInput('Which number is correct?', int)

        return userAnswer - 1

    # Informs the user they are correct
    def showCorrect(self):
        self.clear()
        print 'Correct!'
        time.sleep(2)


    # Informs the user they are wrong
    def showWrong(self):
        self.clear()
        print 'Wrong!'
        time.sleep(2)
    
    # Shows the current score of the game
    # scoreDict should by a dictionary with ('numRight': Int) and ('numWrong': int)
    def showScore(self, scoreDict):
        self.clear()
        print 'Score -- Correct: {}, Incorrect: {}\n\n'.format(scoreDict['numRight'], scoreDict['numWrong'])
        time.sleep(2)

    def showEnd(self, info):
        self.showScore(info)

        gretting = 'Good work, {0}. You know who you are following!'.format(info['playerName'])
        if info['numRight'] < info['numWrong']:
            gretting = 'Better luck next time, {0}. Maybe get to know who you are following!'.format(info['playerName'])

        print gretting
        print 'See you later!'
    

    # Clears the console
    # Works for Mac and Linux, not Windows
    def clear(self):
        os.system('clear')
