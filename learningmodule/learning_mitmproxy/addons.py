from common.logger_handler import logger
from learningmodule.learing_jinja2.learing_jinja2 import Writer_Api_Files
from mitmproxy import http


class Counter:
    def __init__(self, file_system_loader_path, template_file, output_file, url_list):
        self.count = 0
        self.writer = Writer_Api_Files(file_system_loader_path, template_file, output_file)
        self.url_list = url_list

    def url_to_method_name(self, url):
        # 移除非法字符，替换为下划线
        return url.replace('.', '_').replace('/', '_').replace(':', '_').replace('-', '_')

    def request(self, flow: http.HTTPFlow, url_list) -> None:
        logger.info(f"请求计数器: {self.count}")
        self.count += 1
        try:
            req = flow.request
            if req.headers['Host'] in self.url_list and req.method in ['POST', 'GET', 'DELETE',
                                                                       'PUT']:  # 对请求的URL进行过滤，只处理特定的请求
                logger.info(f"请求URL: {req.url}")
                logger.info(f"请求方法: {req.method}")
                logger.info(f"Content-Type: {req.headers['Content-Type']}")
                logger.info(f"Authorization: {req.headers['Authorization']}")
                logger.info(f"请求内容: {req.content.decode('utf-8')}")
                self.writer.create_template_render(
                    title=self.url_to_method_name(req.url),
                    method=req.method,
                    url=req.url,
                    content_type=req.headers['Content-Type'],
                    authorization=req.headers['Authorization'],
                    content=req.content.decode('utf-8'),
                )
        except Exception as e:
            logger.error(f"处理请求时发生错误: {e}")

    def response(self, flow: http.HTTPFlow) -> None:
        logger.info(f"响应计数器: {self.count}")
        self.count += 1
        try:
            logger.info(f"响应 状态码: {flow.response.status_code}")
            logger.info(f"响应 原因: {flow.response.reason}")
            logger.info(f"响应 头部: {flow.response.headers}")
            logger.info(f"响应 内容: {flow.response.content}")
            cookies = '; '.join(f'{k}={v}' for k, v in flow.response.cookies.items())
            if cookies:
                logger.info(f"响应 Cookies: {cookies}")
        except Exception as e:
            logger.error(f"处理响应时发生错误: {e}")


addons = [
    Counter(
        file_system_loader_path=r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2',
        template_file='templates.txt',
        output_file=r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2\outfile.py',
        url_list=['mms.sermatec-cloud.com', '47.111.104.162:30301', '192.168.1.82:3322']
    )
]
