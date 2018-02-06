from behave import when, then
from compare import expect
from api_core.api_request.api_request_manager import post_put_request, get_delete_request


@when(u'I set this change ')
def step_impl(context):
    params = {}
    for row in context.table:
        params['username'] = row['username']
        params['password'] = row['password']
        params['deleteLockTime'] = 10
    context.credentials = None
    context.data = params


@then(u'The response should equals that Get method')
def step_impl(context):
    mapa = get_delete_request(context.base_url, "/services", "GET", None, None, None).json()
    for dictonary in mapa:
        if(context.item_id == dictonary['_id']):
            expect(context.data['username']).to_equal(dictonary['username'])
            break