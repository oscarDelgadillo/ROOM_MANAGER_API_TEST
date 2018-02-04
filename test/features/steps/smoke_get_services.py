@when(u'I set the following params ')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["hostname"] = row["hostname"]
        context.params["name"] = row["name"]
        context.params["type"] = row["type"]
        context.params["version"] = row["version"]
    context.credentials = None
    context.item_id = None
