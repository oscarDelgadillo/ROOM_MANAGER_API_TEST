from behave import given, when

from api_core.api_request.api_request_manager import get_delete_request


@given(u'I have room manager server up')
def step_impl(context):
    print()


@when(u'I {method} to {end_point}')
def step_impl(context, method, end_point):
    context.end_point = end_point
    context.method = method
    context.response = get_delete_request(context.base_url, context.end_point, context.method, None, None, None)
