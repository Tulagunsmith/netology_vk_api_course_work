from vk_api import Vk
from pprint import pprint
from tokens import vk_token
from tokens import user_id
from tokens import yandex_token
from yandex_api_class import YaUploader


def photos_upload_quantity(photos_list):
    photos = input('How many photos would you like to upload?')
    if not photos.isdigit() or int(photos) > len(photos_list):
        return 5
    else:
        return int(photos)


if __name__ == '__main__':
    user_id_number = user_id
    access_token = vk_token
    album_owner_id = input('Input album owner id: ')
    vk = Vk(access_token, user_id_number)
    user_photo = vk.get_photo_url(album_owner_id)
    photo_quantity = photos_upload_quantity(user_photo)
    directory = input('Input the name of the directory: ')
    yandex = YaUploader(token=yandex_token)
    yandex.create_dir(dir_name=directory)
    for item in user_photo[:photo_quantity]:
        yandex.upload_file(dir_name=directory, file_name=item['file_name'], file_url=item['photo_url'], file_date=item['date'])
