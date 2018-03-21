from pprint import pprint
from urllib.parse import urlencode
import requests
import json
import os

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

TOKEN = '4026506e0ed143175146a5bfd3d4da192e8c36300f80888eb53c68ded54b22f079075d4e377e0dadf679e'

params = {
    'access_token' : TOKEN,
    'v' : '5.73'
}
#
# params['text'] = 'status from python'
# params = {
#     'access_token' : TOKEN,
#     'text' : 'status from python',
#     'v' : '5.73'
# }

# response = requests.get('https://api.vk.com/method/status.get', params)
# response = requests.get('https://api.vk.com/method/wall.get', params)
# response = requests.get('https://api.vk.com/method/wall.post', params)
# first_user = input("type the id first user ")
# second_user = input("type the id second user ")

# 157312,212696
# params['users_id'] = 157312 , 212696
# params['fields'] = 'link'
# response_link = requests.get('https://api.vk.com/method/users.get', params)
#
# pprint(response_link.text)


def mutual_friend():
    params['source_uid'] = '135282071'
    params['target_uid'] = '95904836'
    # params['source_uid'] = first_id
    # params['target_uid'] = second_id
    response_friends = requests.get('https://api.vk.com/method/friends.getMutual', params)
    pprint(response_friends.text)

    friends_link = json.loads(response_friends.text)
    print(friends_link)
    # all_id = friends_link['response']
    # print(all_id)
    link_vk = 'https://vk.com/id'
    for user_id in friends_link['response']:
        print('id user = {}'.format(user_id))
        print(link_vk + str(user_id))
    # print(friends_link)
    # print(type(friends_link))


# mutual_friend(first_user,second_user)
mutual_friend()
# response_set = requests.get('https://api.vk.com/method/status.set', params)
#
# pprint(response.text)
# response = requests.get('https://api.vk.com/method/status.get', params)
# print(response_set.text)
# pprint(response.text)