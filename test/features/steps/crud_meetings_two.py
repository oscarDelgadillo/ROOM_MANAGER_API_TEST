from compare import expect
from api_core.utils.validate_schemes_json import validate_schema
from api_core.utils.compare_json import *



#

@step(u'I keep the "id" as "$id_meeting" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.item_id = resp_json["_id"]
    context.after_item_id = resp_json["_id"]
    context.id_meeting = resp_json["_id"]
    # context.item_id= None

    # print("JSONNNNNNNNNNN:", resp_json)
    print("EL id ES :", context.id_meeting)
    # expect('44444444')=='8888888888888'


@step(u'I keep the "body" respons as "$body_respons"')
def step_impl(context):
    context.body_respons = context.response.json()

    resp_json = context.response.json()
    context.after_item_id = resp_json["_id"]
    context.id_meeting = resp_json["_id"]

    # print("JSONNNNNNNNNNN SABE BODY:", resp_json)
    # context.item_id = resp_json["_id"]
    #
    # context.id_meeting = resp_json["_id"]
    # # context.after_method = 'DELETE'
    # print("EL id ES :", context.id_meeting)
    # expect('44444444')=='8888888888888'

#----------------------------------------------------------------
#------------------- Validations---------------------------------
#----------------------------------------------------------------
@step(u'I validate the schema of the request')
def step_impl(context):
    print("VALIDANDO ESQUEMAS: ", validate_schema(context.response.json(), 'schema_meeting'))
    print("RESPONS GET ALL: ", context.response.json())

    expect(True).to_equal(validate_schema(context.response.json(), 'schema_meeting'))
    # expect('44444444')=='8888888888888'

@step(u'I validate the schemas of the request')
def step_impl(context):

    print("VALIDANDO ESQUEMAS: ", validate_schema(context.response.json(), 'schema_meeting_array'))
    # print("RESPONS GET ALL: ", context.response.json())

    expect(True).to_equal(validate_schema(context.response.json(), 'schema_meeting_array'))
    # expect('44444444')=='8888888888888'



@step(u'I validate the response contains the body json sent')
def step_impl(context):
    print("----------------------------------DATA---------------------------------------------------------------------------------")
    print("DATA:", context.data)
    # print("RESPONSE:", context.response.json())
    # print("BODY_RESPONSE:", context.body_respons)
    print("equivalencia:", equivalence_json(context.data, context.response.json()))

    expect(True).to_equal(equivalence_json(context.data, context.response.json()))

    # /expect('11111111') == '55555555555555'

@step(u'I validate the GET response  compare with POST response')
def step_impl(context):
    print("DATA:", context.data)
    print("RESPONSE:", context.response.json())
    print("BODY_RESPONSE:", context.body_respons)
    print("COMPARACION:", compare_json(context.body_respons, context.response.json()))
    print("COMPARACION_2:", compare_json(context.response.json(), context.body_respons))

    # expect('11111111') == '55555555555555'


@step(u'I validate the GET response contains the POST response')
def step_impl(context):
    # print("DATA:", context.data)
    print("*****************GET RESPONSE:******************************************************")
    print("RESPONSE:", context.response.json())
    print("*****************POST RESPONSE:******************************************************")
    print("BODY_RESPONSE:", context.body_respons)
    print("CONTENGA:", json_contains(context.body_respons, context.response.json()))
    print("CONTENGA_2:", json_contains(context.response.json(), context.body_respons))

    # expect('11111111') == '55555555555555'
