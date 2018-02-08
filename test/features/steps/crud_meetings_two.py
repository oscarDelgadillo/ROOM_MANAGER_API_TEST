from behave import step
from compare import expect
from api_core.utils.validate_schemes_json import validate_schema
from api_core.utils.compare_json import *


@step(u'I keep the "id" as "$id_meeting" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.item_id = resp_json["_id"]
    context.after_item_id = resp_json["_id"]
    context.id_meeting = resp_json["_id"]


@step(u'I keep the "body" respons as "$body_respons"')
def step_impl(context):
    context.body_respons = context.response.json()
    resp_json = context.response.json()
    context.after_item_id = resp_json["_id"]
    context.id_meeting = resp_json["_id"]


# ----------------------------------------------------------------
# ------------------- Validations---------------------------------
# ----------------------------------------------------------------
@step(u'I validate the schema of the request')
def step_impl(context):
    print("VALIDATION SCHEME: ", validate_schema(context.response.json(), 'schema_meeting'))
    expect(True).to_equal(validate_schema(context.response.json(), 'schema_meeting'))


@step(u'I validate the schemas of the request')
def step_impl(context):
    print("VALIDATION SCHEME: ", validate_schema(context.response.json(), 'schema_meeting_array'))
    expect(True).to_equal(validate_schema(context.response.json(), 'schema_meeting_array'))


@step(u'I validate the response contains the body json sent')
def step_impl(context):
    print("DATA:", context.data)
    print("equivalencia:", equivalence_json(context.data, context.response.json()))
    expect(True).to_equal(equivalence_json(context.data, context.response.json()))


@step(u'I validate the GET response  compare with POST response')
def step_impl(context):
    print("RESPONSE:", context.response.json())
    print("BODY_RESPONSE:", context.body_respons)
    print("COMPARACION:", compare_json(context.body_respons, context.response.json()))
    expect(True).to_equal(compare_json(context.body_respons, context.response.json()))
    # expect('11111111') == '55555555555555'


@step(u'I validate the GET response contains the POST response')
def step_impl(context):
    # print("*****************GET RESPONSE:******************************************************")
    # print("RESPONSE:", context.response.json())
    # print("*****************POST RESPONSE:******************************************************")
    # print("BODY_RESPONSE:", context.body_respons)
    print("CONTENGA:", json_contains(context.body_respons, context.response.json()))
    expect(True).to_equal(json_contains(context.body_respons, context.response.json()))
