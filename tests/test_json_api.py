import http

import allure
import pytest

from api.json_placeholder_api.models import Post, Comment


@allure.title("Тест на получение всех postoв")
def test_get_all_posts(json_placeholder_api):
    response = json_placeholder_api.get_posts()

    assert response.status_code == http.HTTPStatus.OK

    all_posts = response.json()
    assert len(all_posts) == 100, "вернулось постов не 100"
    for post in all_posts:
        Post(**post)


@allure.title("тест на получение всех комментариев")
def test_get_all_comments(json_placeholder_api):
    response = json_placeholder_api.get_comments()
    assert response.status_code == http.HTTPStatus.OK
    all_comments = response.json()
    assert len(all_comments) == 500, "вернулось не 500 комментов"

    for comments in all_comments:
        Comment(**comments)


@allure.title("тест на получение поста по айди")
@pytest.mark.parametrize("post_id", ["1", "100", "57"])
def test_get_post_by_id(json_placeholder_api, post_id):
    response = json_placeholder_api.get_post_by_id(post_id)
    assert response.status_code == http.HTTPStatus.OK
    Post(**response.json())
#