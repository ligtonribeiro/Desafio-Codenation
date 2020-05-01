import requests
from decouple import config

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token="+config('TOKEN')

files = [
    ('answer', open('answer.json', 'rb'))
]

headers = {}

response = requests.post(url, headers=headers, files=files)

print(response.text.encode('utf-8'))
