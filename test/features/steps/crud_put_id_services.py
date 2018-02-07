from behave import when, then
from compare import expect
from api_core.api_request.api_request_manager import post_put_request, get_delete_request


@when(u'I set this change ')
def step_impl(context):
    params = {}
    for row in context.table:
        params['username'] = context.accounts[row['username']]
        params['password'] = context.accounts[row['password']]
        params['deleteLockTime'] = context.environment_variables['__DELETE_LOCK_TIME']
    context.data = params
    context.credentials = None



@then(u'I keep the data changed as {__data_changed}')
def step_impl(context,__data_changed):
    context.__data_changed = context.data



@then(u'I keep the json response got from get services as __new_data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I keep the json response got from get services as __new_data')

@then(u'I compare json response __data_changer between __new_data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I compare json response __data_changer between __new_data')
