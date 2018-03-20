from pprint import pprint
from urllib.parse import urlencode
import requests

APP_ID = 6417385
AUTH_URL ='https://oauth.vk.com/authorize'

auth_data = {
    'client_id' : APP_ID,
    'display' : 'mobile',
    'scope' : 'friends, status',
    'response_type' : 'token',
    'v' : '5.73'
}


# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '81a544d5640cd70f4e1c5442a8668ac48cde19954046db34121196c41f5a62f0cfd8fdef1150734c7c77c'

params = {
    'access_token' : TOKEN,
    'v' : '5.73'
}

response = requests.get('https://api.vk.com/method/status.get', params)

pprint(response.text)

