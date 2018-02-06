from behave import when, then
from compare import expect
from api_core.api_request.api_request_manager import post_put_request, get_delete_request


@when(u'I set this change ')
def step_impl(context):
    params = {}
    for row in context.table:
        params['username'] =context.accounts[row['username']]
        params['password'] = context.accounts[row['password']]
        params['deleteLockTime'] = context.__deleteLockTime
    context.data = params
    context.credentials = None


