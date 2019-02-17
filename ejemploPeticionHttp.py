import requests

url = 'https://www.getpostman.com/'

res = requests.get(url)

print(res.content)
