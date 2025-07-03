from lesson_19.homework_19_2.get_img import GetImage
from lesson_19.homework_19_2.tests.conftest import BASE_URL, IMAGE

def test_get_image_by_name(upload_image_fixture):
    get_service = GetImage(base_url=BASE_URL)
    response = get_service.get_image(filename=IMAGE)
    assert 'image_url' in response.json()

