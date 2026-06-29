import requests

try:
    r = requests.get("https://httpbin.org/ip", timeout=5)
    print(r.text)
except Exception as e:
    print(e)