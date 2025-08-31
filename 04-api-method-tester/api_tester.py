import requests

url = input("Enter API endpoint: ")
methods = ["GET", "POST", "PUT", "DELETE", "HEAD"]

for method in methods:
    try:
        response = requests.request(method, url)
        print(f"{method}: {response.status_code}")
    except Exception as e:
        print(f"{method}: ERROR - {e}")
