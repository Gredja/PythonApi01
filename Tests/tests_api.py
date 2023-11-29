from Tests.base.api_base_test import TestApiBaseClass
from Tests.base.base_test import TestBaseClass
from urllib.parse import urljoin
import requests


class TestApiClass(TestApiBaseClass):
    def test_registration(self):
        rel = TestBaseClass().configuration.api.Api.version + '/store/inventory'
        url = urljoin(TestBaseClass().configuration.api.Api.baseUrl, rel)

        response = requests.get(url)

        assert str(response.status_code).startswith('20')
