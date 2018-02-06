import requests
from behave import when, then
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request
from api_core.utils.compare_json import compare_json


@when(u'I set with the following params')
def step_impl(context):
    context.data = {}
    context.data['type'] = context.__type_server
    context.data['hostname'] = context.__hostname
    context.data['username'] = context.__user_administrator
    context.data['password'] = context.__password_administrator
    context.data['deleteLockTime'] = context.__deleteLockTime


@then(u'The response should be saved in database in {services} schema')
def step_impl(context, services):
    jjson = context.response.json()
    id_response = jjson['_id']
    context.data['_id'] = id_response

    item = get_delete_request(context.base_url, context.endpoint, 'GET', None, id_response, context.params)

    ur = 'http://10.28.133.13:7070/api/v1/services/{}'.format(id_response)
    requests.delete(url=ur)

    expect(compare_json(context.response.json(), item.json())).to_be_truthy()
