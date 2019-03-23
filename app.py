import tweepy
from configs.Config import keys
import logging as logger

CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']

def init_bot():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return auth

def demo_bot():
    auth = init_bot()
    api = tweepy.API(auth)
    twts = api.search(q="Hello World!")

    for tweet in twts:
        print("user [{}] tweeted [{}]".format(tweet.user.screen_name, tweet.text))

def run_bot():
    pass


if __name__ == '__main__':
    demo_bot()

