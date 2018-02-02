from behave import given, when
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request


@given(u'I make a \'{method}\' request to \'{endpoint}\'')
def step_impl(context, method, endpoint):
    context.method = method
    context.end_point = endpoint


@when(u'I execute the request with the following infor')
def step_impl(context):
    context.parameters = {}
    for row in context.table:
        context.parameters["owner"] = row["owner"]
        context.parameters["start"] = row["start"]
        context.credentials = row["credentials"]
    context.response = get_delete_request(context.base_url, context.end_point, context.method, context.credentials,
                                          None, context.parameters)


@then(u'I expect a response status code \'{status_code}\'')
def step_impl(context, status_code):
    expect(str(context.response.status_code)) == status_code
