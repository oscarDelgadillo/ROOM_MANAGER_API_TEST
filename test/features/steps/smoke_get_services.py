from api_core.api_request.api_request_manager import get_delete_request


@when(u'I set the following params ')
def step_impl(context):
    context.param = {}
    for row in context.table:
        context.param["hostname"] = row["hostname"]
        context.param["name"] = row["name"]
        context.param["type"] = row["type"]
        context.param["version"] = row["version"]
    context.response = get_delete_request(context.base_url, context.endpoint, context.method, None, None, context.param)
    context.status = context.response.status_code
