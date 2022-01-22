from tweepy import StreamListener
import json


class TweetStream(StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, status):
        print('Tweet text: ' + status.text)
        self.reply_tweet('Hello @{}, really happy to hear from you'.format(status.user.screen_name), status.id_str)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

    def reply_tweet(self, msg, t_id):
        self.api.update_status(msg, t_id)
