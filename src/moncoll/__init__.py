
from pymongo import (
    MongoClient,
    cursor,
    command_cursor,
    # InsertOne,
    UpdateOne,
    # UpdateMany,
    # ReplaceOne,
    # DeleteOne,
    # DeleteMany,
)
from .util import (
    make_url,
    methods,
)


def make_method(self, method_name: str):
    """
    Moncollのコンストラクタで動的に追加する関数を返す
    関数名は.util.methodsから取得
    """

    def _fn(*args):
        with MongoClient(self.url) as client:
            db = client[self.dbname]
            coll = db[self.coll_name]
            fn = getattr(coll, method_name)
            res = fn(*args)
            if type(res) is cursor.Cursor or type(res) is command_cursor.CommandCursor:
                res = list(res)
        return res

    return _fn


class BulkItemNotIdError(Exception):
    """to_bulklistで使用: dict[idname]が存在しない場合に投げる例外"""

    pass


class Moncoll:
    def __init__(self, connect_settings: dict, collection_name: str):
        self.url = make_url(connect_settings)
        self.dbname = connect_settings["dbname"]
        self.coll_name = collection_name
        for method_name in methods:
            if not method_name.startswith("_"):
                setattr(self, method_name, make_method(self, method_name))

    @staticmethod
    def to_bulklist(_list: list, idname: str = "_id") -> list:  # test書いてない
        if not type(_list) is list:
            raise TypeError("must be a list")

        def _fn(_dict: dict):
            if not _dict.get(idname):
                raise BulkItemNotIdError(f"{idname} property does not exist: {_dict}")
            _dict["_id"] = _dict[idname]
            return UpdateOne({"_id": _dict["_id"]}, {"$set": _dict}, upsert=True)

        return list(map(_fn, _list))