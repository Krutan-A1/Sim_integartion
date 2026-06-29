import requests

payload = {
    "device":"SIM7600",
    "temperature":27,
    "humidity":64
}

r = requests.post(
    "https://httpbin.org/post",
    json=payload
)

print(r.json())