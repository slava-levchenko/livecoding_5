

import pytest

from api.json_placeholder_api.json_placeholder_api import JsonPlaceholderApi
from config.config import JSONPlaceholderConfig


@pytest.fixture
def json_placeholder_api() -> JsonPlaceholderApi:
    return JsonPlaceholderApi(base_url=JSONPlaceholderConfig.BASE_URL)
#