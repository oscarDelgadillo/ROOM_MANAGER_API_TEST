from behave import given, when

from api_core.api_request.api_request_manager import get_delete_request


@given(u'I have room manager server up')
def step_impl(context):
    print()
