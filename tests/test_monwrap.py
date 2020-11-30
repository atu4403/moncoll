import pymongo
import pytest
from moncoll import Moncoll

settings = {"user": "testuser", "password": "testpass", "dbname": "db_test"}
coll_name = "test_collection"


def test_insert_and_find():
    coll = Moncoll(settings, coll_name)
    coll.insert_one({"_id": 123})
    coll.insert_one({"_id": 456})
    res = coll.find()
    assert res == [{"_id": 123}, {"_id": 456}]
    coll.drop()


def test_bulk_write():
    test_data = [
        {"name": "Christensen", "gender": "male"},
        {"name": "Jefferson", "gender": "male"},
        {"name": "Juliette", "gender": "female"},
        {"name": "Jill", "gender": "female"},
        {"name": "Nancy", "gender": "female"},
    ]
    coll = Moncoll(settings, coll_name)
    bulkdata = Moncoll.to_bulklist(test_data, "name")
    bulk_res = coll.bulk_write(bulkdata)
    assert bulk_res.upserted_count == 5
    # print("bulk_res: ", bulk_res.upserted_count)
    find_res = coll.find({"gender": "male"})
    assert len(find_res) == 2
    assert {"_id": "Jefferson", "name": "Jefferson", "gender": "male"} in find_res
    assert {"_id": "Christensen", "name": "Christensen", "gender": "male"} in find_res
    coll.drop()


# @pytest.mark.dev
def test_aggregate():
    test_data = [
        {"_id": "5fc3b666e172f2f4951a471a", "price": 267, "category": "banana"},
        {"_id": "5fc3b666cba8fbaedbebc508", "price": 136, "category": "apple"},
        {"_id": "5fc3b66629110554e6af893a", "price": 367, "category": "apple"},
        {"_id": "5fc3b6668ab6e2b58aacf6b3", "price": 367, "category": "apple"},
        {"_id": "5fc3b666bcb15d3b1c2a49f6", "price": 396, "category": "banana"},
        {"_id": "5fc3b6665720415b11e4febf", "price": 195, "category": "apple"},
        {"_id": "5fc3b66632a39823a114ff29", "price": 98, "category": "strawberry"},
        {"_id": "5fc3b6667eae905a7cf7ef6f", "price": 285, "category": "strawberry"},
        {"_id": "5fc3b666f2e779c0a56e021b", "price": 200, "category": "strawberry"},
    ]
    coll = Moncoll(settings, coll_name)
    bulkdata = Moncoll.to_bulklist(test_data)
    coll.bulk_write(bulkdata)
    res = coll.aggregate(
        [
            {"$group": {"_id": "$category", "max_price": {"$max": "$price"}}},
            {"$sort": {"max_price": 1}},
        ]
    )
    assert res == [
        {"_id": "strawberry", "max_price": 285},
        {"_id": "apple", "max_price": 367},
        {"_id": "banana", "max_price": 396},
    ]
    coll.drop()