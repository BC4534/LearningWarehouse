import re


def read_file(file_path):
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容的行列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"错误：未找到文件 {file_path}。")
        return []


def count_words(lines):
    """
    统计每个单词的出现次数
    :param lines: 文件内容的行列表
    :return: 包含单词及其出现次数的字典
    """
    word_dict = {}
    for line in lines:
        word_list = re.findall(r'\b\w+\b', line)
        for word in word_list:
            word = word.lower()
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    return word_dict


def sort_words(word_dict):
    """
    按词频从高到低对单词进行排序
    :param word_dict: 包含单词及其出现次数的字典
    :return: 排序后的单词列表
    """
    return sorted(word_dict.items(), key=lambda item: item[1], reverse=True)


def print_top_10_words(sorted_words):
    """
    输出出现频率最高的前 10 个单词及其出现次数
    :param sorted_words: 排序后的单词列表
    """
    print("出现频率最高的前 10 个单词：")
    for i, (word, count) in enumerate(sorted_words[:10], start=1):
        print(f"排名第 {i}：单词 '{word}' 共出现 {count} 次")


def count_unique_words(word_dict):
    """
    统计独特单词的数量
    :param word_dict: 包含单词及其出现次数的字典
    :return: 独特单词的数量
    """
    return len(word_dict)


def solve_question1():
    file_path = 'article.txt'
    lines = read_file(file_path)
    if not lines:
        return
    word_dict = count_words(lines)
    sorted_words = sort_words(word_dict)
    print_top_10_words(sorted_words)
    unique_word_count = count_unique_words(word_dict)
    print(f"文件中独特单词的数量为：{unique_word_count}")


if __name__ == '__main__':
    solve_question1()