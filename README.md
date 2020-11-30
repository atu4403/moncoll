# moncoll
Wrapper for mongodb-collection class

## install

```
pip install moncoll
```

## useit

```python
from moncoll import Moncoll

settings = {"user": "testuser", "password": "testpass", "dbname": "db_test"}
coll_name = "test_collection"

coll = Moncoll(settings, coll_name)
coll.insert_one({"_id": 123})
coll.insert_one({"_id": 456})
res = coll.find()
print(res) # => [{"_id": 123}, {"_id": 456}]
coll.drop()
```

## api

[collection – Collection level operations — PyMongo documentation](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html)

Please refer to here. But there are some differences.

1. "find" and "aggregate" return a list instead of a cursor

## Related
- [mongodb/mongo\-python\-driver: PyMongo \- the Python driver for MongoDB](https://github.com/mongodb/mongo-python-driver)


## License

MIT © [atu4403](https://github.com/atu4403)