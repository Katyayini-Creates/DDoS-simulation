import requests

target = "http://127.0.0.1:8080"

for i in range(10000):
    requests.get(target)