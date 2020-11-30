import pytest
from moncoll import Moncoll

settings = {"user": "testuser", "password": "testpass", "dbname": "db_test"}
coll_name = "test_collection"


@pytest.fixture(scope="module", autouse=True)
def setup_paths():
    # test start
    # Before hook
    ins = Moncoll(settings, coll_name)
    ins.drop()
    # Before hook end
    yield ()
    # after hook
    # test end