# Module: db_request_manager
from pymongo import MongoClient
from bson.objectid import ObjectId


def get_item_by_id(host, port, data_base_name, schema, obj_id, return_data):
    """This method performs request to the data base by ObjectId.
    params:
        @host: server direction
        @port: data base port
        @data_base_name: name of the data base
        @schema: data base schema (collections)
        @obj_id: obj_id of item
        @return_data: dictionary with params to return
            example {'displayName': 1, 'email': 1}.
            '1' means this param will be part of the response"""

    client = MongoClient(host, port)
    data_base = client[data_base_name]
    if return_data is not None:
        result = data_base[schema].find_one(ObjectId(obj_id), return_data)
    else:
        result = data_base[schema].find_one(ObjectId(obj_id))
    return result


def get_items(host, port, data_base_name, schema, request, return_data):
    """This method performs request to the data base.
        params:
            @host: server direction
            @port: data base port
            @data_base_name: name of the data base
            @schema: data base schema (collections)
            @request: dictionary with params which values are used to match
                the query sent.
                example {'name': 'Room01'}.
            @obj_id: obj_id of item
            @return_data: dictionary with params to return
                example {'displayName': 1, 'email': 1}.
                '1' means this param will be part of the response"""

    client = MongoClient(host, port)
    data_base = client[data_base_name]
    if return_data is not None:
        result = data_base[schema].find(request, return_data)
    else:
        result = data_base[schema].find(request)
    return result


def to_json(request):
    """This method performs conversion of database response Cursor to Json.
            params:
                @request: A Cursor object
                """
    result = {}
    for doc in request:
        print(doc)
        result.update(doc)
    return result

def to_array_json(request):
    """This method performs conversion of database response Cursor to Json.
                params:
                    @request: A Cursor object
                    """
    result = []
    for doc in request:
        result.append(doc)
    return result
