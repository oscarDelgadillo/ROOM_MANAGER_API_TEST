from behave import when, then, given, step
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request
from api_core.utils.compare_json import compare_json
from api_core.utils.validate_parameters import validate_parameters1


@step(u'I set with the following params for a services')
def step_impl(context):
    context.data = {}
    for row in context.table:
        context.data['type'] = validate_parameters1(context.services, row['type'])
        context.data['hostname'] = validate_parameters1(context.services, row['hostname'])
        context.data['username'] = validate_parameters1(context.services, row['username'])
        context.data['password'] = validate_parameters1(context.services, row['password'])
        context.data['deleteLockTime'] = int(validate_parameters1(context.services, row['deleteLockTime']))


@step(u'The response should be saved in database in services schema')
def step_impl(context):
    context.after_item_id = context.response.json()['_id']
    context.data['_id'] = context.after_item_id
    item = get_delete_request(context.base_url, context.endpoint, 'GET', None, context.after_item_id, context.params)
    expect(compare_json(context.response.json(), item.json())).to_be_truthy()


@step(u'I keep the response as "{new_response}" from the previous step')
def step_impl(context, new_response):
    context.responses[new_response] = context.response


@step(u'The response "{actual_response}" should be equal to response "{expected_response}"')
# @then(u'It should be equal "{actual_response}" and "{expected_response}"')
def step_impl(context, actual_response, expected_response):
    expect(compare_json(context.responses[actual_response].json(),
                        context.responses[expected_response].json())).to_be_truthy()


@given(u'I have a service created with the following data')
def step_impl(context):
    context.execute_steps('''
        When I POST to /services
            And I set with the following params for a services
                | type          | hostname   | username             | password                 | deleteLockTime     |
                | __TYPE_SERVER | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __DELETE_LOCK_TIME |
            And I send the request
    ''')
    context.after_item_id = context.response.json()['_id']


@step(u'The response "_expected_response" should be equal to database service schema')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The response "_get_response" should be equal to database service schema')


@then(u'this catch')
def step_impl(context):
    print('++++++++++++++++++')
    # print('id', context.item_ids['__ServId'])
    # print('res', context.responses['_get_response'].json())
    print('code:', context.response.status_code)
    expect(False).to_be_truthy()
