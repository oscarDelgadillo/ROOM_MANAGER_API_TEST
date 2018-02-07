# Smoke test: get rooms
from behave import when, step
from api_core.api_request.api_request_manager import get_delete_request
from api_core.api_request.db_request_manager import get_items


@when(u'I set the following params')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params['from'] = row['from']
        context.params['to'] = row['to']
        context.params['status'] = row['status']


@step(u'I have obtained {schema} Id of the database')
def step_impl(context, schema):
    item_request = get_items(context.rm_host, context.rm_db_port, context.database, schema, None, None)
    context.item_id = item_request[0]["_id"]



@when(u'I {method} to {end_point}/roomsId')
def step_impl(context, method, end_point):
    context.end_point = end_point
    context.method = method
    context.response = get_delete_request(
        context.base_url, context.end_point,
        context.method, None, context.item_id,
        None)
