from behave import then, step, when
from compare import expect

from api_core.api_request.api_request_manager import get_delete_request, post_put_request
from api_core.utils.compare_json import compare_json


@step(u'I keep the "id" as "$id_(.+)" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.item_id = resp_json["_id"]
    context.after_item_id = resp_json["_id"]
    context.after_method = 'DELETE'
    print("EL id ES :", context.id_meeting)


@step(u'I send the request delete')
def step_impl(context):
    context.resp = get_delete_request(context.base_url,
                                      context.endpoint,
                                      context.after_method,
                                      context.credentials,
                                      context.id_meeting, None)

    print("Was deleted meeting id:", context.id_meeting)
    print('//////////////////////////////')
    print(context.resp.json())


@step(u'I send the request update')
def step_impl(context):
    # (base_url, end_point, method, credentials, item_id, data):
    context.resp = post_put_request(context.base_url,
                                    context.endpoint,
                                    'PUT',
                                    context.credentials,
                                    context.id_meeting,
                                    context.data)

    print("Was update meeting id:", context.id_meeting)
    print('//////////////////////////////')
    print(context.resp.json())


# @step(u'I send the request cancel')
# def step_impl(context):
#     # (base_url, end_point, method, credentials, item_id, data):
#     context.resp = post_put_request(context.base_url,
#                                     context.endpoint,
#                                     'POST',
#                                     context.credentials,
#                                     context.id_meeting,
#                                     context.data)
#
#     print("Was update meeting id:", context.id_meeting)
#     print('//////////////////////////////')
#     print(context.resp.json())
@step(u'I send the request {method}')
def step_impl(context, method):
    # (base_url, end_point, method, credentials, item_id, data):
    context.resp = post_put_request(context.base_url,
                                    context.endpoint,
                                    method,
                                    context.credentials,
                                    context.id_meeting,
                                    context.data)

    print("Was update meeting id:", context.id_meeting)
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


@when(u'I make POST request to /meetings/$id_meeting/cancellation')
def step_impl(context):
    context.end_point = str('/meetings/' + context.item_id + '/cancellation')
    context.method = 'POST'
    print('------------endpoint---------')
    print(context.end_point)
    # expect(False).to_be_truthy()
    # requester = requests.request(method, context.builder.built_url(end_point))
