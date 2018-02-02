from compare import expect
from api_core.api_request.api_request_manager import get_delete_request

@given(u'I go to Room Manager services "{services}"')
def step_impl(context,services):
    context.end_point = services

@when(u'I do "{method}" to services with this data : hostname {hostname} , name {name}, type server {typ} and version {version}')
def step_impl(context,method,hostname,name,typ, version):
    context.method = method
    print(hostname)
    param= {'hostname': hostname,'name':name,'type':typ,'version':version}
    response = get_delete_request(context.base_url, context.end_point,context.method, None,None, param)
    context.status = response.status_code

@then(u'It should return status code "{expect_status}"')
def step_impl(context,expect_status):
    expect(str(context.status)).to_equal(str(expect_status))


