from behave import when

from api_core.api_request.api_request_manager import post_put_request


@when(u'I set this change ')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params['username'] = row['username']
        context.params['password'] = row['password']
        context.params['deleteLockTime'] = 10

    print(context.params)
    print(context.endpoint)
    print(context.method)
    print(context.base_url)
    # context.response = post_put_request(context.base_url, context.endpoint, context.method, None, context.item_id,context.params)
    # context.status = context.response.status_code
