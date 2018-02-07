from behave import when


@when(u'I set the following params ')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["hostname"] = context.environment_variables[row['hostname']]
        context.params["name"] = context.environment_variables[row['name']]
        context.params["type"] = context.environment_variables[row['type']]
        context.params["version"] = context.environment_variables[row['version']]
    context.credentials = None
    context.item_id = None
