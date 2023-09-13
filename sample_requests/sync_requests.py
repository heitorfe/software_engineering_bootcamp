import requests

def get_and_parse_user(base_url : str, endpoint_prefix: str, user_id : int):

    url = base_url + endpoint_prefix + str(user_id)
    response = requests.get(url)
    return response.json()