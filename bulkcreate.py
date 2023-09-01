import requests

url = "https://core.subsplash.com/media/v1/media-items"

# set app_key and title. This title was the first thing I thought of..
data = {
    "app_key": "app_key",
    "title": "Bulk Created"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_BEARER_TOKEN"
}

# set "x" to how ever many media items they want created, sends "x" POST requests. e.g. for _ in range(100):
for _ in range("x"):
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:  # HTTP status code for Created
        print("Media item created")
    else:
        print(f"Request {response.request.method} {response.url} - Status code: {response.status_code}")
