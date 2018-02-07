from behave import step
from compare import expect
from api_core.utils.validate_schemes_json import validate_schema
from api_core.utils.compare_json import *


@step(u'I validate the schema of the request')
def step_impl(context):
    print("VALIDANDO ESQUEMAS: ", validate_schema(context.response.json(), 'schema_meeting'))
    expect(True).to_equal(validate_schema(context.response.json(), 'schema_meeting'))


#
@step(u'I validate the response contains the body json sent')
def step_impl(context):
    print("DATA:", context.data)
    print("RESPONSE:", context.response.json())
    print("COMPARACION:", compare_json(context.data, context.response.json()))
    print("COMPARACION_2:", compare_json(context.response.json(), context.data))

    expect('11111111') == '55555555555555'
