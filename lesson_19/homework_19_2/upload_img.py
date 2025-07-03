import requests

class UploadImage:
    def __init__(self, base_url, image_path):
        self.base_url = base_url
        self.image_path = image_path
        self.upload_endpoint = 'upload'

    def upload_image(self):
        with open(self.image_path, 'rb') as img:
            files = {'image': img}
            response = requests.post(f'{self.base_url}/{self.upload_endpoint}', files=files)
            assert response.status_code == 201, f'Status code is not 201, but {response.status_code}'

        return response


