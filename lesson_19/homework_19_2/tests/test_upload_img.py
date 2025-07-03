from lesson_19.homework_19_2.upload_img import UploadImage
from lesson_19.homework_19_2.tests.conftest import BASE_URL, IMAGE

upload_service = UploadImage(base_url=BASE_URL,image_path=IMAGE)

def test_upload_img():
    response = upload_service.upload_image()
    expected_response = {'image_url': f'{BASE_URL}/uploads/{IMAGE}'}
    assert response.json() == expected_response