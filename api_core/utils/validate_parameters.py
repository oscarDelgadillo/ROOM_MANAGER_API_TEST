def validate_parameters(dictionary, param):
    """ This method replace parameters of the feature with environments """
    if param[0] == '_' and param[1] == '_':
        return dictionary[param]
    return param


def replace_parameters(dictionary, param):
    """ This method replace json parameters with environments """
    param = str(param)
    for key in dictionary:
        param = param.replace(key, dictionary[key])
    return param
