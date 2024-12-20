from jinja2 import Environment, FileSystemLoader
from common.logger_handler import logger

class Writer_Api_Files():
    def __init__(self, file_system_loader_path, template_file, output_file):
        """
        初始化Writer_Api_Files类。

        :param file_system_loader_path: 模板文件路径
        :param template_file: 模板文件名
        :param output_file: 输出文件路径
        """
        self.file_system_loader_path = file_system_loader_path
        self.template_file = template_file
        self.output_file = output_file
        # 初始化 Jinja2 环境，设置模板加载路径
        self.env = Environment(loader=FileSystemLoader(self.file_system_loader_path))
        logger.info("Jinja2环境初始化成功。")

    def write_request_api(self, content, outfile):
        """
        将渲染后的模板内容写入指定文件。

        :param content: 渲染后的模板内容
        :param outfile: 输出文件名
        """
        try:
            with open(outfile, 'a', encoding='utf-8') as f:
                f.write(content + '\n')  # 添加换行符，便于多次调用时内容不连在一起
            logger.info(f"内容已写入 {outfile}")
        except Exception as e:
            logger.error(f"写入文件 {outfile} 时出错: {e}")

    def create_template_render(self, title, method, url, content_type, authorization, content):
        """
        根据传入的参数渲染模板，并将渲染后的内容写入文件。

        :param title: 请求标题
        :param method: HTTP 方法 (如 GET, POST)
        :param url: 请求 URL
        :param content_type: 内容类型
        :param authorization: 授权信息
        :param content: 请求内容
        """
        try:
            # 获取模板文件
            template = self.env.get_template(self.template_file)
            logger.info("模板加载成功。")
            # 渲染模板
            outfile_content = template.render(
                title=title,
                method=method,
                url=url,
                content_type=content_type,
                authorization=authorization,
                content=content
            )
            logger.info("模板渲染成功。")
            # 将渲染后的内容写入文件
            self.write_request_api(outfile_content, self.output_file)  # 指定输出文件路径
        except Exception as e:
            # 打印异常信息
            logger.error(f"渲染模板时出错: {e}")


if __name__ == '__main__':
    writer = Writer_Api_Files(
        file_system_loader_path=r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2',
        template_file='templates.txt',
        output_file=r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2\outfile.py'
    )
    # 调用方法创建模板渲染并写入文件
    writer.create_template_render(
        title='test',
        method='GET',
        url='http://www.baidu.com',  # 确保URL正确
        content_type='application/json',
        authorization='',
        content=''
    )