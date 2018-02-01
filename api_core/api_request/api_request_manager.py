# Module: api_request_manager
import requests

headers = {'Accept': 'application/json'}


# Function: Perform GET or DELETE request
def get_delete_request(base_url, end_point, method, credentials, meeting_id, params):
    response = None
    uri = base_url + end_point
    if meeting_id is not None:
        headers['Credentials'] = credentials
        headers['ServiceName'] = 'ExchangeServer'
        uri = uri + '/' + meeting_id
        print("new uri:", uri)
        if method == 'GET':
            response = requests.get(url=uri, headers=headers, params=params)
        elif method == 'DELETE':
            response = requests.delete(url=uri, headers=headers)
    elif method == 'GET':
        if credentials is not None:
            headers['Credentials'] = credentials
            response = requests.get(url=uri, headers=headers, params=params)
        else:
            response = requests.get(url=uri, headers=headers, params=params)
    return response


# Function: Perform POST or PUT request
def post_put_request(base_url, end_point, method, credentials, meeting_id, data):
    response = None
    uri = base_url + end_point
    headers['Credentials'] = credentials
    headers['Content-Type'] = 'application/json'
    if meeting_id is not None:
        headers['ServiceName'] = 'ExchangeServer'
        uri = uri + '/' + meeting_id
        print("new uri:", uri)
        if method == 'POST':
            response = requests.post(url=uri, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url=uri, headers=headers, json=data)
    elif method == 'POST':
        response = requests.post(url=uri, headers=headers, json=data)
    return response
