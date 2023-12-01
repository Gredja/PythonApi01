from Constants import Constants
from Helpers.RequestExecutor import RequestExecutor
from Helpers.Checkers import is_variable_in_collection
from Tests.base.api_base_test import TestApiBaseClass
from Tests.base.base_test import TestBaseClass
from urllib.parse import urljoin
from Enums.RequestMethodEnum import RequestMethod


class TestApiClass(TestApiBaseClass):
    def test_registration(self):
        rel = TestBaseClass().configuration.api.Api.version + '/store/inventory'
        url = urljoin(TestBaseClass().configuration.api.Api.baseUrl, rel)

        response = RequestExecutor.http_request_executor(url=url, request_method=RequestMethod.GET)
        print(response.json())

        assert is_variable_in_collection(response.status, Constants.HTTP_SUCCESS) is True
