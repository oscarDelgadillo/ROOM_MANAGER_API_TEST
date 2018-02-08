from behave import when, then
from compare import expect

from api_core.utils.common_functions import build_rooms_query_list, build_query
from api_core.utils.compare_json import response_contains_query


@when(u'I set the following query')
def step_impl(context):
    context.query_list = build_rooms_query_list(context.table)
    query = build_query(context.query_list)
    context.params.update(query)


@then(u'I should get a response containing the params requested')
def step_impl(context):
    expect(True).to_equal(response_contains_query(context.query_list, context.response.json()))
