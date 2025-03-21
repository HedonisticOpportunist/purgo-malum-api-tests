import requests


def make_a_get_request(request_url: str):
    response = requests.get(request_url)
    return response


def return_status_code(response):
    return response.status_code


def return_json_body(response):
    return response.json()
