import requests
import pytest

class TestLogin:

    def test_login():
        response = requests.options(
            method='GET',
            url = 'http://www.baid1u.com',
            headers={'Content-Type': 'application/json'},
            cookies=,
            data={'username': 'admin', 'password': '123456'},
            json=json,

        )
        assert response.status_code == 200