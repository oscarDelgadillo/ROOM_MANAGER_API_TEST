from api_core.api_request.api_request_manager import get_delete_request

@when(u'I set the hostname of the server "{hostname}"')
def step_impl(context,hostname):
    context.params = {'hostname':hostname}
    response = get_delete_request(context.base_url, context.endpoint, context.method, None, None,context.params)
    arrayId = response.text.split(",")
    id = arrayId[0].split(':')
    context.item_id = str(id[1]).replace('"',' ')



