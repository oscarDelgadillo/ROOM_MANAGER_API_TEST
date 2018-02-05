from behave import given, when
from compare import expect
from api_core.api_request.api_request_manager import get_delete_request, post_put_request
import json

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


########################


@given(u'I make a \'{method}\' request to \'{endpoint}\' by Id')
def step_impl(context, method, endpoint):
    context.method = method
    context.end_point = endpoint

@given(u'I made a \'POST\' request to \'/meetings\'')
def step_impl(context):
    context.end_point_me = '/meetings' #endpoint
    context.method_me = 'POST' #method

@given(u'I have meeting whit credentiales \'{credentiales}\' and the body is')
def step_impl(context, credentiales):
    context.text
    context.credentiales_me=credentiales
    json_text=json.loads(context.text)
    context.response= post_put_request(context.base_url, context.end_point_me, context.method_me, context.credentiales_me, None,json_text )

@given(u'I keep the "id" as "$id_meeting" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.id_meeting = resp_json["_id"]
    context.after_method = 'DELETE'

@when(u'I execute the request with "$id_meeting" and the following info')
def step_impl(context):
    context.parameters = {}
    for row in context.table:
        context.parameters["owner"] = row["owner"]
        context.parameters["start"] = row["start"]
        context.credentials = row["credentials"]

    context.response = get_delete_request(context.base_url, context.end_point, context.method, context.credentials,
                                          context.id_meeting, context.parameters)

