from twython import Twython
from secrets import get_secrets_for

def get_client(username):
    twitter_secrets = get_secrets_for(username)

    # set up twitter client
    return Twython(twitter_secrets['TWITTER_KEY'],
                   twitter_secrets['TWITTER_SECRET'],
                   twitter_secrets['TWITTER_OAUTH_TOKEN'],
                   twitter_secrets['TWITTER_OAUTH_SECRET'])
