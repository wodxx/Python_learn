# dict & set

## dict

> Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

### 形式: 

```py
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 增加一个键值对
dict.fromkeys--d.fromkeys(a,m) 字典d中键的来源 为可迭代对象 m为值的默认值
setdefault--d.setdefault(a,b) 字典d中添加a b这个键值对 有则改 无则添

# 删除一个键值对
d.pop() 删除字典d中最后的一个键值对
d.popitem(a) 删除字典d中键为a的键值对
d.clear() 清空字典d

# 查找一个值
d.get(a) 查找字典d中是否存在键为a的键值对
d.keys() 获取字典d中所有的键
d.values() 获取字典d中所有的值
d.items() 获取字典d中的所有键值对

# 修改键值对
d.update(a) # 更新字典中d中a键对应的值

# 遍历一个dict
for key in dict.keys(): # 遍历键

for value in dict.values(): # 遍历值

for key, value in dict.items(): 遍历键值对

```

### 与list比较

请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

1. 查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

2. 而list相反,查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。

所以，**dict是用空间来换取时间**的一种方法;且需要注意,dict的key必须是不可变对象.


## set

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。


### 形式: 

```py
s = {1，2，3}

# 增加一个元素
s.add(a) 向集合s中增加元素a

# 删除一个键值对
s.pop() 随机删除集合s中的某个元素并返回值
s.remove(a) 删除集合s中的a元素

# 查找一个值
a.issubset(b) 集合a是否为b的子集
a.issuperset(b) 集合a是否为b的父集
a.isdisjoint(b) 集合a与b之间是否没有交集

# 修改键值对
s.update(d) # 将可迭代对象d的元素撒入集合s中

```