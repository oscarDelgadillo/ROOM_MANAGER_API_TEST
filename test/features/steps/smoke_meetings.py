import json

from behave import step

from api_core.utils.validate_parameters import validate_parameters, replace_parameters

@step(u'I set the following parameters for a meeting')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["owner"] = validate_parameters(context.accounts, row["owner"])
        context.params["start"] = validate_parameters(context.accounts, row["start"])
        context.credentials = validate_parameters(context.accounts, row["credentials"])


@step(u'I set the following body')
def step_impl(context):

    json_text = replace_parameters(context.accounts, context.text)
    json_text = json.loads(json_text)
    context.data = json_text


@step(u'I send \'{credentials}\' as credentials')
def step_impl(context, credentials):
    context.credentials = validate_parameters(context.accounts, credentials)


@step(u'I keep the "id" as "$id_meeting" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.item_id = resp_json["_id"]
    context.id_meeting = resp_json["_id"]
    context.after_method = 'DELETE'
    print("EL id ES :", context.id_meeting)
