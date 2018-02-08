# Module: common_functions


def build_json(table, item_name, context):
    """This function builds a Json from file depending on the item name
        params:
            @table: table to convert
            @item_name: name of the item
            @context: context from step
            """
    if item_name == "meeting":
        return build_meeting(context, table)
    elif item_name == "service":
        return build_service(context, table)


def build_meeting(context, table):
    """This function builds a Json for usage on meetings' requests
        params:
            @table: meetings table to convert
            @context: context from step
            """
    json_data = {}
    return json_data


def build_service(context,table):
    """This function builds a Json for usage on services' requests
        params:
            @table: service table to convert
            @context: context from step"""
    json_data = {}
    for row in table:
        context.data["type"] = context.services[row['type']]
        context.data["hostname"] = context.services[row['hostname']]
        context.data["username"] = context.accounts[row['username']]
        context.data["password"] = context.accounts[row['password']]
        context.data["deleteLockTime"] = context.services[row['deleteLockTime']]
    return json_data


def build_params(table):
    """This function builds a Json for usage on as request' params
        params:
            @table: params table to convert
            """
    params = {}
    for row in table:
        params['from'] = row['from']
        params['to'] = row['to']
        params['status'] = row['status']
    return params
