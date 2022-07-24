import requests


class YaUploader:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_dir(self, dir_name):
        put_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': dir_name}
        response = requests.get(url=put_url, headers=self.headers, params=params)
        if response.status_code == 404:
            params = {'path': dir_name, 'overwrite': 'true'}
            requests.put(url=put_url, headers=self.headers, params=params)
            # return response.json()
            print('Directory created.')
        else:
            print('Directory already exists.')

    def upload_file(self, dir_name, file_name, file_url, file_date):
        put_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': f'{dir_name}/{file_name}'}
        response = requests.get(url=put_url, headers=self.headers, params=params)
        if response.status_code == 200:
            upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            upload_path = f'{dir_name}/{str(file_name) + " " + str(file_date)}'
            params = {
                'path': upload_path,
                'url': file_url
            }
            response = requests.post(url=upload_url, headers=self.headers, params=params)
            print('Photo with such name already exists. Renaming the photo...')
            return response.json()
        elif response.status_code > 200:
            upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            upload_path = f'{dir_name}/{file_name}'
            params = {
                'path': upload_path,
                'url': file_url
            }
            response = requests.post(url=upload_url, headers=self.headers, params=params)
            print('Copying photo!..')
            return response.json()

