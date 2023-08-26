# a = 1
# b = 0 * 10
# print(type(a))

# c = 1.2
# d = .5
# g = .314e1
# print(type(g)) 
# print(g)

# complex 复数数据类型
# e = 1 + 2j  # 格式为 a + bj 或者复数函数complex（a，b)
# f = complex(1, 2)  
# print(type(e))
# print("e = ", e)
# print(f == e)


# Operators  + - * / ** // %

# print(1 + 1)
# print(2 - 2)
# print(3 * 3)
# print(5 / 4)
# print(2 ** 10)  # 平方
# print(5 // 4)   # 求商数
# print(5 % 4)    # 求模

# print(5 // 2)
# print(5 % 2)

# print(10 / 3)   # 会保留15位小数

# Casting

# Integer/Stirng -> float

print(float(3))
print(3 / 1)
print(float("3.14"))

# float/string -> Interge
print(int(3.14))
print(int("3", base = 10))  # 10进制转10进制
print(int("1010", base = 2)) # 2进制转10进制
print(int("0b1010", base = 0)) # 0b或者0B开头也是2进制，2进制转十进制
print(bin(32)) # 转二进制
print(oct(32)) # 转八进制
print(hex(32)) # 转十六进制