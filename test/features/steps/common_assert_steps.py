from behave import then
from compare import expect
from pprint import pprint

from api_core.api_request.api_request_manager import get_delete_request, get_request
from api_core.utils.compare_json import compare_json


@then(u'I should get a response with status code {status_code:d}')
def step_impl(context, status_code):
    expect(status_code).to_equal(context.response.status_code)


@then(u'I should get an empty Json response')
def step_impl(context):
    expected_body = []
    print('Expected body', expected_body)
    print('Actual body:')
    pprint(context.response.json())
    expect(expected_body).to_equal(context.response.json())


@then(u'The response should said service "{message}"')
def step_impl(context, message):
    responce = get_request(context.base_url, context.endpoint, None, None)
    expect(responce.json()['name']).to_equal(message)


@then(u'The answer should be the same as the answer Get method')
def step_impl(context):
    item = get_request(context.base_url, context.endpoint, None, None)
    expect(compare_json(context.response.json(), item.json())).to_be_truthy()
