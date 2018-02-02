# Smoke test: get rooms
from behave import given, when

from api_core.api_request.api_request_manager import get_delete_request


@given(u'I have rooms created')
def step_impl(context):
    print()


@when(u'I set the following params')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params['from'] = row['from']
        context.params['to'] = row['to']
        context.params['status'] = row['status']


@given(u'I have obtained roomsId of the database')
def step_impl(context):
    context.item_id = '5a720749d54ad40d1882f3e6'


@when(u'I {method} to {end_point}/roomsId')
def step_impl(context, method, end_point):
    context.end_point = end_point
    context.method = method
    context.response = get_delete_request(
        context.base_url, context.end_point,
        context.method, None, context.item_id,
        None)
