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


# Contains logic for interacting with the Twitter api and getting questions
class TwitterGame(Game):

    def __init__(self, name):
        Game.__init__(self, name)
        self.friends = API.GetFriends()
        self.tweets = API.GetHomeTimeline()

    # Gets a tweet from the user's twitter home timeline and provides prossible answers for who tweeted
    # the tweet.  Only one answer will be correct.
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


    # Gets a random tweet from the timeline
    def getRandomTweet(self):
        tweet = self.tweets[random.randint(0, len(self.tweets))]
        return tweet

    # Gets random users from the user's friend list
    def getRandomUsers(self, num=4):
        userIndexes = random.sample(xrange(len(self.friends)), num)
        users = [self.friends[i] for i in userIndexes]
        return users

    