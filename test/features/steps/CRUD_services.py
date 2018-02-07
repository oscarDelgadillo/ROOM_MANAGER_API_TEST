from behave import when, then, given
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request
from api_core.utils.compare_json import compare_json
from api_core.utils.validate_parameters import validate_parameters1


@when(u'I set with the following params for a services')
def step_impl(context):
    context.data = {}
    for row in context.table:
        context.data['type'] = validate_parameters1(context.services, row['type'])
        context.data['hostname'] = validate_parameters1(context.services, row['hostname'])
        context.data['username'] = validate_parameters1(context.services, row['username'])
        context.data['password'] = validate_parameters1(context.services, row['password'])
        context.data['deleteLockTime'] = int(validate_parameters1(context.services, row['deleteLockTime']))


@then(u'The response should be saved in database in services schema')
def step_impl(context):
    context.item_id = context.response.json()['_id']
    context.data['_id'] = context.item_id
    item = get_delete_request(context.base_url, context.endpoint, 'GET', None, context.item_id, context.params)
    expect(compare_json(context.response.json(), item.json())).to_be_truthy()


@given(u'I have a service created with the following information')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a service created with the following information')


@given(u'I keep the response as $response for later step')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I keep the response as $response for later step')


@when(u'I GET /service')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I GET /service')
