from behave import then, step
from compare import expect

from api_core.api_request.api_request_manager import get_delete_request, get_request
from api_core.utils.compare_json import compare_json


@then(u'I should get a response with status code {status_code:d}')
def step_impl(context, status_code):
    expect(status_code).to_equal(context.response.status_code)


@then(u'I should get an empty Json response')
def step_impl(context):
    expected_body = []
    expect(expected_body).to_equal(context.response.json())


@then(u'The response should display service "{message}"')
def step_impl(context, message):
    print('carajo',context.response.json())
    print(context.endpoint)
    print(context.method)
    expect(context.response.json()['name']).to_equal(message)


@then(u'The answer should be the same as the answer Get method')
def step_impl(context):
    item = get_request(context.base_url, context.endpoint, None, None)
    expect(compare_json(context.response.json(), item.json())).to_be_truthy()













@step(u'I keep the data changed as "{__data_changed}"')
def step_impl(context,__data_changed):
    context.item_ids[__data_changed] = context.data

@then(u'I save the json response got from get services as "{__new_data}"')
def step_impl(context,__new_data):
    context.item_ids[__new_data] = get_request(context.base_url, "/services", None, None)



@then(u'I compare json response "{__data_changed}" between "{__new_data}"')
def step_impl(context,__data_changed,__new_data):
    expect(context.response.json()['_id']).to_equal(context.item_ids[__new_data].json()[1]['_id'])
    expect(context.item_ids[__data_changed]['username']).to_equal(context.item_ids[__new_data].json()[1]['username'])

