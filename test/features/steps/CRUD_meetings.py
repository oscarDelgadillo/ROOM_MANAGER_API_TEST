from behave import then, step, when
from compare import expect

from api_core.api_request.api_request_manager import get_delete_request, post_put_request
from api_core.utils.compare_json import compare_json


@step(u'I send the request delete')
def step_impl(context):
    context.resp = get_delete_request(context.base_url,
                                      context.endpoint,
                                      context.method,
                                      context.credentials,
                                      context.id_meeting,
                                      None)


@step(u'I send the request update')
def step_impl(context):
    context.resp = post_put_request(context.base_url,
                                    context.endpoint,
                                    'PUT',
                                    context.credentials,
                                    context.id_meeting,
                                    context.data)


@step(u'I construct a expected response')
def step_impl(context):
    context.actual_json = context.resp.json()
    context.expect_json = context.data
    context.expect_json['_id'] = context.id_meeting
    context.expect_json['body'] = context.actual_json['body']


@then(u'the built expected response should be equal to the obtained response')
def step_impl(context):
    result = compare_json(context.expect_json, context.actual_json)
    expect(result).to_be_truthy()


@when(u'I make POST request to /meetings/$id_meeting/cancellation')
def step_impl(context):
    context.end_point = str('/meetings/' + context.item_id + '/cancellation')
    context.method = 'POST'
