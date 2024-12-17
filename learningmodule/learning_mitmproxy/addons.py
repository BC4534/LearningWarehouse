from common.logger_handler import logger

from mitmproxy import http


class Counter:

    def request(self, flow: http.HTTPFlow) -> None:
        try:
            req = flow.request
            if req.host in ['mms.sermatec-cloud.com', '47.111.104.162:30301'] and req.method == 'POST':
                logger.info("请求 api: {}".format(flow.request.url))
                logger.info("请求 方法: {}".format(flow.request.method))
                logger.info("请求 头部: {}".format(flow.request.headers))
                logger.info("请求 内容: {}".format(flow.request.content))
        except Exception as e:
            logger.error("处理请求时发生错误: {}".format(e))

    def response(self, flow: http.HTTPFlow) -> None:
        try:
            res = flow.response
            if flow.request.method == 'POST':
                logger.info("响应 状态码: {}".format(flow.response.status_code))
                logger.info("响应 原因: {}".format(flow.response.reason))
                logger.info("响应 头部: {}".format(flow.response.headers))
                logger.info("响应 内容: {}".format(flow.response.content))
                cookies = '; '.join('{}={}'.format(k, v) for k, v in flow.response.cookies.items())
                if cookies:
                    logger.info("响应 Cookies: {}".format(cookies))
        except Exception as e:
            logger.error("处理响应时发生错误: {}".format(e))


addons = [
    Counter()
]

