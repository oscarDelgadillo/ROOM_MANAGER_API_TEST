from behave import then, step
from compare import expect

from api_core.api_request.api_request_manager import get_delete_request
from api_core.utils.compare_json import compare_json


@step(u'I keep the "id" as "$id_(.+)" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.item_id = resp_json["_id"]
    context.after_item_id = resp_json["_id"]
    context.after_method = 'DELETE'
    print("EL id ES :", context.id_meeting)


@step(u'I send the request extra')
def step_impl(context):
    context.resp = get_delete_request(context.base_url, context.endpoint, context.after_method, context.credentials,
                                      context.id_meeting, None)

    print("Was deleted meeting id:", context.id_meeting)
    print('//////////////////////////////')
    print(context.resp.json())


@then(u'I should get a response with status code {status_code:d} extra')
def step_impl(context, status_code):
    print('Response: ')
    print(context.resp.status_code)
    print('Status Code:', context.resp.status_code)
    expect(status_code).to_equal(context.resp.status_code)


@step(u'I construct a expected response')
def step_impl(context):
    print('**************************ACTUAL*****************')
    print(context.resp.json())
    context.actual_json = context.resp.json()
    print('**************************EXPECTED*****************')
    context.expect_json = context.data
    context.expect_json['_id'] = context.id_meeting
    context.expect_json['body'] = context.actual_json['body']
    print(context.expect_json)



@then(u'the built expected response should be equal to the obtained response')
def step_impl(context):
    result = compare_json(context.expect_json, context.actual_json)
    print('+++++++++++++++++result compare json+++++++++++++++++')
    print(result)
    expect(result).to_be_truthy()
