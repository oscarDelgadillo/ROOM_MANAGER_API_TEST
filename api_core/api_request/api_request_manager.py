# Module: api_request_manager
import requests

headers = {'Accept': 'application/json'}


def get_delete_request(base_url, end_point, method, credentials, item_id, params):
    """This method performs GET or DELETE request"""
    response = None
    uri = base_url + end_point
    if item_id is not None:
        headers['Credentials'] = credentials
        headers['ServiceName'] = 'ExchangeServer'
        uri = "{}/{}".format(uri, item_id)
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


def post_put_request(base_url, end_point, method, credentials, meeting_id, data):
    """This method performs POST or PUT request"""
    response = None
    uri = base_url + end_point
    headers['Content-Type'] = 'application/json'
    headers['Credentials'] = credentials
    if meeting_id is not None:
        headers['ServiceName'] = 'ExchangeServer'
        uri = "{}/{}".format(uri, meeting_id)
        if method == 'POST':
            response = requests.post(url=uri, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url=uri, headers=headers, json=data)
    elif method == 'POST':
        headers['Accept'] = 'application/json'
        response = requests.post(url=uri, headers=headers, json=data)
    return response
