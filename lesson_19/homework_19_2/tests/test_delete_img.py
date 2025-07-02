from lesson_19.homework_19_2.delete_img import DeleteImage
from lesson_19.homework_19_2.tests.conftest import BASE_URL, IMAGE

def test_delete_image_by_name(upload_image_fixture):
    get_service = DeleteImage(base_url=BASE_URL)
    response = get_service.delete_image(filename=IMAGE)
    expected_response = {'message': f'Image {IMAGE} deleted'}
    assert response.json() == expected_response