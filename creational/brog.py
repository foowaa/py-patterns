"""
单例
What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. 

In other words, the focus is on sharing state instead of sharing instance identity.

"""

'''
所有Brog的实例都会共享共同的属性。

之后可以随意定义对象，并创建对象，他们都是共享的，也就是说一个改变对象属性，其他全都会随之改变。“但是不同对象的id并不一样”，所以更准确的称呼是“monostate”。
'''


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
