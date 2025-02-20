from opcode import opname

from bs4 import BeautifulSoup
import lxml

# 读取 example.html 文件内容。
def read_html(file):
    with open(file,'r',encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml',from_encoding='utf-8')
        return soup
# 从 HTML 内容中提取所有的链接（即 <a> 标签中的 href 属性值）。
def get_all_links(soup):
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
# 去除重复的链接。
# 将提取到的不重复链接保存到一个新的文本文件 links.txt 中，每个链接占一行。
def write_links_txt(links):
    write_links = list(set(links))
    with open('links.txt','w',encoding='utf-8') as f:
        for i in write_links:
            f.write(i+'\n')



if __name__ == '__main__':
    file = 'example.html'
    soup = read_html(file)
    links = get_all_links(soup)
    write_links_txt(links)



