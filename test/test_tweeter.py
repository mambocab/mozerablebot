from pytest import fixture, raises
from tweeter import Tweeter
from badwords import ContainsBadWordException
from unittest.mock import Mock

@fixture
def mock_client():
    return Mock()

def test_clean_status_is_tweeted(mock_client):
    t = Tweeter(mock_client)
    s = 'this is an ok status!'
    t.tweet(s)
    mock_client.update_status.assert_called_with(s)

def test_bad_status_not_tweeted(mock_client):
    t = Tweeter(mock_client)
    s = 'this status contains the word mustard.'
    with raises(ContainsBadWordException):
        t.tweet(s)
    assert not mock_client.update_status.called
