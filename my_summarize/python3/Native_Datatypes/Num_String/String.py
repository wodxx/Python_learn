s1 = ':dog:\n'
s2 = "Dogge's home"  # 双引号在前后加逗号

# 三引号表示分行输出
s3 = """   
hello,
Dogge!
"""

print(type(s1))
print("%s, %s, %s" % (s1, s2, s3))


##############################################   转义字符：

# \可以转义很多字符，比如
# \ 什么也不表示，也不用print出来
# \n表示换行，
# \t表示制表符,即空4个空格
# 如果字符\本身也要转义，\\表示的字符就是\
# """...""" 为分行表示


###############################################   占位符
# 用来格式化字符串的。在字符串内部，

# %s表示用字符串替换，
# %f表示用浮点数替换
# %x表示用十六进制整数替换
# %d表示用整数替换，
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
# 如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

# 求一个字符串的字符个数length
print(len(s1))

################################################   Slicing（切片）

## 左数切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[1:3] # 索引从1开始取两个元素
['Sarah', 'Tracy']

L[0:3] # 取前三个元素
['Michael', 'Sarah', 'Tracy']

# 如果第一个索引是0，还可以省略
L[0:3] == L[:3]

## 倒数切片

L[-2:] # 从倒数第二个元素开始取完
# ['Bob', 'Jack']
L[-2:-1] # 从倒数第二个元素开始取到倒数第一个元素之前，倒数第一个元素不取
# ['Bob']

## 隔一定索引取法
L[:10:2] # 前10个数，每两个取一个
L[:]  # 原**复制**一遍
L[1 : 3] # 方括号内没有第三个数表示 默认为1 步进为1

## 方括号第三个为负值得情况：
L[::-1] # 当第三个为负值，前两个分别默认为-1 和 -len(L)-1。
# 即步进为1倒着从最后一个值取到第一个值，**常用于反转字符串**。


##############################################  类型转换  -> str

x = {1, 2, 3}             # 这里不管x是什么类型，转str都是给x加上双引号
print(str(x))             # "{1, 2, 3}"