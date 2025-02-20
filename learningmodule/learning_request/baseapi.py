import os
import requests
import allure
from common.logger_handler import logger


class BaseApi:
    """
    封装请求方法，方便后续调用
    """
    # 初始化日志记录器
    def __init__(self):
        self.logger = logger


    def _log_request(self, method, url, params=None, data=None, json=None):
        self.logger.info(f"发起{method.upper()}请求: {url}")
        if params:
            self.logger.info(f"查询参数: {params}")
        if data:
            self.logger.info(f"请求数据: data:{data}")
        if json:
            self.logger.info(f"请求数据: json:{json}")

    def _log_response(self, response):
        self.logger.info(f"响应状态码: {response.status_code}")
        try:
            self.logger.info(f"响应数据: {response.json()}")
        except ValueError:
            self.logger.info(f"响应数据: {response.text}")

    def _make_request(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        try:
            self._log_request(method, url, params=params, data=data, json=json)
            response = requests.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)
            self._log_response(response)
            return response
        except requests.RequestException as e:
            self.logger.error(f"请求失败: {e}")
            raise

    @allure.step("get")
    def get(self, url, params=None, **kwargs):
        return self._make_request('GET', url, params=params, **kwargs)

    @allure.step("post")
    def post(self, url, data=None, json=None, headers=None, **kwargs):
        return self._make_request('POST', url, data=data, json=json, headers=headers, **kwargs)

    @allure.step("put")
    def put(self, url, data=None, json=None, headers=None, **kwargs):
        return self._make_request('PUT', url, data=data, json=json, headers=headers, **kwargs)

    @allure.step("delete")
    def delete(self, url, data=None, json=None, headers=None, **kwargs):
        return self._make_request('DELETE', url, data=data, json=json, headers=headers, **kwargs)

    def request(self, method, url, data=None, json=None, headers=None, **kwargs):
        method = method.lower()
        return self._make_request(method, url, data=data, json=json, headers=headers, **kwargs)

    # 获取响应状态码
    def get_status_code(self, response):
        self.logger.info(f"获取响应状态码: {response.status_code}")
        return response.status_code

    # 获取响应头
    def get_headers(self, response):
        self.logger.info(f"获取响应头: {response.headers}")
        return response.headers

    # 获取响应文本
    def get_text(self, response):
        self.logger.info(f"获取响应文本: {response.text}")
        return response.text

    # 获取响应json
    def get_json(self, response):
        self.logger.info(f"获取响应json: {response.json()}")
        return response.json()


if __name__ == '__main__':
    url = "http://47.111.104.162:30301/web-api/open/login"
    username = os.getenv('USERNAME', 'admin')
    password = os.getenv('PASSWORD', '*sermatecroot24')
    data = {"username": username, "password": password}
    headers = {"Content-Type": "application/json"}
    try:
        BaseApi().post(url=url, json=data, headers=headers)
    except requests.RequestException as e:
        print(f"请求失败: {e}")
