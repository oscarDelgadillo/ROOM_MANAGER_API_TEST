from behave import given
from api_core.api_request.api_request_manager import post_put_request


@given(u'I have a meeting {method} to {endpoint} with the following info')
def step_impl(context, endpoint, method):
    context.data = {}
    for row in context.table:
        context.data['organizer'] = row['organizer']
        context.data['subject'] = row['subject']
        context.data['body'] = row['body']
        context.data['start'] = row['start']
        context.data['end'] = row['end']
        context.data['rooms'] = [row['rooms']]
        context.data['attendees'] = [row['attendees']]
        context.data['optionalAttendees'] = [row['optionalAttendees']]

    context.method = method
    context.endpoint = endpoint
    context.after_endpoint = context.endpoint

    # Creating meeting
    context.response = post_put_request(context.base_url, context.endpoint, context.method, context.credentials, None,
                                        context.data)
    print("POST Response Status Code:", context.response.status_code)

    context.after_item_id = context.response.json()["_id"]
    context.after_credentials = context.credentials
    context.credentials = None
