from pytest import fixture, raises
from tweeter import Tweeter
from badwords import ContainsBadWordException
from unittest.mock import Mock


@fixture
def mock_client():
    return Mock()


def get_client_tweet_method(client):
    '''
    Getter for the method that should be called when the Twitter client tries
    to tweet. Provides a single point of failure when client API changes.
    Actual client currently uses Tweepy, so the method's name is
    update_status.
    '''
    return client.update_status


def assert_tweeted(client, s):
    '''
    Asserts that client's method for tweeting things was called with s.
    Provides a single point of failure for when the client's API changes.
    Actual client currently uses Tweepy, so the method takes a keyword
    argument called status
    '''
    get_client_tweet_method(client).assert_called_with(status=s)


def test_clean_status_is_tweeted(mock_client):
    t = Tweeter(mock_client)
    s = 'this is an ok status!'
    t.tweet(s)
    assert_tweeted(mock_client, s)


def test_bad_status_not_tweeted(mock_client):
    t = Tweeter(mock_client)
    s = 'this status contains the word mustard.'
    assert not get_client_tweet_method(mock_client).called


def test_bad_status_raises_exception(mock_client):
    t = Tweeter(mock_client)
    s = 'this status contains the word mustard.'
    with raises(ContainsBadWordException):
        t.tweet(s)


def test_bad_status_not_tweeted_case_insensitive(mock_client):
    t = Tweeter(mock_client)
    s = 'this status contains the word sauerkrAut.'
    assert not get_client_tweet_method(mock_client).called
