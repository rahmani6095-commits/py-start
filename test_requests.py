import requests
try:
    response=requests.get("https://api.github.com",timeout=10)
    print(f"status code: {response.status_code}")
    print("اتصال به اینترنت برقراره")
except Exception as e:
    print(f"خطا: {e}")    