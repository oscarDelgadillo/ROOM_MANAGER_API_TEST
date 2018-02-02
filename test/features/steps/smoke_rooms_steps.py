# Smoke test: get rooms
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request


@given(u'I have rooms created')
def step_impl(context):
    print()


@when(u'I set the following params')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params['from'] = row['from']
        context.params['to'] = row['to']
        context.params['status'] = row['status']


@when(u'I send the request')
def step_impl(context):
    context.response = get_delete_request(context.base_url, context.endpoint, context.method, None, None,
                                          context.params)
