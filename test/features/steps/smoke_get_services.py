from behave import when


@when(u'I set the following params ')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["hostname"] = context.services[row['hostname']]
        context.params["name"] = context.services[row['name']]
        context.params["type"] = context.services[row['type']]
        context.params["version"] = context.services[row['version']]
    context.credentials = None
    context.item_id = None
