from behave import then
from compare import expect


@then(u'I should get a response with status code {status_code:d}')
def step_impl(context, status_code):
    expect(status_code).to_equal(context.response.status_code)
