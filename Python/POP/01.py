'''
定义一个学生类来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类,pass代表直接跳过
    # 此处pass必须有
    pass
# 定义一个对象
mingyue = Student()

# 定义一个厅Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course =  "Python"
    # 需要注意:
    # 1 def的层级要小于class的层级
    # 2 系统默认室友一个self参数
    def doHomework(self):
        print("i do work!")
        # 在函数末尾使用return
        return None
#实例化一个叫mingyueyue的学生,是一个具体的人
mingyueyue = PythonStudent()
print(mingyueyue.name)
print(mingyueyue.age)
# 注意成员函数的调用没有传递如参数
mingyueyue.doHomework()