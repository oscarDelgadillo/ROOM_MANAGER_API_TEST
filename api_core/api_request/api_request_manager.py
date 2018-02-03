# Module: api_request_manager
import requests


def get_delete_request(base_url, end_point, method, credentials, item_id, params):
    """This method performs GET or DELETE request"""
    headers = {'Accept': 'application/json'}
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


def post_put_request(base_url, end_point, method, credentials, item_id, data):
    """This method performs POST or PUT request"""
    headers = {'Accept': 'application/json'}
    response = None
    uri = base_url + end_point
    headers['Credentials'] = credentials
    headers['Content-Type'] = 'application/json'
    if item_id is not None:
        headers['ServiceName'] = 'ExchangeServer'
        uri = "{}/{}".format(uri, item_id)
        if method == 'POST':
            response = requests.post(url=uri, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url=uri, headers=headers, json=data)
    elif method == 'POST':
        response = requests.post(url=uri, headers=headers, json=data)
    return response
