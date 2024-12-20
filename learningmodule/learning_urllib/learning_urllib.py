import urllib.parse

url = "http://47.111.104.162:30301/web-api/role/find-page"



def url_to_method_name(url):
    # 移除非法字符，替换为下划线
    return url.replace('.', '_').replace('/', '_').replace(':', '_')

method_name = url_to_method_name(url)
print(url)
print(method_name)