@when(u'I set the following params ')
def step_impl(context):
    context.params = {}
    context.params["hostname"] = context.__hostname
    context.params["name"] = context.__name_server
    context.params["type"] = context.__type_server
    context.params["version"] =  context.__version_server
    context.credentials = None
    context.item_id = None
