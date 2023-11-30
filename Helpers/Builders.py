import requests
from requests.auth import HTTPBasicAuth


class Builders:
    @staticmethod
    def http_request_builder(url, is_headers_needed=True, body=None, user_name=None, token=None):
        is_post_request = False
        headers = {"Content-Type": "application/json; charset=utf-8"}

        if body is not None:
            is_post_request = True

        try:
            response = requests.get(url)
            response.raise_for_status()
            # If the request fails (404) then print the error.
        except requests.exceptions.HTTPError as error:
            print(error)

        requests.

        return requests.get(url, headers=headers)
