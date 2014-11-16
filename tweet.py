import inflect
from tweeter import Tweeter
from wordnikclient import get_singular_noun
from twitterclient import get_client
from badwords import ContainsBadWordException

tweeter = Tweeter(get_client('mozerablebot'))
inflector = inflect.engine()

# get a random noun that isn't a word of oppression

posted = False

while not posted:
    status = "I was looking for {n}, and then I found {n}\nand Heaven knows I'm miserable now".format(n=inflector.a(get_singular_noun()))
    try:
        tweeter.tweet(status)
        posted = True
    except ContainsBadWordException:
        pass
