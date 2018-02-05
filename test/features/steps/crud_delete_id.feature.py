from behave import given
from compare import expect

from api_core.api_request.api_request_manager import get_delete_request, post_put_request


@given(u'Given I have a Service Created with this data')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["type"] = row["type"]
        context.params["hostname"] = row["hostname"]
        context.params["username"] = row["username"]
        context.params["password"] = row["password"]
        context.params["deleteLockTime"] = 10
    response = post_put_request(context.base_url, "/services", 'POST', None, None, context.params)
    context.item_id = response.json()['_id']
