import requests
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BaseRequest:
    def __init__(self):
        # 初始化会话
        self.session = requests.Session()
        # 设置默认的超时时间
        self.default_timeout = 10

    def __enter__(self):
        # 进入上下文管理器时返回自身实例
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出上下文管理器时关闭会话
        self.close()
        if exc_type is not None:
            # 若有异常发生，记录异常信息
            logging.error(f"An exception occurred: {exc_type.__name__} - {exc_val}", exc_info=True)

    def _request(self, method, url, response_handler=None, **kwargs):
        try:
            # 如果没有提供超时参数，使用默认超时时间
            if 'timeout' not in kwargs:
                kwargs['timeout'] = self.default_timeout
            # 发送请求
            response = self.session.request(method, url, **kwargs)
            # 检查响应状态码，如果不是 200 系列，抛出异常
            response.raise_for_status()
            if response_handler:
                # 如果提供了自定义的响应处理函数，调用该函数处理响应
                return response_handler(response)
            return response
        except requests.exceptions.RequestException as e:
            # 记录请求异常信息
            logging.error(f"Request failed: {e}")
            return None
        except Exception as e:
            # 记录其他异常信息
            logging.error(f"An unexpected error occurred: {e}", exc_info=True)
            return None

    def get(self, url, response_handler=None, **kwargs):
        # 调用 _request 方法发送 GET 请求
        return self._request('GET', url, response_handler=response_handler, **kwargs)

    def post(self, url, response_handler=None, **kwargs):
        # 调用 _request 方法发送 POST 请求
        return self._request('POST', url, response_handler=response_handler, **kwargs)

    def put(self, url, response_handler=None, **kwargs):
        # 调用 _request 方法发送 PUT 请求
        return self._request('PUT', url, response_handler=response_handler, **kwargs)

    def delete(self, url, response_handler=None, **kwargs):
        # 调用 _request 方法发送 DELETE 请求
        return self._request('DELETE', url, response_handler=response_handler, **kwargs)

    def close(self):
        try:
            # 关闭会话
            self.session.close()
            logging.info("Session closed successfully.")
        except Exception as e:
            # 记录关闭会话时的异常信息
            logging.error(f"Failed to close session: {e}", exc_info=True)

    @staticmethod
    def parse_json(response):
        """将响应内容解析为 JSON 格式"""
        try:
            return response.json()
        except ValueError:
            logging.error("Failed to parse response as JSON.")
            return None

    @staticmethod
    def get_status_code(response):
        """获取响应的状态码"""
        return response.status_code if response else None

    @staticmethod
    def get_text(response):
        """获取响应的文本内容"""
        return response.text if response else None