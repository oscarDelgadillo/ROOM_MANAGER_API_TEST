from behave import given, when, step


@step(u'I set a invalid {__item_id} as this {invalid_id}')
def step_impl(context, __item_id, invalid_id):
    context.item_ids[__item_id] = invalid_id
