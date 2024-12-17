# 编写一段随机字符串,用于re模块学习测试
import random
import string

# 生成随机长度的字符串
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))

# 生成随机字符串
random_string = generate_random_string(100)

# 打印随机字符串
# print(random_string)
data = r"""c]hF4~<_F&D>B*6q#[S!DZQDJh0lxCXkn%eqf3-xwY;prX9oJrlO$;G0`[y\xCOz}Nw2nFM;!(G";y$FD]_~t-F>G!kE2;8!hbS\""""
# print(data)






