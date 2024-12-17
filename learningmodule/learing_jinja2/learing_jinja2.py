from jinja2 import Environment,FileSystemLoader

evn = Environment(loader=FileSystemLoader(r'D:\CODE\LearningWarehouse\learningmodule\learing_jinja2'))
template = evn.get_template('templates.txt')
outfile = template.render(
    title = 'login',
    method='\'POST\'',
    url='\'http://www.baid1u.com\'',
    headers={'Content-Type':'application/json'},
    data ={'username':'admin','password':'123456'},
    json = {}
)
print(outfile)
# 将outfile写入文件
with open('outfile.py','a',encoding='utf-8') as f:
    f.write(outfile)