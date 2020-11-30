import urllib.parse


def make_url(settings):
    """
    docstring
    """
    if type(settings) is str:
        return settings
    elif type(settings) is dict:
        user = settings.get("user")
        password = settings.get("password")
        if user and password:
            user = urllib.parse.quote(user)
            password = urllib.parse.quote(password)
            up = f"{user}:{password}@"
        else:
            up = ""
        host = settings.get("host") or "localhost"
        port = settings.get("port") or 27017
        params = settings.get("params") or {"authMechanism": "DEFAULT"}
        # params = settings.get("params") or {}
        params = urllib.parse.urlencode(params)
        url = f"mongodb://{up}{host}:{port}/?{params}"
    else:
        raise TypeError(f"argument must be a string or a dict, not {type(settings)}")
    return url


methods = [
    "_BaseObject__codec_options",
    "_BaseObject__read_concern",
    "_BaseObject__read_preference",
    "_BaseObject__write_concern",
    "_Collection__create",
    "_Collection__create_indexes",
    "_Collection__database",
    "_Collection__find_and_modify",
    "_Collection__full_name",
    "_Collection__name",
    "_Collection__write_response_codec_options",
    "__call__",
    "__class__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattr__",
    "__getattribute__",
    "__getitem__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__iter__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__next__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
    "_aggregate",
    "_aggregate_one_result",
    "_command",
    "_count",
    "_delete",
    "_delete_retryable",
    "_insert",
    "_insert_one",
    "_legacy_write",
    "_map_reduce",
    "_read_preference_for",
    "_socket_for_reads",
    "_socket_for_writes",
    "_update",
    "_update_retryable",
    "_write_concern_for",
    "_write_concern_for_cmd",
    "aggregate",
    "aggregate_raw_batches",
    "bulk_write",
    "codec_options",
    "count",
    "count_documents",
    "create_index",
    "create_indexes",
    "database",
    "delete_many",
    "delete_one",
    "distinct",
    "drop",
    "drop_index",
    "drop_indexes",
    "ensure_index",
    "estimated_document_count",
    "find",
    "find_and_modify",
    "find_one",
    "find_one_and_delete",
    "find_one_and_replace",
    "find_one_and_update",
    "find_raw_batches",
    "full_name",
    "group",
    "index_information",
    "initialize_ordered_bulk_op",
    "initialize_unordered_bulk_op",
    "inline_map_reduce",
    "insert",
    "insert_many",
    "insert_one",
    "list_indexes",
    "map_reduce",
    "name",
    "next",
    "options",
    "parallel_scan",
    "read_concern",
    "read_preference",
    "reindex",
    "remove",
    "rename",
    "replace_one",
    "save",
    "update",
    "update_many",
    "update_one",
    "watch",
    "with_options",
    "write_concern",
]
