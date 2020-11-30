import pytest
from moncoll import Moncoll, BulkItemNotIdError
from pymongo import UpdateOne

fn = Moncoll.to_bulklist


def test_not_id():
    li = [{"name": "Karin", "gender": "female"}, {"name": "Decker", "gender": "male"}]
    assert fn(li, "name") == [
        UpdateOne(
            {"_id": "Karin"},
            {"$set": {"name": "Karin", "gender": "female", "_id": "Karin"}},
            True,
            None,
            None,
            None,
        ),
        UpdateOne(
            {"_id": "Decker"},
            {"$set": {"name": "Decker", "gender": "male", "_id": "Decker"}},
            True,
            None,
            None,
            None,
        ),
    ]


def test_with_id():
    data = [
        {"_id": "5fc3af959f9e4b17a00d15f5", "name": "Mosley", "gender": "male"},
        {"_id": "5fc3af9584542f2b3fb85bdf", "name": "Kelly", "gender": "male"},
    ]
    assert fn(data) == [
        UpdateOne(
            {"_id": "5fc3af959f9e4b17a00d15f5"},
            {
                "$set": {
                    "_id": "5fc3af959f9e4b17a00d15f5",
                    "name": "Mosley",
                    "gender": "male",
                }
            },
            True,
            None,
            None,
            None,
        ),
        UpdateOne(
            {"_id": "5fc3af9584542f2b3fb85bdf"},
            {
                "$set": {
                    "_id": "5fc3af9584542f2b3fb85bdf",
                    "name": "Kelly",
                    "gender": "male",
                }
            },
            True,
            None,
            None,
            None,
        ),
    ]


def test_noy_id():
    li = [{"name": "Karin", "gender": "female"}, {"name": "Decker", "gender": "male"}]
    with pytest.raises(BulkItemNotIdError) as e:
        fn(li)
    assert "_id property does not exist: {'name': 'Karin', 'gender': 'female'}" in str(
        e
    )
