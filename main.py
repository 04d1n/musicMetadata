import json
import requests

# response = requests.get("https://musicbrainz.org/ws/2/")
# print(response.status_code)
response = requests.get("https://musicbrainz.org/ws/2/")
url = "https://musicbrainz.org/ws/2/"
payload = {'artist': 'Linkin Park'}

post = requests.post(url, data=json.dumps(payload))

respuesta = response.json()['al']
print(respuesta)
