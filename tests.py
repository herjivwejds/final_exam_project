import requests
response = requests.get('http://127.0.0.1:8000/api/products/')
if response.status_code == 200:
    try:
        products = response.json()
    except ValueError:
        print('No JSON response or invalid JSON')
else:
    print(f"Request failed with status: {response.status_code}")
