from jinja2 import Environment, FileSystemLoader


class Writer():
    def __init__(self):
        # 初始化 Jinja2 环境，设置模板加载路径
        self.env = Environment(loader=FileSystemLoader(r'D:\\CODE\\LearningWarehouse\\learningmodule\\learing_jinja2'))
        print("Jinja2 environment initialized.")

    def write_request_api(self, content, outfile):
        """
        将渲染后的模板内容写入指定文件。

        :param content: 渲染后的模板内容
        :param outfile: 输出文件名
        """
        try:
            with open(outfile, 'a', encoding='utf-8') as f:
                f.write(content + '\n')  # 添加换行符，便于多次调用时内容不连在一起
            print(f"Content written to {outfile}")
        except Exception as e:
            print(f"Error writing to file {outfile}: {e}")

    def create_template_render(self, title, method, url, headers, data, json_data, cookies):
        """
        根据传入的参数渲染模板，并将渲染后的内容写入文件。

        :param title: 请求标题
        :param method: HTTP 方法 (如 GET, POST)
        :param url: 请求 URL
        :param headers: 请求头字典
        :param data: 请求数据字典
        :param json_data: 请求 JSON 数据字典
        :param cookies: 请求 Cookie 字典
        """
        try:
            # 获取模板文件
            template = self.env.get_template('templates.txt')
            print("Template loaded successfully.")
            # 渲染模板
            outfile_content = template.render(
                title=title,
                method=method,
                url=url,
                headers=headers,
                data=data,
                json=json_data,
                cookies=cookies
            )
            print("Template rendered successfully.")
            # 将渲染后的内容写入文件
            self.write_request_api(outfile_content,
                                   r'D:\\CODE\\LearningWarehouse\\learningmodule\\learing_jinja2\\output.py')  # 指定输出文件路径
        except Exception as e:
            # 打印异常信息
            print(f"Error rendering template: {e}")


if __name__ == '__main__':
    writer = Writer()
    # 调用方法创建模板渲染并写入文件
    writer.create_template_render(
        title='test',
        method='GET',
        url='http://www.baidu.com',
        headers={'Content-Type': 'application/json'},
        data={'key': 'value'},
        json_data={'username': 'admin', 'password': '123456'},
        cookies={'session_id': 'abc123'}
    )
