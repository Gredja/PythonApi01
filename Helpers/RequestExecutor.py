import urllib3
import logging

from Enums.RequestMethodEnum import RequestMethod
from requests.auth import HTTPBasicAuth


class RequestExecutor:
    @staticmethod
    def http_request_executor(url, request_method=RequestMethod.GET, is_headers_needed=True, body=None, user_name=None,
                              token=None):
        headers = {}

        if is_headers_needed is True:
            headers = {"Content-Type": "application/json; charset=utf-8"}

        http = urllib3.PoolManager()

        try:
            response = http.request(str(request_method.name), url, headers=headers, body=body)
        except response.exceptions.HTTPError as error:
            logging.error(error)

        return response
