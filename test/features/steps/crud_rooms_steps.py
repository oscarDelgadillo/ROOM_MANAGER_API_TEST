from behave import given, then
from api_core.api_request.db_request_manager import get_items
from api_core.api_request.api_request_manager import request
from api_core.utils.compare_json import compare_json
from api_core.utils.compare_json import json_contains
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from compare import expect


@given(u'I set the following meeting info')
def step_impl(context):
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


@then(u'I should not get {schema} occupied by the meeting created')
def step_impl(context, schema):
    database_request = {}
    context.schema = schema
    database_request['email'] = context.data[schema][0]
    context.request = get_items(context.rm_host, context.rm_db_port, context.database, context.schema, database_request,
                                None)
    db_response_data = {}
    for doc in context.request:
        db_response_data.update(doc)
    context.item_id = db_response_data['_id']

    context.item_response = request(context.base_url, context.endpoint, context.method,
                                    context.credentials, context.item_id,
                                    context.data, context.params)

    expect(False).to_equal(json_contains(context.item_response.json(), context.response.json()))


@then(u'The response should be equal in data base {schema} schema')
def step_impl(context, schema):
    database_request = {}
    context.schema = schema
    database_request['email'] = context.data[schema][0]
    context.request = get_items(context.rm_host, context.rm_db_port, context.database, context.schema, database_request,
                                None)
    db_response_data = {}
    for doc in context.request:
        db_response_data.update(doc)

    try:
        expect(True).to_equal(compare_json(db_response_data, context.response.json()[0]))
    except KeyError:
        expect(True).to_equal(compare_json(db_response_data, context.response.json()))
    except IndexError:
        expect(True).to_equal(compare_json(db_response_data, context.response.json()))


@then(u'The response should have a valid {schema_name} schema')
def step_impl(context, schema_name):
    rooms_schema = {
        "type": "object",
        "properties": {
            "uuid": {"type": "string"},
            "name": {"type": "string"},
            "displayName": {"type": "string"},
            "email": {"type": "string"},
            "code": {"type": "string"},
            "capacity": {"type": "number"},
            "roomStatus": {"type": "string"},
            "equipment": {"type": ["string", "null"]},
            "location": {"type": ["string", "null"]}
        }
    }

    def validate_schema(json_response, schema):
        try:
            validate(json_response, schema)
            return True
        except ValidationError:
            return False

    try:
        expect(True).to_equal(validate_schema(context.response.json()[0], rooms_schema))
    except KeyError:
        expect(True).to_equal(validate_schema(context.response.json(), rooms_schema))
    except IndexError:
        expect(True).to_equal(validate_schema(context.response.json(), rooms_schema))
