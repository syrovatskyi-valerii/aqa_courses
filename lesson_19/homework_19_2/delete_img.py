import requests
from lesson_19.homework_19_2.tests.conftest import BaseAPITest

class DeleteImage(BaseAPITest):
    def __init__(self, base_url):
        self.base_url = base_url
        self.delete_endpoint = 'delete'

    def delete_image(self, filename):

        response = requests.delete(f'{self.base_url}/{self.delete_endpoint}/{filename}')

        assert response.status_code == 200, f'Status code is not 200, but {response.status_code}'

        return response
