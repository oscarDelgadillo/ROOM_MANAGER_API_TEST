from behave import when, step


from behave import when, step

from api_core.api_request.api_request_manager import get_delete_request, post_put_request

from api_core.api_request.api_request_manager import request


@step(u'I {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    aux_endpoint = str(endpoint).split('/')
    context.endpoint ='/{}/{}'.format(aux_endpoint[1], context.__ServId)
    print("estoy enviado el ai para eleminar",context.endpoint)

@step(u'I set {credentials} as credentials')
def step_impl(context, credentials):
    context.credentials = credentials


@step(u'I send the request')
def step_impl(context):
    print("nooooooooooooooooooooooooooooo")
    print(context.endpoint)
    print(context.base_url)
    print(context.method)
    print(context.credentials)
    print(context.item_id)
    print(context.data)
    print(context.params)
    print("fin")
    print("siiiiiiiiiiiiiiiiiiiiiiii")
    context.response = request(context.base_url, context.endpoint, context.method, context.credentials, context.item_id,
                               context.data, context.params)
    print("pasoooooooooooooooooooooooooooooooooooo")
    context.status_code = context.response.status_code



@step(u'I keep service_id as __ServId')
def step_impl(context):
    context.__ServId = context.response.json()['_id']
    print("aaaaaaaaaaaaaaaaaaaadiiiiiiiiiiiiii",context.__ServId)




@step(u'Given I have a Service Created with this data')
def step_impl(context):
    context.data = {}
    print("************************************************")
    print( context.__type_server)
    print( context.__hostname)
    print("************************************************")
    for row in context.table:
        context.data["type"] = context.__type_server
        context.data["hostname"] = context.__hostname
        context.data["username"] = context.accounts[row['username']]
        context.data["password"] = context.accounts[row['password']]
        context.data["deleteLockTime"] = context.__deleteLockTime
    print("marcoooooooooooooooooo")

    #def request(base_url, endpoint, method, credentials, item_id, data, params):
    context.response = request(context.base_url, "/services", 'POST', None, None,context.data,context.params)
    # context.item_id = response.json()['_id']
    print(context.response.status_code)
    print("marcoooooooooooooooooppppppppppppppppppo")

