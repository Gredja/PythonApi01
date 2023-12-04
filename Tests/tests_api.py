import json
from Constants import Constants
from Helpers.RequestExecutor import RequestExecutor
from Helpers.Checkers import is_variable_in_collection
from Tests.base.api_base_test import TestApiBaseClass
from Tests.base.base_test import TestBaseClass
from urllib.parse import urljoin
from Enums.RequestMethodEnum import RequestMethod

from Validators import JsonSchemas
from Validators.JsonSchemaValidator import JsonSchemaValidator


class TestApiClass(TestApiBaseClass):
    def test_store_inventory(self):
        rel = TestBaseClass().configuration.api.Api.version + '/store/inventory'
        url = urljoin(TestBaseClass().configuration.api.Api.baseUrl, rel)

        response = RequestExecutor.http_request_executor(url=url, request_method=RequestMethod.GET)
        errors = JsonSchemaValidator.validate(json_data=json.loads(response.data),
                                              schema=JsonSchemas.Schemas.store_inventory_schema)

        assert len(errors) is 0
        assert is_variable_in_collection(response.status, Constants.HTTP_SUCCESS) is True
