from behave import when, then
from compare import expect


@when(u'I set with the following params')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params['type'] = row['type']
        context.params['hostname'] = row['hostname']
        context.params['username'] = row['username']
        context.params['password'] = row['password']
        context.params['deleteLockTime'] = int(row['deleteLockTime'])


@then(u'validate response with get method')
def step_impl(context):
    expect(1).to_equal(2)
