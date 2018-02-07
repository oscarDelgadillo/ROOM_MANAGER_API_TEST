from behave import when

from api_core.api_request.api_request_manager import get_delete_request, request


@when(u'I set the hostname of the server "{__exchange_server}"')
def step_impl(context, __exchange_server):
    context.params = {'hostname': context.services[__exchange_server]}
    response = request(context.base_url, context.endpoint, context.method, context.credentials, context.item_id,
                       context.data, context.params)
    context.item_id = response.json()[0]['_id']
