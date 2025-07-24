import pytest
import requests
import logging

logging.basicConfig(
    filename='test_search.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def base_url():
    return "http://127.0.0.1:8080"


@pytest.fixture(scope="class")
def auth_session(base_url):
    session = requests.Session()
    auth_service = 'auth'
    credentials = ("test_user", "test_pass")

    response = session.post(f"{base_url}/{auth_service}", auth=credentials)

    assert response.status_code == 200, f"Login failed: status code {response.status_code}, response: {response.text}"

    access_token = response.json().get("access_token")
    assert access_token, "No access token in response"
    logger.info(f"Access token received: {access_token[:10]}... (length access_token: {len(access_token)})")

    session.headers.update({"Authorization": f"Bearer {access_token}"})
    return session