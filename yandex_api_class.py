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
        if response.status_code == 404:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            upload_path = f'{dir_name}/{file_name}'
            # file_url = 'https://sun1-88.userapi.com/impf/4ZoyoamCuqCTBMvJRACC34hZJ5gwmTMJVzcZfA/MkPV5C3t7hM.jpg?size=1620x2160&quality=96&sign=93bf73b835c03657fb27fae9748441ec&c_uniq_tag=4Wzv77FjOmjE34dx4uXLyc4VqVQPUsAi0G5q2CRuico&type=album'
            params = {
                'path': upload_path,
                'url': file_url,
                'overwrite': 'true'
            }
            response = requests.post(url=url, headers=self.headers, params=params)
            return response.json()
        else:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            upload_path = f'{dir_name}/{str(file_name) + str(file_date)}'
            params = {
                'path': upload_path,
                'url': file_url,
                'overwrite': 'true'
            }
            response = requests.post(url=url, headers=self.headers, params=params)
            return response.json()
