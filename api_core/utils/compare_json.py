from bson import ObjectId


def json_contains(json, json_response_list):
    '''This method receive a json and a list of json  of the response;
    json checks if this content in the json list.'''
    if json in json_response_list:
        return True
    else:
        return False


def json_key_contains(key, value, json_response_list):
    '''This method verify if a key with some value is content in the json list.'''
    for item in json_response_list:
        if item[key] == value:
            return True
    return False


def compare_json(expected_json, actual_json):
    '''This method check if two json are equals. Otherwise, display when it is not'''

    result = True
    if type(expected_json) and type(actual_json) is not dict:
        return None

    for key in expected_json.keys():
        if key in actual_json.keys():
            if type(expected_json[key]) is ObjectId:
                if str(expected_json[key]) == str(actual_json[key]):
                    # print(f'ObjectId: {key}:{expected_json[key]} is equal to {key}:{actual_json[key]}')
                    continue
                else:
                    result = False
                    print(f'ObjectId: {key}:{expected_json[key]} is not equal to {key}:{actual_json[key]}')
            else:
                if expected_json[key] == actual_json[key]:
                    # print(f'{key}:{expected_json[key]} is equal to {key}:{actual_json[key]}')
                    continue
                else:
                    print(f'{key}:{expected_json[key]} is not equal to {key}:{actual_json[key]}')
                    result = False
    return result


def equivalence_json(json, to_compare):
    '''This method check if one dictionary contains the other'''
    try:
        for key in json:
            if not (str(json[key]) in str(to_compare[key]) or str(to_compare[key]) in str(json[key])):
                print(str(to_compare[key]) + "!=" + str(json[key]))
                return False
        return True
    except KeyError:
        return False
