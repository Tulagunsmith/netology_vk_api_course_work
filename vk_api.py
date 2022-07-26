import requests
import time
from datetime import datetime
from progress.bar import ChargingBar


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
        if 'error' in response.keys():
            print('Incorrect data!')
            return
        else:
            raw_list = response['response']['items']
            photo_json = []
            bar = ChargingBar('Getting photo URLs', max=len(raw_list), suffix='%(percent)d%%')
            for item in raw_list:
                sizes = item['sizes']
                likes = item['likes']['count']
                date = datetime.utcfromtimestamp(item['date']).strftime('%Y-%m-%d')
                photo_info = {}
                for photo in sizes:
                    photo_info['size'] = 'a'
                    photo_info['file_name'] = likes
                    photo_info['date'] = date
                    if photo['type'] == 'w':
                        photo_info['photo_url'] = photo['url']
                        photo_info['size'] = photo['type']
                        break
                    elif ord(photo_info['size']) <= ord(photo['type']):
                        photo_info['size'] = photo['type']
                        photo_info['photo_url'] = photo['url']
                bar.next()
                time.sleep(0.3)
                photo_json.append(photo_info)
            bar.finish()
            print(f'Total URLs got: {len(photo_json)}')
            return photo_json
