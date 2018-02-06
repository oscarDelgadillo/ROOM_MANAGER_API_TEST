from behave import step
from api_core.util.validate_parameters import validate_parameters, replace_parameters
import json


@step(u'I set the following parameters')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["owner"] = validate_parameters(context, row["owner"])
        context.params["start"] = validate_parameters(context, row["start"])
        context.credentials = validate_parameters(context, row["credentials"])


@step(u'I set the following body')
def step_impl(context):
    print("")
    context.text
    json_text = replace_parameters(context, context.text)
    json_text = json.loads(json_text)
    context.data = json_text


@step(u'I send \'{credentials}\' as credentials')
def step_impl(context, credentials):
    context.credentials = validate_parameters(context, credentials)


@step(u'I keep the "id" as "$id_meeting" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.id_meeting = resp_json["_id"]
    context.after_method = 'DELETE'
    print("EL id ES :", context.id_meeting)
