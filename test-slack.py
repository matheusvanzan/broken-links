import json
import requests


url = ''

data = {
    'text': 'Esta é uma linha de texto no canal.\nE esta é outra linha de texto.'
}

response = requests.post(url, json.dumps(data))

print(response)