import requests


def postMethod():
  '''Method Post'''


URL = 'https://httpbin.org/post'

data = {'username': 'yocayoca', 'password': 'lapasswordmasarrechadetodas'}

response = requests.post(URL, data=data)
print(response.text)

if response.status_code == 200:
  payload = response.json()

  print('\n', payload['form'])
  print('\n', payload['url'])

  params = payload['headers']
  print('\n', params['Accept'])

postMethod()
