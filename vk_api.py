import requests


class Vk:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_users_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'user_ids': self.id, 'album_id': 'profile'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()