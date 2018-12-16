"""
工厂方法
What is this pattern about?
The Factory Method pattern can be used to create an interface for a
method, leaving the implementation to the class that gets
instantiated.

"""
'''
工厂方法使用函数创建对象, cls_name是类的映射的关键字，使用clses字典表示可以使用的类别。
'''


def create_obj(cls_name):
    """The factory method"""
    clses = dict(cls_name_1: cls_1, cls_name_2: cls_2)
    return clses[cls_name]()
