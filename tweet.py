from badwords import badwords

from twython import Twython

import requests

import os
import json

# get wordnik and twitter keys from ${OPENSHIFT_DATA_DIR}secrets.json
datadir = os.environ['OPENSHIFT_DATA_DIR']
with open(datadir + 'secrets.json') as secrets_data:
    secrets = json.load(secrets_data)

# set up twitter client
twitter_api = Twython(secrets['TWITTER_KEY'], secrets['TWITTER_SECRET'],
                      secrets['TWITTER_OAUTH_TOKEN'],
                      secrets['TWITTER_OAUTH_SECRET'])

# get a random noun that isn't a word of oppression
wordnik_params = {'hasDictionaryDef': True,
                  'includePartOfSpeech': 'noun',
                  'minCorpusCount': '20000',
                  'maxCorpusCount': -1,
                  'minDictionaryCount': 1,
                  'maxDictionaryCount': -1,
                  'excludePartOfSpeech': 'proper-noun,proper-noun-plural,noun-plural,proper-noun-posessive,noun-posessive,suffix,family-name,idiom,affix',
                  'minLength': 3,
                  'maxLength': -1,
                  'api_key': secrets['WORDNIK_KEY']}
noun = None
while noun is None:
    r = requests.get('http://api.wordnik.com/v4/words.json/randomWord', params=wordnik_params)
    noun = r.json()['word']

    if noun.lower() in badwords:
        noun = None

status = "I was looking for a {n}, and then I found a {n}\nand Heaven knows I'm miserable now".format(n=noun)
twitter_api.update_status(status=status)
