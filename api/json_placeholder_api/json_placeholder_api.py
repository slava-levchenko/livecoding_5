import allure
import requests

from api.http_client.client import HttpClient
from enum import StrEnum

class JsonPlaceholderRoute:
    POSTS = "/posts"
    COMMENTS = "/comments"

class JsonPlaceholderApi:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._http_client = HttpClient(base_url)


    @allure.step("получение всех постов")
    def get_posts(self) -> requests.Response:
        response = self._http_client.get(JsonPlaceholderRoute.POSTS)
        return response

    @allure.step("получение поста по айди {post_id}")
    def get_post_by_id(self, post_id: str) -> requests.Response:
        response = self._http_client.get(f"{JsonPlaceholderRoute.POSTS}/{post_id}")
        return response


    @allure.step("получение всех комментариев")
    def get_comments(self) -> requests.Response:
        response = self._http_client.get(JsonPlaceholderRoute.COMMENTS)
        return response



#