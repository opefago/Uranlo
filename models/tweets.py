from bson import ObjectId
from models import mongo_connection
import logging as log
collection = "tweets"


class TweetObject:
    def __init__(self, text, sentiment):
        self.id = id;
        self.text = text
        self.sentiment = sentiment
    def to_document(self):
        return {
            'text': self.text,
            'sentiment': self.sentiment
        }
    @staticmethod
    def cursor_to_document(cursor):
        return {
            "_id": cursor['_id'],
            "text": cursor["text"],
            "sentiment": cursor["sentiment"]
        }


class TweetStore:
    def __init__(self, collection_name):
        self.collection = mongo_connection()[collection_name]
        pass

    def insert_one(self, text, sentiment):
        try:
            job_object = TweetObject(text, sentiment).to_document()
            result = self.collection.insert_one(job_object)
            log.info('One post: {0}'.format(result.inserted_id))
            return job_object
        except Exception as e:
            log.info('Could not create new tweet: [{}]'.format(e))
            return None

    def find_by_id(self, tweet_id):
        try:
            cursor = self.collection.find_one({'_id': ObjectId(tweet_id)})
            job_found = TweetObject.cursor_to_document(cursor)
            log.info("Found tweet: [{}]".format(job_found))
            return job_found
        except Exception as e:
            log.info("could not find tweet: [{}]".format(e))
            return None

    def update(self, id, text, sentiment):
        try:
            self.collection.update({'_id': id}, {
                '$set': {'sentiment': sentiment}
            })
            return TweetObject(text, sentiment).to_document()
        except Exception as e:
            log.info("Error updating: [{}]".format(e))

    def find_all_jobs(self):
        jobs = self.collection.find({})
        all_tweets = list(map(lambda job: TweetObject.cursor_to_document(job), jobs))
        log.info("All job information: [{}]".format(all_tweets))
        return all_tweets
