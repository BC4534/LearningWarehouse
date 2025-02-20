import asyncio
from mitmproxy.addons.proxyserver import Proxyserver
from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from addons import Counter

async def start_proxy(listen_port: int = 8080, listen_host: str = '127.0.0.1', mode: list = None) -> None:
    """
    启动 mitmproxy 代理服务器。

    :param listen_port: 监听端口，默认为 8080。
    :param listen_host: 绑定的主机，默认为 '127.0.0.1'。
    :param mode: 代理模式，默认为 ['socks5']。
    """
    # 创建 Options 实例，配置代理服务器选项
    options = Options(
        listen_port=listen_port,
        listen_host=listen_host,
        mode = mode or ['socks5']
    )
    # 创建 DumpMaster 实例，传入配置选项
    dm = DumpMaster(options=options)
    # 设置代理服务器
    dm.server = Proxyserver()
    # 添加 Counter 插件，传入必要的参数
    dm.addons.add(Counter(
        file_system_loader_path=r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2',
        template_file='templates.txt',
        output_file=r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2\outfile.py',
        headers_host_list=['mms.sermatec-cloud.com', '47.111.104.162:30301', '192.168.1.82:3322']
    ))
    # 异步运行代理服务器
    await dm.run()

if __name__ == '__main__':
    # 启动异步事件循环，并运行 start_proxy 函数
    asyncio.run(start_proxy())