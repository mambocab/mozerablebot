from badwords import contains_badword, ContainsBadWordException

class Tweeter():
    def __init__(self, client):
        self._client = client

    def tweet(self, s):
        if contains_badword(s):
            raise ContainsBadWordException("{} contains a bad word".format(s))
        else:
            self._client.update_status(status=s)
