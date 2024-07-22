import requests

BASE_URL = "https://httpbin.org"

# Send /get request and validate response code
def test_httpbin_get_request():
    URL = BASE_URL + "/get"
    resp = requests.get(URL)
    print(resp.status_code)

    assert resp.status_code == 200

# Send /post request with json body and validate response contains relevant data
def test_http_bin_post_request():
    URL = BASE_URL + "/post"
    payload = {
        "name": "Pavan",
        "place": "Bangalore"
    }
    resp = requests.post(URL, data=payload)
    data = resp.json()["form"]
    assert data == payload

# Validate request with delayed response /delay/{delay_time}
def test_httpbin_delayed_response():
    URL = BASE_URL + '/delay/4'
    resp = requests.get(URL)
    assert resp.status_code == 200

# Write any negative scenario
def test_authentication_positive_scenario():
    URL = BASE_URL + "/basic-auth/"
    username = "test_user"
    password = "test_password"
    resp = requests.get(URL + f"{username}/{password}", auth=(username, password))
    resp_json = resp.json()
    assert resp.status_code == 200
    assert resp_json['authenticated'] == True and resp_json['user'] == username

def test_authentication_negative_scenario():
    URL = BASE_URL + "/basic-auth/"
    username = "test_user"
    password = "test_password"
    # Note: Passing invalid URL while sending request
    resp = requests.get(URL + f"username/{password}", auth=(username, password))
    # validating with unauthorized status code
    assert resp.status_code == 401

# Simulate Unauthorized Access
def test_unauthorized_access_with_improper_bearer_token():
    URL = BASE_URL + '/bearer'

    TOKEN = "token 1"

    # headers = {
    #     "Authorization": f"Bearer {TOKEN}"
    # }

    # Passing improper Bearer token
    headers = {
        "Authorization": f"Bearers {TOKEN}"
    }
    resp = requests.get(URL, headers=headers)
    # validating with unauthorized status code
    assert  resp.status_code == 401




