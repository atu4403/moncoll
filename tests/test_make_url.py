import pytest
from moncoll.util import make_url as fn


def test_str():
    assert fn("test_url") == "test_url"


def test_dict():
    d = {"user": "myuser", "password": "mypassword"}
    assert fn(d) == "mongodb://myuser:mypassword@localhost:27017/?authMechanism=DEFAULT"


def test_other_type():
    with pytest.raises(TypeError) as e:
        # print(str(e.type))
        fn(1)
    assert "argument must be a string or a dict, not <class 'int'>" in str(e)
