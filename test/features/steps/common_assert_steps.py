from behave import then
from compare import expect
from pprint import pprint

from api_core.api_request.api_request_manager import get_delete_request, get_request


@then(u'I should get a response with status code {status_code:d}')
def step_impl(context, status_code):
    print("quiero lorar")
    print(context.response.status_code)
    print('Status Code:', context.response.status_code)
    print("1",status_code)
    print("2",context.response.status_code)
    expect(status_code).to_equal(context.response.status_code)


@then(u'I should get an empty Json response')
def step_impl(context):
    expected_body = []
    print('Expected body', expected_body)
    print('Actual body:')
    pprint(context.response.json())
    expect(expected_body).to_equal(context.response.json())

@then(u'The response should equals that Get method')
def step_impl(context):#def get_request(base_url, end_point, credentials, param):
    mapa = get_request(context.base_url, "/services", None, None).json()
    print(mapa)
    for dictonary in mapa:
        if(context.item_id == dictonary['_id']):
            expect(context.data['username1']).to_equal(dictonary['username'])
            break