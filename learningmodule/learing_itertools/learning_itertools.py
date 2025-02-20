import itertools
from traceback import print_tb

counter = itertools.count(2,3)
for i in range(5):
    print(next(counter))

counter2 = itertools.cycle(['a','b','c'])
for i in range(7):
    print(next(counter2))

counter3 = itertools.repeat(['a','b','c'],3)
print(next(counter3))
print(next(counter3))
print(next(counter3))

resout1 = itertools.product(['a','b','c'],['1','2'])
for item in resout1:
    print(item)
print("++++++++++++++++++++++++++++++++++++")

resout2 = itertools.permutations(['a','b','c'],2)
for item in resout2:
    print(item)
print("________________________________________")
resout3 = itertools.combinations(['a','b','c'],2)
for item in resout3:
    print(item)
print("________________________________________")
resout4 = itertools.combinations_with_replacement(['a','b','c'],2)
for i in resout4:
    print(''.join(i))
print("________________________________________")
resout5 = itertools.chain(["1","2"],["a","b"])
for item in resout5:
    print(item)
print("________________________________________")
data = [1, 2, 3, 4]
selectors = [True, False, True, False]
resout6 = itertools.compress(data,selectors)
for item in resout6:
    print(item)

print("________________________________________")
iterable = [1, 2, 3, 4, 5]
drop = itertools.dropwhile(lambda x:x<3,iterable)
for i in drop:
    print(i)
print("________________________________________")
take = itertools.takewhile(lambda x:x<3,iterable)
for i in take:
    print(i)
print("________________________________________")
iterable = [1, 2, 3, 4, 5]
groups = itertools.groupby(iterable,key=lambda x:x<3)
for key,group in groups:
    print(f"Key: {key}, Values: {list(group)}")