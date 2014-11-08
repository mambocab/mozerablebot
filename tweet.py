import random

# # only tweet about 5x/day
# if random.random() > 5 / (24 * 60):
#     exit(0)

from badwords import badwords

from twython import Twython

import requests
import inflect

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
noun = None
while noun is None:
    r = requests.get('http://api.wordnik.com/v4/words.json/randomWord?' +
                     'api_key={}'.format(secrets['WORDNIK_KEY']) +
                     '&includePartOfSpeech=noun' +
                     '&excludePartOfSpeech=proper-noun,' +
                     'proper-noun-plural,noun-plural,' +
                     'proper-noun-posessive,noun-posessive,suffix,' +
                     'family-name,idiom,affix'
                     '&maxDictionaryCount=-1' +
                     '&minLength=3&maxCorpusCount=-1' +
                     '&minDictionaryCount=1&maxLength=-1' +
                     '&hasDictionaryDef=True' +
                     '&minCorpusCount=20000')
    noun = r.json()['word']
    # doublecheck for plural nouns
    sing = inflect.engine().singular_noun(noun)
    if sing:
        noun = sing

    if noun.lower() in badwords:
        noun = None

status = "I was looking for a {n}, and then I found a {n}\nand Heaven knows I'm miserable now".format(n=noun)
twitter_api.update_status(status=status)
