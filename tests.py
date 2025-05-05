import requests
response = requests.get("http://127.0.0.1:8000/api/products/")
if response.status_code == 200:
    products = response.json()
else:
    print(f"Error {response.status_code}: {response.text}")