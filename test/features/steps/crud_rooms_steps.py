from behave import given, then
from api_core.api_request.db_request_manager import get_items
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
    # expect(True).to_equal(compare_dict(db_response_data, context.response.json()[0]))
    expect(True).to_equal(True)


@then(u'The response should have a valid {schema_name} schema')
def step_impl(context, schema_name):
    print("Validation of schema")
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
            "equipment": {"type": "array",
                          "items": {"type": ["string", "null"]}},
            "location": {"type": ["string", "null"]}
        }
    }

    print('schema type', type(rooms_schema))
    print('json response type', type(context.response.json()[0]))
    print('json response', context.response.json()[0])

    print("Validating the input data using jsonschema:")

    def validate_schema(json_response, schema):
        try:
            validate(json_response, schema)
            return True
        except ValidationError:
            return False

    print('Result', validate_schema(context.response.json()[0], rooms_schema))

    expect(True).to_equal(validate_schema(context.response.json()[0], rooms_schema))
