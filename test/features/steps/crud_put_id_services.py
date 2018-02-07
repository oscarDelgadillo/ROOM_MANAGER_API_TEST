from behave import then, when

from api_core.api_request.api_request_manager import get_request


@when(u'I set this change ')
def step_impl(context):
    params = {}
    for row in context.table:
        params['username'] = context.accounts[row['username']]
        params['password'] = context.accounts[row['password']]
        params['deleteLockTime'] = context.services[row['deleteLockTime']]
    context.data = params
    context.credentials = None











