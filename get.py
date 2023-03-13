import requests


def getMethod():

  URL = 'https://httpbin.org/get'
  
  response = requests.get(URL)
  print(response.status_code)
  print(response.text)
  
  payload = response.json()
  print('\n', payload.get('origin'))
  
  print(response.url)


getMethod()