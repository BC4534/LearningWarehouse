# 从数据字段列表中选择所有可能的 A 和 B 组合，要求 A 和 B 必须不同。
# 将每组 A 和 B 代入公式模板，生成对应的公式。
# 输出所有公式，并统计总的组合数量。
# 数据字段列表：fnd17_oxlcxspebq, fnd17_shsoutbs, fnd28_value_05191q, fnd28_value_05301q,fnd28_value_05302q, fnd17_pehigh,
# fnd17_pelow, fnd17_priceavg150day,fnd17_priceavg200day, fnd17_priceavg50day, fnd17_pxedra, fnd28_newa3_value_18191a,
# fnd28_value_02300a, mdl175_ebitda, mdl175_pain
# 参考的其中一个输出：
# ts_regression(ts_zscore(fnd17_oxlcxspebq, 500), ts_zscore(fnd17_shsoutbs, 500), 500)
import itertools

data_list = [
    'fnd17_oxlcxspebq',
    'fnd17_shsoutbs',
    'fnd28_value_05191q',
    'fnd28_value_05301q',
    'fnd28_value_05302q',
    'fnd17_pehigh',
    'fnd17_pelow',
    'fnd17_priceavg150day',
    'fnd17_priceavg200day',
    'fnd17_priceavg50day',
    'fnd17_pxedra',
    'fnd28_newa3_value_18191a',
    'fnd28_value_02300a',
    'mdl175_ebitda',
    'mdl175_pain'
]
a = 0
length = len(data_list)
for i in range(length):
    for j in range(length):
        if i == j:
            continue
        else:
            print(f"ts_regression(ts_zscore({data_list[i]}, 500), ts_zscore({data_list[j]}, 500), 500)")
            a = a + 1
print(f'总共有{a}中')

print('-------------------------------')
b = 0
permutations = itertools.permutations(data_list, 2)
for item in permutations:
    b += 1
    print(f"ts_regression(ts_zscore({item[0]}, 500), ts_zscore({item[1]}, 500), 500)")
print(b)
