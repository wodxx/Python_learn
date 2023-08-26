# 封装
# class Student():
#     Name = 'wxh'   # 类自己的属性

# #     def __init__ (self, name, score):
# #         self.name = name
# #         self.score = score

# #     def print_score(self):
# #         print("%s : %s" % (self.name, self.score))
              
# # wuxuhui = Student('wuxuhui', 100)

# # print(wuxuhui.Name)  # 实例来调用父类的属性
# # print(Student.Name)  # 类本身调用自己的属性
# # print(wuxuhui.print_score())

 
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score  # 让属性变私有

#     def get_name (self) :
#         return self.__name
    
#     def get_score (self) :
#         return self.__score   # 让外部代码获取私有属性  
    
#     def set_score (self, score) : # 允许外部代码修改类私有属性
#         self.__score = score

#     def print_score(self):
#         print("%s : %s" % (self.__name, self.__score))

# wuxuhui = Student('wxh', 100)


# # 当类中的属性变为私有时，实例想要调用类中的函数
# # 类中必须有让外部代码获取私有属性的方法 即上面的def get_name()
# print(wuxuhui.print_score())

###############################################################
# 继承

# class Animal(object):
#     def run(self):
#         print("Animal is running...")

# # 子类1
# class Dog(Animal):
#     pass

# # 子类2
# class Cat(Animal):
#     def run(self):
#         print("Cat is running...")

# # 给子类2举实例，并调用父类的方法如下：
# cat = Cat()
# print(cat.run())  # 此时打印子类的函数执行

# 给子类写自己的run()方法,则调用run()方法会打印子类的方法


#################################################################
# 多态
class Animal(object):
    def run(self):
        print("Animal is running...")

# 子类1
class Dog(Animal):
    # def run(self):  #子类的run()函数
    #     print("Dog is running...")
    pass

# 子类2
class Cat(Animal):
    def run(self):
        print("Cat is running...")

# 给子类2举实例，并调用父类的方法如下：
cat = Cat()
print(cat.run())  # 此时打印子类的函数执行
dog = Dog()

# 子类无run()函数时，实例调用run()会执行父类的run()函数 
print(dog.run()) # Animal is running...