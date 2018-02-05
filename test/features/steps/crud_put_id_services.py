from behave import when

from api_core.api_request.api_request_manager import post_put_request


@when(u'I set this change ')
def step_impl(context):
    params = {}
    for row in context.table:
        params['username'] = row['username']
        params['password'] = row['password']
        params['deleteLockTime'] = 10

    context.credentials = None
    context.data = params

