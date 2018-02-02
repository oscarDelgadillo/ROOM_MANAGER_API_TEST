from api_core.api_request.api_request_manager import get_delete_request


@when(u'I set the service ID "{service_id}"')
def step_impl(context, service_id):
    context.serviceId = service_id
    context.response = get_delete_request(context.base_url, context.endpoint, context.method, None, context.serviceId,
                                          None)
    context.status = context.response.status_code
