import os
import twitter
import random
from game import Game

# Seed the random number generator
random.seed()

# set up authentication so we can do the needed api calls
config = os.environ
API = twitter.Api(consumer_key=config['consumerKey'],
                    consumer_secret=config['consumerSecret'],
                    access_token_key=config['accessToken'],
                    access_token_secret=config['accessTokenSecret'])


class TwitterGame(Game):

    def __init__(self, name):
        Game.__init__(self, name)
        self.friends = API.GetFriends()
        self.tweets = API.GetHomeTimeline()

    def getQuestionAndAnswers(self, numAnswers=4):
        tweet = self.getRandomTweet()

        answers = self.getRandomUsers(numAnswers - 1)
        answerIds = [user.id for user in answers]

        # Make sure one of the possible answers is not the true answer
        # If it is, just get new indexes
        correctUserId = tweet.user.id
        while correctUserId in answerIds:
            answers = self.getRandomUsers(numAnswers - 1)
            answerIds = [user.id for user in answers]

        # Add the correct user to the list at a random location
        correctIndex = random.randint(0, numAnswers)
        answersText = [user.name for user in answers]
        answersText.insert(correctIndex, tweet.user.name)

        return {
            'question': tweet.text,
            'answers': answersText,
            'correctIndex': correctIndex
        }


    def getRandomTweet(self):
        tweet = self.tweets[random.randint(0, len(self.tweets))]
        return tweet


    def getRandomUsers(self, num=4):
        userIndexes = random.sample(xrange(len(self.friends)), num)
        users = [self.friends[i] for i in userIndexes]
        return users

    