import requests
import inflect
from secrets import get_secrets_for

wordnik_key = get_secrets_for('wordnik')['WORDNIK_KEY']

inflector = inflect.engine()

def get_singular_noun():
    r = requests.get('http://api.wordnik.com/v4/words.json/randomWord?' +
                     'api_key={}'.format(wordnik_key) +
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
    sing = inflector.singular_noun(noun)
    if sing:
        noun = sing
    return noun
