
def validate_parameters(context, param):
    if param[0]=='_' and param[1]=='_':
        return context.accounts[param]
    return param

def replace_parameters(context, param):
    param=str(param)
    for key in context.accounts:
        param = param.replace(key, context.accounts[key])
    return param
