from behave import given, then
from api_core.api_request.api_request_manager import post_put_request
from api_core.api_request.db_request_manager import get_items
from bson.objectid import ObjectId

from pprint import pprint
from compare import expect

from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json


@given(u'I have a meeting {method} to {endpoint} with the following info')
def step_impl(context, endpoint, method):
    context.data = {}
    for row in context.table:
        context.data['organizer'] = row['organizer']
        context.data['subject'] = row['subject']
        context.data['body'] = row['body']
        context.data['start'] = row['start']
        context.data['end'] = row['end']
        context.data['rooms'] = [row['rooms']]
        context.data['attendees'] = [row['attendees']]
        context.data['optionalAttendees'] = [row['optionalAttendees']]

    context.method = method
    context.endpoint = endpoint
    context.after_endpoint = context.endpoint

    # Creating meeting
    context.response = post_put_request(context.base_url, context.endpoint, context.method, context.credentials, None,
                                        context.data)
    print("POST Response Status Code:", context.response.status_code)
    print(type(context.response.json()))

    context.after_item_id = context.response.json()["_id"]
    context.after_credentials = context.credentials
    context.credentials = None

    # Getting room from database
    context.room = context.response.json()['rooms'][0]
    print("Rooms:", context.room)


@then(u'I should get a Json response with the following info')
def step_impl(context):
    print("Validation of data")
    context.data = {}
    for row in context.table:
        context.data['name'] = row['name']
        context.data['displayName'] = row['displayName']
        context.data['email'] = row['email']
        context.data['code'] = row['code']
        context.data['capacity'] = int(row['capacity'])
        context.data['service'] = ObjectId(row['service'])
        context.data['equipment'] = row['equipment']
        context.data['location'] = row['location']

    # pprint(context.data)

    request = {'email': context.room}
    context.expected_data = get_items(context.rm_host, context.rm_db_port, context.database, 'rooms', request,
                                      context.return_data)

    print("Result of query = Room:")
    print(type(context.expected_data))
    for doc in context.expected_data:
        pprint(doc)

        # Todo Add Validation of Json Data

        # expect('10').to_equal(1)


@then(u'I should get a Json response with the following schema')
def step_impl(context):
    print("Validation of schema")
    schema = {
        'type': 'array',
        'properties': {
            'uuid': {'type': 'string'},
            'name': {'type': 'string'},
            'displayName': {'type': 'string'},
            'email': {'type': 'string'},
            'code': {'type': 'string'},
            'capacity': {'type': 'number'},
            'roomStatus': {'type': 'string'},
            'equipment': {'type': 'array',
                          'items': {'type': 'string'}},
            'location': {'type': 'string'}
        }
    }

    print(type(schema))

    print("Validating the input data using jsonschema:")
    try:
        print('Entering in Try')
        validate(context.expected_data, schema)
        print('True')
    except ValidationError:
        print('Entering in except')
        print('False')

    expect('10').to_equal(1)
