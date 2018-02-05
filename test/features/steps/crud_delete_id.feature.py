from behave import given
@given(u'I have a Service Created with this data')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["type"] = row["type"]
        context.params["hostname"]= row["hostname"]
        context.params["username"] = row["username"]
        context.params["password"] = row["password"]
        context.params["deleteLockTime"] = 10
    #post_put_request(base_url, end_point, method, credentials, meeting_id, data):
   # response = post_put_request(context.base_url, "/services",'POST', None, None, context.params)
    #print(response.status_code)
    #response = post_put_request(None,None,'POST',None,None,)



@given(u'I have a services created in "{hostname}"')
def step_impl(context,hostname):
    context.params = {'hostname':hostname}

    context.item_id =


