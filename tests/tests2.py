import configparser
import pytest
import requests

config = configparser.ConfigParser()
config.read('settings.ini')
TOKEN = config['YD']['token']
URL = config['YD']['url']


@pytest.mark.parametrize(
    'token, url, param, folder_name, status',
    (
            (TOKEN, URL, 'path', 'Folder1', 201),
            (TOKEN, URL, 'pathh', 'Folder2', 400),
            ('token', URL, 'path', 'Folder3', 401),
            (TOKEN, URL[:-1], 'path', 'Folder4', 404),
            (TOKEN, URL, 'path', 'Folder1', 409),
    )
)
def test_create_folder(token, url, param, folder_name, status):
    headers = {
        'Authorization': token
    }

    params = {
        param: folder_name
    }

    response = requests.put(
        url, params=params,
        headers=headers
    )

    assert response.status_code == status