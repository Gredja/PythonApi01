import json
import datetime
from Constants import Constants
from Helpers.RequestExecutor import RequestExecutor
from Helpers.Checkers import is_variable_in_collection
from Tests.base.api_base_test import TestApiBaseClass
from Tests.base.base_test import TestBaseClass
from urllib.parse import urljoin
from Enums.RequestMethodEnum import RequestMethod

from Validators.JsonSchemas import Schemas
from Validators.JsonSchemaValidator import JsonSchemaValidator
from Requests.Models.OrderCreateRequest import OrdersCreateRequest


class TestApiClass(TestApiBaseClass):
    def test_store_inventory(self):
        rel = TestBaseClass().configuration.api.Api.version + '/store/inventory'
        url = urljoin(TestBaseClass().configuration.api.Api.baseUrl, rel)

        response = RequestExecutor.http_request_executor(url=url, request_method=RequestMethod.GET)
        errors = JsonSchemaValidator.validate(json_data=json.loads(response.data),
                                              schema=Schemas.store_inventory_schema)

        assert len(errors) is 0
        assert is_variable_in_collection(response.status, Constants.HTTP_SUCCESS) is True

    def test_create_order(self):
        rel = TestBaseClass().configuration.api.Api.version + '/store/order'
        url = urljoin(TestBaseClass().configuration.api.Api.baseUrl, rel)

        order = OrdersCreateRequest(1, 1, 100, "2023-12-05T11:53:47.836+0000", "placed", True).to_json()
        response = RequestExecutor.http_request_executor(url=url, request_method=RequestMethod.POST, body=order)

        assert is_variable_in_collection(response.status, Constants.HTTP_SUCCESS) is True
