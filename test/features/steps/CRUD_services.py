import operator
import json
from pprint import pprint

import requests
from behave import when, then
from compare import expect

from api_core.api_request.api_request_manager import request
from api_core.api_request.db_request_manager import get_item_by_id, get_items


@when(u'I set with the following params')
def step_impl(context):
    context.data = {}
    for row in context.table:
        context.data['type'] = row['type']
        context.data['hostname'] = row['hostname']
        context.data['username'] = row['username']
        context.data['password'] = row['password']
        context.data['deleteLockTime'] = int(row['deleteLockTime'])


@then(u'I validate that the service was successful saved')
def step_impl(context):
    jjson = context.response.json()
    id_response = jjson['_id']
    context.data['_id'] = id_response

    item = get_item_by_id(context.rm_host, context.rm_db_port, context.database, 'services', id_response, None)
    context.item_id = item["_id"]
    temp = {}
    temp['_id'] = item['_id']
    temp['type'] = item['type']
    temp['hostname'] = item['hostname']
    temp['username'] = item['username']
    temp['password'] = item['password']
    temp['deleteLockTime'] = item['deleteLockTime']

    expect(temp == context.data)












    # # resultado = sorted(context.data.items(), key=operator.itemgetter(0))
    # # jjj = json.dump(context.data)
    # print('-----', context.data)
    # print('contex.data:', type(context.data))
    # # print('jjj:', type(jjj))
    #
    #
    #
    # # x = json.loads(resultado)
    # # jsonarray = json.dumps(resultado)
    # # print('J:', jsonarray.json())
    #
    # validate = request(context.base_url, context.endpoint, 'GET', context.credentials, id_response, None, None)
    #
    # print('+++++++++++:', validate.json())
    # print('validate:', type(validate.json()))
    #
    #
    # # a = {'a': 'aaa', 'b': 'bbb'}
    # # b = {'b': 'bbb', 'a': 'aaa', 'c' : 2}
    # # print('A:', type(a))
    # # print('B:', type(b))
    # # print(a == b)
    #
    #
    # print("rm_host:", context.rm_host,)
    # print("rm-db:", context.rm_db_port)
    # print("database:", context.database)
    # print("id:", id_response)
    # item = get_item_by_id(context.rm_host, context.rm_db_port, context.database, 'services', id_response, None)
    # print("Result of query:", item)
    #
    #
    #
    ur = 'http://10.28.133.13:7070/api/v1/services/{}'.format(id_response)
    requests.delete(url=ur)
    #
    # expect(True).to_equal(False)
