
'''
定义一个学生类，用来形容学生
'''
# 定义一个类
class Student():
    pass

# 定义一个对象
sxc = Student()

#  再定义一个类,用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    home = "japan"
    course = "python"

    # 系统默认的self参数
    def doHomework(self):
        print("get out")
        #  推荐在函数末尾使用return语句
        return None
# 示例化一个具体的人
cxk = PythonStudent()
print(cxk.name)
print(cxk.age)
cxk.doHomework()
PythonStudent.__dict__

