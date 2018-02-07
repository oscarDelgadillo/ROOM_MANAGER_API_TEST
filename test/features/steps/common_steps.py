from behave import step
from api_core.api_request.api_request_manager import request


@step(u'I {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    context.endpoint = endpoint


@step(u'I set {credentials} as credentials')
def step_impl(context, credentials):
    context.credentials = credentials


@step(u'I send the request')
def step_impl(context):
    context.response = request(context.base_url, context.endpoint, context.method, context.credentials, context.item_id,
                               context.data, context.params)


@step(u'I keep the "id" as "after_item_id" from JSON response')
def step_impl(context):
    context.after_item_id = context.response.json()['_id']
