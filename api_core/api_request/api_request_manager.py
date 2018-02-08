# Module: api_request_manager
import requests

headers = {'Accept': 'application/json'}


def delete_request(base_url, end_point, credentials, params):
    uri = base_url + end_point
    response = requests.delete(url=uri, headers=headers, params=params)
    return response


def post_request(base_url, end_point, credentials, data):
    uri = base_url + end_point
    response = requests.post(url=uri, headers=headers, json=data)
    return response


def put_request(base_url, end_point, credentials, data):
    uri = base_url + end_point
    response = requests.put(url=uri, headers=headers, json=data)
    return response


def get_request(base_url, end_point, credentials, param):
    uri = base_url + end_point
    response = requests.get(url=uri, headers=headers, params=param)
    return response


def get_delete_request(base_url, end_point, method, credentials, item_id, params):
    """This method performs GET or DELETE request"""
    # headers = {'Accept': 'application/json'}
    response = None
    uri = base_url + end_point
    if item_id is not None:
        headers['Credentials'] = credentials
        headers['ServiceName'] = 'ExchangeServer'
        uri = "{}/{}".format(uri, item_id)
        if method == 'GET':
            response = requests.get(url=uri, headers=headers, params=params)
        elif method == 'DELETE':
            response = requests.delete(url=uri, headers=headers, params=params)
    elif method == 'GET':
        if credentials is not None:
            headers['Credentials'] = credentials
            response = requests.get(url=uri, headers=headers, params=params)
        else:
            response = requests.get(url=uri, headers=headers, params=params)
    return response


def post_put_request(base_url, end_point, method, credentials, item_id, data):
    """This method performs POST or PUT request"""
    response = None
    uri = base_url + end_point
    headers['Content-Type'] = 'application/json'
    headers['Credentials'] = credentials
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


def request(base_url, endpoint, method, credentials, item_id, data, params):
    headers['ServiceName'] = 'ExchangeServer'
    if method == 'DELETE':
        return delete_request(base_url, endpoint, credentials, data)
    elif method == 'POST':
        headers['Content-Type'] = 'application/json'
        headers['Credentials'] = credentials
        return post_request(base_url, endpoint, credentials, data)
    elif method == 'PUT':
        headers['Content-Type'] = 'application/json'
        return put_request(base_url, endpoint, credentials, data)
    elif method == 'GET':
        return get_delete_request(base_url, endpoint, method, credentials, item_id, params)

