import requests
import json


token_source_user = input("type token")
first_user = input("type the id first user ")
second_user = input("type the id second user ")


def mutual_friend(first_id, second_id, TOKEN):
    params = {'access_token': TOKEN, 'v': '5.73', 'source_uid': first_id, 'target_uid': second_id}
    response_friends = requests.get('https://api.vk.com/method/friends.getMutual', params)
    friends_link = json.loads(response_friends.text)
    link_vk = 'https://vk.com/id'
    for user_id in friends_link['response']:
        print('id user = {}'.format(user_id))
        print(link_vk + str(user_id))


mutual_friend(first_user, second_user, token_source_user)



