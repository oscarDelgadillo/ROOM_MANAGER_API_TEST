def validate_parameters1(dictionary, param):
    """ This method replace parameters of the feature with environments """
    if param[0] == '_' and param[1] == '_':
        return dictionary[param]
    return param


def replace_parameters1(dictionary, param):
    """ This method replace json parameters with environments """
    param = str(param)
    for key in dictionary:
        param = param.replace(key, dictionary[key])
    return param

def validate_parameters(context, param):
    """ This method replace parameters of the feature with environments """
    if param[0] == '_' and param[1] == '_':
        return context.accounts[param]
    return param


def replace_parameters(context, param):
    """ This method replace json parameters with environments """
    param = str(param)
    for key in context.accounts:
        param = param.replace(key, context.accounts[key])
    return param