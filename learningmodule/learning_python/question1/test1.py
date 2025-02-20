import re

# 单词统计：统计文件中每个单词出现的次数，忽略单词的大小写。例如，"The" 和 "the" 应被视为同一个单词。
# 词频排序：按照单词出现的频率从高到低对单词进行排序。
# 高频词输出：输出出现频率最高的前 10 个单词及其出现次数。
# 独特单词统计：统计文件中独特单词（不重复的单词）的数量。
def solve_qusetion1():

    # 读取txt内容
    with open('article.txt','r',encoding='utf-8') as f:
        txtlines = f.readlines()
    # 定义一个字典存储单词出现格式
    word_dict = {}
    for line in txtlines:
        word_list = re.findall(r'\b\w+\b',line)
        for word in word_list:
            if word.lower() not in word_dict.keys():
                word_dict[word.lower()] = 1
            else:
                word_dict[word.lower()] += 1

    sort_dict = sorted(word_dict.items(),key=lambda item:item[1],reverse=True)
    for i in range(10):
        print(f'{sort_dict[i][0]}单词第{i+1}多，共出现{sort_dict[i][1]}次')
    a = 0
    for word in sort_dict:
        if word[1] ==1:
            a += 1
    print(f'出现一次的单词共有{a}个')
if __name__ == '__main__':

    solve_qusetion1()