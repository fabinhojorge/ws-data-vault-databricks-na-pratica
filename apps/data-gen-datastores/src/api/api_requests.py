"""
https://random-data-api.com/api/
"""

import numpy as np
import requests
from datetime import datetime
from requests.exceptions import HTTPError


class Requests(object):

    @staticmethod
    def gen_user_id():
        return np.random.randint(1, 10000, size=100)

    @staticmethod
    def gen_timestamp():
        current_datetime = datetime.now()
        formatted_timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        return formatted_timestamp

    @staticmethod
    def api_get_request(url, params):

        dt_request = requests.get(url=url, params=params)
        for url in [url]:
            try:
                response = requests.get(url)
                response.raise_for_status()
                dict_request = dt_request.json()

            except HTTPError as http_err:
                print(f'http error occurred: {http_err}')
            except Exception as err:
                print(f'api not available at this moment: {err}')
            else:
                return dict_request
