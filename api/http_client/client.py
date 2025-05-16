from typing import Optional

import allure
import requests


class HttpClient:
    def __init__(self, host: str, default_headers: Optional[dict] = None):
        self.host = host
        self.default_headers = default_headers

    @allure.step("отправка get запроса")
    def get(self, route: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> requests.Response:
        response = requests.get(self.host + route, headers=headers, params=params)
        return response

    @allure.step("отправка post запроса")
    def post(self, route: str, headers: Optional[dict] = None, json: Optional[dict] = None,
             data: Optional[dict] = None) -> requests.Response:
        response = requests.post(self.host + route, headers=headers, json=json, data=data)
        return response





