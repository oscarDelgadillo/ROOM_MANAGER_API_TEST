# CRUD test: get rooms
from behave import then
from api_core.api_request.db_request_manager import to_json
from api_core.api_request.db_request_manager import get_items
from api_core.api_request.api_request_manager import request
from api_core.utils.compare_json import compare_json, extract_item
from api_core.utils.compare_json import json_contains
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from compare import expect
import json


@then(u'I should get a collection with only free {collection}')
def step_impl(context, collection):
    database_request = {}
    database_request['email'] = context.data[collection][0]

    context.request = get_items(context.rm_host, context.rm_db_port, context.database, collection,
                                database_request,
                                None)
    context.item_id = context.request[0]['_id']  # Should disappear
    item_response = request(context.base_url, context.endpoint, context.method,
                            context.credentials, context.item_id,
                            context.data, context.params)

    expect(False).to_equal(json_contains(item_response.json(), context.response.json()))


@then(u'The response should be equal in data base {collection} collection')
def step_impl(context, collection):
    database_request = {}
    database_request['email'] = context.data[collection][0]

    context.request = get_items(context.rm_host, context.rm_db_port, context.database, collection,
                                database_request,
                                None)

    expect(True).to_equal(compare_json(to_json(context.request), extract_item(context.response.json())))


@then(u'The response should have a valid {schema_name} schema')
def step_impl(context, schema_name):
    context.schema_name = json.loads(open('test/schemes/' + schema_name + '.json.').read())

    def validate_schema(json_response, schema):
        try:
            validate(json_response, schema)
            return True
        except ValidationError:
            return False

    expect(True).to_equal(validate_schema(extract_item(context.response.json()), context.schema_name))
