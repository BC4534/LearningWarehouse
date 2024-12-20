import asyncio
from mitmproxy.addons.proxyserver import Proxyserver
from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from addons import Counter


async def start_proxy(listen_port = 8080,listen_host = '127.0.0.1', mode =None ):
    dm = DumpMaster(options=Options(
        listen_port = listen_port,
        listen_host = listen_host,
        mode = ['socks5']
    ))
    dm.server = Proxyserver()
    dm.addons.add(Counter())
    await dm.run()

if __name__ == '__main__':
    asyncio.run(start_proxy())