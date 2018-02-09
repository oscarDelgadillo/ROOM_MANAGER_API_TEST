from behave import then, given, step
from bson import ObjectId
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request
from api_core.api_request.db_request_manager import get_items, to_array_json
from api_core.utils.common_functions import return_json_from_array
from api_core.utils.compare_json import compare_json, equivalence_json
from api_core.utils.validate_parameters import validate_parameters1
from api_core.utils.validate_schemes_json import validate_schema


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


@then(u'The response "{_actual_response}" should be contain in database {collection} collection')
def step_impl(context, actual_response, collection):
    database_request = {}
    database_request['_id'] = ObjectId(context.after_item_id)
    context.request = get_items(context.rm_host, context.rm_db_port, context.database, collection, database_request,
                                None)
    db_json = return_json_from_array(context.after_item_id, context.responses[actual_response].json())
    json_compare = to_array_json(context.request)[0]
    expect(equivalence_json(db_json, json_compare)).to_be_truthy()

