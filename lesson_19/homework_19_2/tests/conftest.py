import pytest
from lesson_19.homework_19_2.upload_img import UploadImage

BASE_URL = 'http://127.0.0.1:8080'
IMAGE = 'example_image.jpg'


@pytest.fixture(scope='module')
def upload_image_fixture():
    uploader = UploadImage(base_url=BASE_URL, image_path=IMAGE)
    response = uploader.upload_image()
    assert response.status_code == 201, f'Status code is not 201, but {response.status_code}'
    return response