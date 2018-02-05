
from behave import when, step

from api_core.api_request.api_request_manager import get_delete_request, post_put_request


@step(u'Given I have a Service Created with this data')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["type"] = row["type"]
        context.params["hostname"] = row["hostname"]
        context.params["username"] = row["username"]
        context.params["password"] = row["password"]
        context.params["deleteLockTime"] = 10
    response = post_put_request(context.base_url, "/services", 'POST', None, None, context.params)
    context.item_id = response.json()['_id']


@step(u'I set {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    context.endpoint = endpoint
    print(context.method)
    print(context.endpoint)


@step(u'I set {credentials} as credentials')
def step_impl(context, credentials):
    context.credentials = credentials


@step(u'I send the request')
def step_impl(context):
    context.response = get_delete_request(context.base_url, context.endpoint, context.method, context.credentials,
                                          context.item_id,
                                          context.params)
