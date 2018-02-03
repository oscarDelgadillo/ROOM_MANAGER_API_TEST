from behave import then
from compare import expect
from pprint import pprint


@then(u'I should get a response with status code {status_code:d}')
def step_impl(context, status_code):
    print('Status Code:', context.response.status_code)
    expect(status_code).to_equal(context.response.status_code)


@then(u'I should get an empty Json response')
def step_impl(context):
    expected_body = []
    print('Expected body', expected_body)
    print('Actual body:')
    pprint(context.response.json())
    expect(expected_body).to_equal(context.response.json())
