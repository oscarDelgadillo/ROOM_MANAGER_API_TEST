# Smoke test: get rooms
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request


@given(u'I have rooms created')
def step_impl(context):
    print()


@when(u'I {method} to {end_point} for rooms with the following info')
def step_impl(context, method, end_point):
    context.end_point = end_point
    context.method = method
    context.params = {}
    for row in context.table:
        context.params['from'] = row['from']
        context.params['to'] = row['to']
        context.params['status'] = row['status']

    context.response = get_delete_request(context.base_url, context.end_point, context.method, None, None,
                                          context.params)


@then(u'I should get a response with status code {status_code:d}')
def step_impl(context, status_code):
    print('Status Code:', context.response.status_code)
    expect(context.response.status_code).to_equal(status_code)
