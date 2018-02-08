import json
from compare import expect
from behave import step
from api_core.utils.validate_parameters import validate_parameters, replace_parameters


@step(u'I set the following parameters for a meeting')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["owner"] = validate_parameters(context, row["owner"])
        context.params["start"] = validate_parameters(context, row["start"])
        context.credentials = validate_parameters(context, row["credentials"])


@step(u'I set the following parameters for a meetings')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["owner"] = validate_parameters(context, row["owner"])
        context.params["start"] = validate_parameters(context, row["start"])
        context.params["end"] = validate_parameters(context, row["end"])
        context.credentials = validate_parameters(context, row["credentials"])


@step(u'I set the following body')
def step_impl(context):
    json_text = replace_parameters(context, context.text)
    json_text = json.loads(json_text)
    context.data = json_text


@step(u'I send \'{credentials}\' as credentials')
def step_impl(context, credentials):
    context.credentials = validate_parameters(context, credentials)
