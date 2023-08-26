# 循环

## 两类循环
**1. for x in n(可迭代对象或range())**

**2. while 条件： 表达式**


## 两个函数

**1. range()****

    Python提供一个**range()函数**，可以生成一个**整数序列**，再通过**list()函数**可以转换为list。比如range(5)生成的序列是从0开始**小于5**的整数：
    ```python
    xulie = list(range(5)) ## list列表装入一个从0-5的整数序列
    print(xulie)  ## [0, 1, 2, 3, 4] 
    # 这个list()函数有点像数据类型转换函数，将其他类型数据转换为该函数的类型数据
    ```

**2. input()函数**
birth = input('birth: ')

## 两个词语

**1. break**：在循环中，break语句可以提前退出循环。一般在一个条件语句后面

**2. continue** ：在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。一般用在一个if条件语句后用continue直接下一次循环。**与break不同的是continue不停止循环，而是跳过当前语句，重新开启新循环。**

> break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。


## enumerate() 函数  
该函数属于非常有用的高级用法     

<<<<<<< HEAD
```txt
    for index in enumrate(list1)
    
    dict.get(键）
    for index, value in enumrate(dict, 1):
    print(f'{index}: {value}')
    
    1: Alice
    2: Bob
    3: Carl 
    
    将Python的enumerate()函数默认0起始索引值修改为1（或者其他任何整形值，根据需求去设置不同值）
=======
```python
for index in enumrate(list1)

dict.get(键）
for index, value in enumrate(dict, 1):
print(f'{index}: {value}')

1: Alice
2: Bob
3: Carl 

将Python的enumerate()函数默认0起始索引值修改为1（或者其他任何整形值，根据需求去设置不同值）
>>>>>>> 1d24433b52d684d0f5763d8ae09345f2f0d903ad
```