import requests


def getMethod():
  """Get method"""
  
  URL = 'https://httpbin.org/get'
  
  response = requests.get(URL)
  print(response.status_code)
  print(response.text)
  
  payload = response.json()
  # print('\n', payload.get('origin')) # Un solo valor del diccionario
  params = payload['headers'] #Los valores de un valor del diccionario

  print(params['Accept'])
  print(params['Accept-Encoding'])
  print(response.url)


getMethod()