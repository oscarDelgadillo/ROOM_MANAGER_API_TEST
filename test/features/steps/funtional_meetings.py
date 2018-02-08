from behave import step

from api_core.utils.validate_parameters import validate_parameters


@step(u'I set the following parameters for a meeting with')
def step_impl(context):
    print("-----------------------------------------------------------------------")
    context.params = {}
    for row in context.table:
        if not row["owner"] == '':
            context.params["owner"] = validate_parameters(context, row["owner"])
            print(context.params["owner"])

        if not row["start"] == '':
            context.params["start"] = validate_parameters(context, row["start"])
            print(context.params["start"])

        if not row["end"] == '':
            context.params["end"] = validate_parameters(context, row["end"])
            print(context.params["end"])

        if not row["credentials"] == '':
            context.credentials = validate_parameters(context, row["credentials"])
            print(context.credentials)
        print("-----------------------------------------------------------------------")
