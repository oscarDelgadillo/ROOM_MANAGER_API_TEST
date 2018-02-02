from behave import when, then


@when(u'I set {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    context.endpoint = endpoint


@when(u'I set {credentials} as credentials')
def step_impl(context, credentials):
    context.credentials = credentials
