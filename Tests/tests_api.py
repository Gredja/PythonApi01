from Constants import Constants
from Helpers.Builders import Builders
from Helpers.Checkers import is_variable_in_collection
from Tests.base.api_base_test import TestApiBaseClass
from Tests.base.base_test import TestBaseClass
from urllib.parse import urljoin
import requests


class TestApiClass(TestApiBaseClass):
    def test_registration(self):
        rel = TestBaseClass().configuration.api.Api.version + '/store/inventory'
        url = urljoin(TestBaseClass().configuration.api.Api.baseUrl, rel)

        response = Builders.http_request_builder(url=url);

        assert is_variable_in_collection(response.status_code, Constants.HTTP_SUCCESS) is True
