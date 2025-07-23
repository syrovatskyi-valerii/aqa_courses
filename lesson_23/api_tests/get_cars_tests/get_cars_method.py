import requests

class GetCars:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.cars_service = 'cars'
        self.session = session


    def get_cars(self,expected_status_code=200, sort_by=None, limit=None):
        query_params = {}
        if sort_by:
            query_params['sort_by'] = sort_by
        if limit:
            query_params['limit'] = limit

        response = self.session.get(f"{self.base_url}/{self.cars_service}", params=query_params)

        assert response.status_code == expected_status_code, \
            f'Status code is not 200, but {response.status_code}'

        return response