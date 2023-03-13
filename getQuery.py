import requests


def getMethod():
  """Get method with Query"""

  URL = 'https://httpbin.org/get'

  params = {'name': 'Alfredo', 'last_name': 'Valdez', 'password': '123'}

  response = requests.get(URL, params=params)
  if response.status_code == 200:
    payload = response.json()
    params = payload['args']

    print(params['name'])
    print(params['last_name'])
    print(params['password'])

    print(response.url)


getMethod()