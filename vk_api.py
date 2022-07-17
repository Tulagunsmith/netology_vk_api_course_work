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

    def get_photo_url(self, album_owner):
        url = 'https://api.vk.com/method/photos.get'
        params = {'user_ids': self.id, 'album_id': 'profile', 'extended': '1', 'owner_id': album_owner}
        response = requests.get(url, params={**self.params, **params})
        response = response.json()
        raw_list = response['response']['items']
        photo_json = []
        for item in raw_list:
            sizes = item['sizes']
            likes = item['likes']['count']
            photo_id = item['id']
            date = item['date']
            photo_info = {}
            for photo in sizes:
                photo_info['size'] = 'a'
                photo_info['likes'] = likes
                photo_info['date'] = date
                if photo['type'] == 'w':
                    photo_info[photo_id] = photo['url']
                    photo_info['size'] = photo['type']
                    break
                elif ord(photo_info['size']) <= ord(photo['type']):
                    photo_info['size'] = photo['type']
                    photo_info[photo_id] = photo['url']
            photo_json.append(photo_info)
        return photo_json
