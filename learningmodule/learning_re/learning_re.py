# import re
# from re import findall
#
# data = r"""c]hF4~<_F&D>B*6q#[S!DZQDJh0lxCXkn%eqf3-xwY;prF4X9oJrlO$;G0`[y\xCOz}NF4w2nFM;!(G";y$FD]_~t-F>G!kE2;8!hbS\""""
#
# # re.match 从头开始匹配，
# # match = re.match(r"(c]hF4)", data)
# match1 = re.match(r"(F4)", data)
# print(match1.group())
# com = re.compile(r"(c]hF4)")
# match =com.match(data)
# print(match)  # 返回匹配对象
# print(match.group()) # 返回匹配到的字符串
# print(match.groups()) # 返回匹配到的字符串的元组
# print(match.span()) # 返回匹配到的字符串的索引位置
# print(match.start()) # 返回匹配到的字符串的开始索引位置
# print(match.end()) # 返回匹配到的字符串的结束索引位置
# print(match.string) # 返回匹配到的字符串
# print(match.re) # 返回匹配到的正则表达式
#
# # re.search 从 anywhere 开始匹配，不用必须是匹配字符串的头
# search1 = re.search(r"c]hF4", data)
# search = re.search(r"xwY", data)
# # print(search)
# # print(search.group())
# # print(search.span())
#
# # findall 返回所有匹配到的字符串 List
# # find_all = re.findall(r"F4", data)
# # print(find_all)
# # print(len(find_all))
# # for i in findall(r"F4", data):
# #     print(i)
#
# # sub 替换 将匹配到的字符串替换为指定的字符串 返回替换后的字符串
# sub = re.sub(r"F44", "_F4_", data)
# # print(sub)
# # print(data)
#
# # split 分割 将匹配到的字符串分割为多个字符串 list 返回
# split  = re.split(r"F4", data, maxsplit=0)
# # print(split)
# # print(len(split))
# # for i in split:
# #     print(i)
# # print(data)
# data = "hello worldh"
# import re
# pattern = re.compile('E', re.I)
# m = pattern.match(data, 1 )
# print(m)
# print(m.group())、
import re

# 示例字符串
text = "This is a test string with ar in it. re are"

# 正则表达式模式，匹配以 "ar" 结尾的字符串，前面至少有两个字符
pattern = r'..*ar'

# 使用 search 方法查找第一个匹配的字符串
match = re.search(pattern, text)

print(match.span())