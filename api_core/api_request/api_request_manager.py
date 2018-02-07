# Module: api_request_manager
import requests

headers = {'Accept': 'application/json'}


def delete_request(base_url, end_point, credentials, params):
    uri = base_url + end_point
    headers['Credentials'] = credentials
    headers['ServiceName'] = 'ExchangeServer'
    response = requests.delete(url=uri, headers=headers, params=params)
    return response


def post_request(base_url, end_point, credentials, data):
    uri = base_url + end_point
    headers = {'Accept': 'application/json'}
    headers['Credentials'] = credentials
    headers['ServiceName'] = 'ExchangeServer'
    response = requests.post(url=uri, headers=headers, json=data)
    return response


def put_request(base_url, end_point, credentials, data):
    uri = base_url + end_point
    print("****************************")
    print("puuuuuuuuuuuuuuuuuuuuuut")
    headers = {'Accept': 'application/json'}
    #headers['Credentials'] = credentials
    headers['Content-Type'] = 'application/json'
   # headers['Content-Type'] = 'ExchangeServer'

    print("uri",uri)
    print("hed",headers)
    print("json",data)
    print("****************************")
    response = requests.put(url=uri, headers=headers, json=data)
    print("resssponse", response.status_code)
    return response


def get_request(base_url, end_point, credentials, param):
    uri = base_url + end_point
    headers = {'Accept': 'application/json'}
    headers['Credentials'] = credentials
    response = requests.get(url=uri, headers=headers, params=param)
    return response


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
    headers = {'Accept': 'application/json'}
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
    if method == 'DELETE':
        return delete_request(base_url, endpoint, credentials, data)
    elif method == 'POST':
        return post_request(base_url, endpoint, credentials, data)
    elif method == 'PUT':
        return put_request(base_url, endpoint, credentials, data)
    elif method == 'GET':
        return get_delete_request(base_url, endpoint, method, credentials, item_id, params)
