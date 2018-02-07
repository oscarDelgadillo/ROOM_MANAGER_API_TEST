from behave import step
from api_core.api_request.api_request_manager import request


@step(u'I {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    aux_endpoint = str(endpoint).split('/')
    if aux_endpoint.__len__() == 3:
        context.endpoint = '/{}/{}'.format(aux_endpoint[1], context.item_ids[aux_endpoint[2]])
        return
    context.endpoint = endpoint


@step(u'I set {credentials} as credentials')
def step_impl(context, credentials):
    context.credentials = credentials


@step(u'I send the request')
def step_impl(context):
    context.response = request(context.base_url, context.endpoint, context.method, context.credentials, context.item_id,
                               context.data, context.params)
    context.status_code = context.response.status_code


@step(u'I keep service_id as {__id}')
def step_impl(context, __id):
    context.item_ids[__id] = context.response.json()['_id']


@step(u'Given I have a Service Created with this data')
def step_impl(context):
    context.data = {}
    for row in context.table:
        context.data["type"] = context.environment_variables[row['type']]
        context.data["hostname"] = context.environment_variables[row['hostname']]
        context.data["username"] = context.accounts[row['username']]
        context.data["password"] = context.accounts[row['password']]
        context.data["deleteLockTime"] = context.environment_variables[row['deleteLockTime']]
    context.response = request(context.base_url, "/services", 'POST', None, None, context.data, context.params)

    
@step(u'I keep the "id" as "after_item_id" from JSON response')
def step_impl(context):
    context.after_item_id = context.response.json()['_id']

    