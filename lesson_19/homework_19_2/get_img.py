import requests

class GetImage:
    def __init__(self, base_url):
        self.base_url = base_url
        self.image_endpoint = 'image'

    def get_image(self, filename):
        response = requests.get(url=f'{self.base_url}/{self.image_endpoint}/{filename}',
                                headers={'Content-Type': 'text'})
        assert response.status_code == 200, f'Status code is not 200, but {response.status_code}'

        return response

