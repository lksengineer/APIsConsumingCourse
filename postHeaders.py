# Packages

import requests


def postHeaders():
  """Post in the headers"""

  URL = 'https://httpbin.org/post'

  headers = {
    'course': 'Python',
    'version': '2.0',
    'author': 'Engineer, Developer Luis Kennedy Saavedra'
  }

  response = requests.post(URL, headers=headers)
  print(response.text)

  if response.status_code == 200:
    payload = response.json()
    print('\n', payload)
    print('\n', payload['headers'])

    paramsHeaders = payload['headers']
    print('\n', paramsHeaders['Author'])
    print(paramsHeaders['Course'])
    print(paramsHeaders['Version'])


postHeaders()
