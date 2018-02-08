# Module: common_functions
from api_core.utils.validate_parameters import validate_parameters


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
    for row in table:
        json_data['organizer'] = validate_parameters(context, row['organizer'])
        json_data['subject'] = row['subject']
        json_data['body'] = row['body']
        json_data['start'] = row['start']
        json_data['end'] = row['end']
        json_data['rooms'] = [row['rooms']]
        json_data['attendees'] = [row['attendees']]
        json_data['optionalAttendees'] = [row['optionalAttendees']]
    return json_data


def build_service(context, table):
    """This function builds a Json for usage on services' requests
        params:
            @table: service table to convert
            @context: context from step"""
    json_data = {}
    for row in table:
        json_data['type'] = validate_parameters(context, row['type'])
        json_data['hostname'] = validate_parameters(context, row['hostname'])
        json_data['username'] = validate_parameters(context, row['username'])
        json_data['password'] = validate_parameters(context, row['password'])
        json_data['deleteLockTime'] = int(validate_parameters(context, row['deleteLockTime']))
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


def build_rooms_query_list(table):
    """This function builds a query list from query table
            params:
                @table: query table to convert
                @return: A query list
                """
    items = []
    for row in table:
        items.append(row['_id'])
        items.append(row['uuid'])
        items.append(row['name'])
        items.append(row['displayName'])
        items.append(row['email'])
        items.append(row['code'])
        items.append(row['capacity'])
        items.append(row['service'])
        items.append(row['roomStatus'])
        items.append(row['equipment'])
        items.append(row['location'])

    query_list = clean_list(items, '')
    return query_list


def build_query(query_list):
    """This function builds a query for usage as request' query
            params:
                @query_list: query list to convert
                @return: A query string
                """
    query_string = add_separator(query_list, ',')
    query = {'$select': query_string}
    return query


def clean_list(items, chain):
    """This function cleans a list of the chain given
                params:
                    @original_list: the target list
                    @chain: the target list
                    @return: A new list without items equal to chain
                    """
    new_list = []
    for item in items:
        if item != chain:
            new_list.append(item)
    return new_list


def add_separator(items, separator):
    """This function adds a separator between items of a list
                    params:
                        @items: the target list
                        @separator: the separator
                        @return: a string with the separator between elements
                        of the list.
                        """
    return separator.join(items)
