import tweepy
from configs.Config import keys
from tweeter.tweet_stream import TweetStream


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
    user = api.me()
    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.friends_count))
    twts = api.search(q="Hello World!")
    for tweet in twts:
        print("user [{}] tweeted [{}]".format(tweet.user.screen_name, tweet.text))


def run_bot():
    auth = init_bot()
    api = tweepy.API(auth)
    listener = TweetStream(api)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=["@phagoton"])

    pass


if __name__ == '__main__':
    run_bot()

