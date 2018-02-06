from behave import when

from api_core.api_request.api_request_manager import get_delete_request

@when(u'I set the hostname of the server "__exchange_server"')
def step_impl(context):
    context.params ={'hostname': context.__exchange_server}
    response = get_delete_request(context.base_url, context.endpoint, context.method, None, None,context.params)
    context.item_id = response.json()[0]['_id']


