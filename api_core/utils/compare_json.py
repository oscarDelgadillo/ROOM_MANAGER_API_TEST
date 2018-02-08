# Module: compare_json
from bson import ObjectId


def json_contains(json, json_response_list):
    """This method receive a json and a list of json  of the response;
    json checks if this content in the json list.
        params:
            @json: Json to validate
            @json_response_list: List of items (Json)
            """
    if json in json_response_list:
        return True
    else:
        return False


def json_key_contains(key, value, json_response_list):
    """This method verify if a key with some value is content in the json list.
        params:
            @key: key to use for comparing
            @value: value to compare
            @json_response_list: List of items (Json)
            """
    for item in json_response_list:
        if item[key] == value:
            return True
    return False


def compare_json(expected, actual):
    """This method check if two json are equals. Otherwise, display when it is not
        params:
            @expected_json: Object base to compare with
            @actual_json: Object to compare
            """
    if type(expected) and type(actual) is not dict:
        return None

    result = True
    for key in expected.keys():
        if key in actual.keys():
            if type(expected[key]) is ObjectId:
                if str(expected[key]) == str(actual[key]):
                    continue
                else:
                    result = False
                    print(f'Exp:{key}-> ObjId({expected[key]}) not equal to Act:{key}-> ObjId({actual[key]})')
            else:
                if expected[key] == actual[key]:
                    # print(f'{key}:{expected_json[key]} is equal to {key}:{actual_json[key]}')
                    continue
                else:
                    print(f'Exp:{key}-> {expected[key]} not equal to Act:{key}-> {actual[key]}')
                    result = False
    return result


def extract_item(json_obj):
    """This method extracts a Json (dict format) from a given json response
        params:
            @json_obj: object to use
            @return: A json item if the input is a non empty list, otherwise it returns the empty list
            """
    if type(json_obj) is not dict:
        if type(json_obj) is list:
            if len(json_obj) != 0:
                return json_obj[0]
            else:
                return json_obj
    return json_obj


def response_contains_query(query_list, response):
    """This method validates if a response, matches with a query.
            params:
                @query_list: List with query parameters
                @response: A list containing the json response
                @return: True if the the response contains only the query params,
                 otherwise the result will be False
                """
    counter = 0
    for i in range(0, len(response)):
        for item in query_list:
            if item in response[i]:
                counter += 1
            else:
                print(f'{item} not in {response[i]}')
                break

    if counter == len(response * len(query_list)):
        return True
    else:
        print('Response does not match query params')
        return False
